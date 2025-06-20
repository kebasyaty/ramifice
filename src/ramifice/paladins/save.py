"""Create or update document in database."""

from datetime import datetime
from typing import Any

from pymongo.asynchronous.collection import AsyncCollection

from ..utils import store
from ..utils.errors import PanicError
from .tools import ignored_fields_to_none, refresh_from_mongo_doc


class SaveMixin:
    """Create or update document in database."""

    async def save(self) -> bool:
        """Create or update document in database.

        This method pre-uses the `check` method.
        """
        cls_model = self.__class__
        # Get collection.
        collection: AsyncCollection = store.MONGO_DATABASE[cls_model.META["collection_name"]]  # type: ignore[index, attr-defined]
        # Check Model.
        result_check: dict[str, Any] = await self.check(is_save=True, collection=collection)  # type: ignore[attr-defined]
        # Reset the alerts to exclude duplicates.
        self._id.alerts = []  # type: ignore[attr-defined]
        # Check the conditions and, if necessary, define a message for the web form.
        if not result_check["is_update"] and not cls_model.META["is_create_doc"]:  # type: ignore[attr-defined]
            self._id.alerts.append("It is forbidden to create new documents !")  # type: ignore[attr-defined]
            result_check["is_valid"] = False
        if result_check["is_update"] and not cls_model.META["is_update_doc"]:  # type: ignore[attr-defined]
            self._id.alerts.append("It is forbidden to update documents !")  # type: ignore[attr-defined]
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
            checked_data["updated_at"] = datetime.now()
            # Run hook.
            await self.pre_update()  # type: ignore[attr-defined]
            # Update doc.
            await collection.update_one({"_id": checked_data["_id"]}, {"$set": checked_data})
            # Run hook.
            await self.post_update()  # type: ignore[attr-defined]
            # Refresh Model.
            mongo_doc: dict[str, Any] | None = await collection.find_one(
                {"_id": checked_data["_id"]}
            )
            if mongo_doc is None:
                msg = (
                    f"Model: `{self.full_model_name()}` > "  # type: ignore[attr-defined]
                    + "Method: `save` => "
                    + "Geted value is None - it is impossible to refresh the current Model."
                )
                raise PanicError(msg)
            refresh_from_mongo_doc(self, mongo_doc)
        else:
            # Add date and time.
            today = datetime.now()
            checked_data["created_at"] = today
            checked_data["updated_at"] = today
            # Run hook.
            await self.pre_create()  # type: ignore[attr-defined]
            # Insert doc.
            await collection.insert_one(checked_data)
            # Run hook.
            await self.post_create()  # type: ignore[attr-defined]
            # Refresh Model.
            mongo_doc = await collection.find_one({"_id": checked_data["_id"]})
            if mongo_doc is None:
                msg = (
                    f"Model: `{self.full_model_name()}` > "  # type: ignore[attr-defined]
                    + "Method: `save` => "
                    + "Geted value is None - it is impossible to refresh the current Model."
                )
                raise PanicError(msg)
            if mongo_doc is not None:
                refresh_from_mongo_doc(self, mongo_doc)
            else:
                msg = (
                    f"Model: `{self.full_model_name()}` > "  # type: ignore[attr-defined]
                    + "Method: `save` => "
                    + "The document was not created."
                )
                raise PanicError(msg)
        #
        # If everything is completed successfully.
        return True
