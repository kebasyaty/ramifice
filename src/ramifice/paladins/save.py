"""Create or update document in database."""

from __future__ import annotations

__all__ = ("SaveMixin",)

import logging
from datetime import datetime
from typing import Any

from pymongo.asynchronous.collection import AsyncCollection

from ramifice.paladins.tools import ignored_fields_to_none, refresh_from_mongo_doc
from ramifice.utils import constants
from ramifice.utils.constants import UTC_TIMEZONE
from ramifice.utils.errors import PanicError

logger = logging.getLogger(__name__)


class SaveMixin:
    """Create or update document in database."""

    async def save(self) -> bool:
        """Create or update document in database.

        This method pre-uses the `check` method.
        """
        cls_model = self.__class__
        # Get collection.
        collection: AsyncCollection = constants.MONGO_DATABASE[cls_model.META["collection_name"]]
        # Check Model.
        result_check: dict[str, Any] = await self.check(is_save=True, collection=collection)
        # Reset the alerts to exclude duplicates.
        self._id.alerts = []
        # Check the conditions and, if necessary, define a message for the web form.
        if not result_check["is_update"] and not cls_model.META["is_create_doc"]:
            self._id.alerts.append("It is forbidden to create new documents !")
            result_check["is_valid"] = False
        if result_check["is_update"] and not cls_model.META["is_update_doc"]:
            self._id.alerts.append("It is forbidden to update documents !")
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
            checked_data["updated_at"] = datetime.now(UTC_TIMEZONE)
            # Run hook.
            await self.pre_update()
            # Update doc.
            await collection.update_one({"_id": checked_data["_id"]}, {"$set": checked_data})
            # Run hook.
            await self.post_update()
            # Refresh Model.
            mongo_doc: dict[str, Any] | None = await collection.find_one({"_id": checked_data["_id"]})
            if mongo_doc is None:
                msg = (
                    f"Model: `{self.full_model_name()}` > "
                    + "Method: `save` => "
                    + "Geted value is None - it is impossible to refresh the current Model."
                )
                logger.critical(msg)
                raise PanicError(msg)
            refresh_from_mongo_doc(self, mongo_doc)
        else:
            # Add date and time.
            today = datetime.now(UTC_TIMEZONE)
            checked_data["created_at"] = today
            checked_data["updated_at"] = today
            # Run hook.
            await self.pre_create()
            # Insert doc.
            await collection.insert_one(checked_data)
            # Run hook.
            await self.post_create()
            # Refresh Model.
            mongo_doc = await collection.find_one({"_id": checked_data["_id"]})
            if mongo_doc is None:
                msg = f"Model: `{self.full_model_name()}` > " + "Method: `save` => " + "The document was not created."
                logger.critical(msg)
                raise PanicError(msg)
            refresh_from_mongo_doc(self, mongo_doc)
        #
        # If everything is completed successfully.
        return True
