# Ramifice - ORM-pseudo-like API MongoDB for Python language.
# Copyright (c) 2024 Gennady Kostyunin
# SPDX-License-Identifier: MIT
#
# Copyright 2024-present MongoDB, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Create or update document in database."""

from __future__ import annotations

__all__ = ("SaveMixin",)

import logging
from datetime import datetime
from typing import Any

from pymongo.asynchronous.collection import AsyncCollection

from ramifice.config import Config
from ramifice.errors import PanicError
from ramifice.paladins.utils import ignored_fields_to_none, refresh_from_mongo_doc

logger = logging.getLogger(__name__)


class SaveMixin:
    """Create or update document in database."""

    async def save(self) -> bool:
        """Create or update document in database.

        This method pre-uses the `check` method.
        """
        metadata = self.__class__.META
        # Get collection.
        collection: AsyncCollection = Config.MONGO_DATABASE[metadata["collection_name"]]
        # Check Model.
        result_check: dict[str, Any] = await self.check(is_save=True, collection=collection)
        # Reset the alerts to exclude duplicates.
        self.id__attrs.alerts = []
        # Check the conditions and, if necessary, define a message for the web form.
        if not result_check["is_update"] and not metadata["is_create_doc"]:
            self.id__attrs.alerts.append("It is forbidden to create new documents !")
            result_check["is_valid"] = False
        if result_check["is_update"] and not metadata["is_update_doc"]:
            self.id__attrs.alerts.append("It is forbidden to update documents !")
            result_check["is_valid"] = False
        # Leave the method if the check fails.
        if not result_check["is_valid"]:
            ignored_fields_to_none(self)
            return False
        # Get data for document.
        checked_data: dict[str, Any] = result_check["data"]
        # Create or update a document in database.
        if result_check["is_update"]:
            # Update date and time.
            checked_data["updated_at"] = datetime.now(Config.UTC_TIMEZONE)
            # Run hook.
            await self.pre_update()
            # Update doc.
            await collection.update_one({"_id": checked_data["id"]}, {"$set": checked_data})
            # Run hook.
            await self.post_update()
            # Refresh Model.
            mongo_doc: dict[str, Any] | None = await collection.find_one({"_id": checked_data["id"]})
            if mongo_doc is None:
                err_msg = (
                    f"Model: `{self.full_model_name()}` > "
                    + "Method: `save` => "
                    + "Geted value is None - it is impossible to refresh the current Model."
                )
                logger.critical(err_msg)
                raise PanicError(err_msg)
            refresh_from_mongo_doc(self, mongo_doc)
        else:
            # Add date and time.
            today = datetime.now(Config.UTC_TIMEZONE)
            checked_data["created_at"] = today
            checked_data["updated_at"] = today
            # Run hook.
            await self.pre_create()
            # Insert doc.
            await collection.insert_one(checked_data)
            # Run hook.
            await self.post_create()
            # Refresh Model.
            mongo_doc = await collection.find_one({"_id": checked_data["id"]})
            if mongo_doc is None:
                err_msg = (
                    f"Model: `{self.full_model_name()}` > " + "Method: `save` => " + "The document was not created."
                )
                logger.critical(err_msg)
                raise PanicError(err_msg)
            refresh_from_mongo_doc(self, mongo_doc)
        #
        # If everything is completed successfully.
        return True
