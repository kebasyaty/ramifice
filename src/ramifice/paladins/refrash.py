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
"""Update Model instance from database."""

from __future__ import annotations

__all__ = ("RefrashMixin",)

import logging
from typing import Any

from pymongo.asynchronous.collection import AsyncCollection

from ramifice.config import Config
from ramifice.errors import PanicError
from ramifice.paladins.utils import refresh_from_mongo_doc

logger = logging.getLogger(__name__)


class RefrashMixin:
    """Update Model instance from database."""

    async def refrash_from_db(self) -> None:
        """Update Model instance from database."""
        metadata = self.__class__.META
        # Get collection.
        collection: AsyncCollection = Config.MONGO_DATABASE[metadata["collection_name"]]
        mongo_doc: dict[str, Any] | None = await collection.find_one(filter={"_id": self._id.value})
        if mongo_doc is None:
            err_msg = (
                f"Model: `{self.full_model_name()}` > "
                + "Method: `refrash_from_db` => "
                + f"A document with an identifier `{self._id.value}` is not exists in the database!"
            )
            logger.critical(err_msg)
            raise PanicError(err_msg)
        self.inject()
        refresh_from_mongo_doc(self, mongo_doc)
