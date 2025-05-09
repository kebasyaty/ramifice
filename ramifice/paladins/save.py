"""Create or update document in database."""

from datetime import datetime
from typing import Any

from pymongo.asynchronous.collection import AsyncCollection

from .. import store
from ..errors import PanicError
from ..tools import model_is_migrated
from ..types import CheckResult


class SaveMixin:
    """Create or update document in database."""

    async def save(self) -> bool:
        """Create or update document in database.
        This method pre-uses the `check` method.
        """
        # Check if this model is migrated to database.
        model_is_migrated(self.__class__)
        # Get collection.
        collection: AsyncCollection = store.MONGO_DATABASE[self.__class__.META["collection_name"]]  # type: ignore[index, attr-defined]
        # Check and get CheckResult.
        result_check: CheckResult = await self.check(is_save=True, collection=collection)  # type: ignore[attr-defined]
        # Reset the alerts to exclude duplicates.
        self.hash.alerts = []  # type: ignore[index, attr-defined]
        # Check the conditions and, if necessary, define a message for the web form.
        if not result_check.is_update and not self.__class__.META["is_create_doc"]:  # type: ignore[index, attr-defined]
            self.hash.alerts.append("It is forbidden to create new documents !")  # type: ignore[index, attr-defined]
            result_check.is_valid = False
        if result_check.is_update and not self.__class__.META["is_update_doc"]:  # type: ignore[index, attr-defined]
            self.hash.alerts.append("It is forbidden to update documents !")  # type: ignore[index, attr-defined]
            result_check.is_valid = False
        # Leave the method if the check fails.
        if not result_check.is_valid:
            self.ignored_fields_to_none()  # type: ignore[index, attr-defined]
            return False
        # Get data for document.
        checked_data: dict[str, Any] = result_check.data
        # Create or update a document in database.
        if result_check.is_update:
            # Update date and time.
            checked_data["updated_at"] = datetime.now()
            # Run hook.
            self.pre_update()  # type: ignore[index, attr-defined]
            # Update doc.
            await collection.update_one(
                {"_id": checked_data["_id"]}, {"$set": checked_data}
            )
            # Run hook.
            self.post_update()  # type: ignore[index, attr-defined]
            # Refresh Model.
            mongo_doc = await collection.find_one({"_id": checked_data["_id"]})
            self.update_from_doc(mongo_doc)  # type: ignore[index, attr-defined]
        else:
            # Add date and time.
            today = datetime.now()
            checked_data["created_at"] = today
            checked_data["updated_at"] = today
            # Run hook.
            self.pre_create()  # type: ignore[index, attr-defined]
            # Insert doc.
            await collection.insert_one(checked_data)  # type: ignore[index, attr-defined]
            # Run hook.
            self.post_create()  # type: ignore[index, attr-defined]
            # Refresh Model.
            mongo_doc = await collection.find_one({"_id": checked_data["_id"]})
            if mongo_doc is not None:
                self.update_from_doc(mongo_doc)  # type: ignore[index, attr-defined]
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
