"""Create or update document in database."""

from datetime import datetime

from .. import store
from ..errors import PanicError


class SaveMixin:
    """Create or update document in database."""

    async def save(self) -> bool:
        """Create or update document in database.
        This method pre-uses the `check` method.
        """
        if not self.__class__.META["is_migrat_model"]:  # type: ignore[attr-defined]
            msg = (
                f"Model: `{self.full_model_name()}` > "  # type: ignore[attr-defined]
                + "Param: `is_migrat_model` (False) => "
                + "This Model is not migrated to database!"
            )
            raise PanicError(msg)
        # Get collection.
        collection = store.MONGO_DATABASE[self.__class__.META["collection_name"]]  # type: ignore[index, attr-defined]
        # Check and get ResultCheck.
        result_check = self.check(is_save=True)  # type: ignore[attr-defined]
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
        checked_data = result_check.data
        # Create or update a document in database.
        if result_check.is_update:
            # Update date and time.
            checked_data["updated_at"] = datetime.now()
            # Run hook.
            self.pre_update()  # type: ignore[index, attr-defined]
            # Update doc.
            mongo_doc = await collection.find_one({"_id": checked_data["_id"]})
            if mongo_doc is not None:
                collection.find_one({"_id": checked_data["_id"]}, checked_data)
            # Run hook.
            self.post_update()  # type: ignore[index, attr-defined]
            # Refresh Model.
            self.update_from_doc(mongo_doc)  # type: ignore[index, attr-defined]
        else:
            pass
        #
        # If everything is completed successfully.
        return True
