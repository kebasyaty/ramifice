"""Validation of Model data before saving to the database."""

from typing import Any

from bson.objectid import ObjectId

from .. import store
from ..types import OutputData


class CheckMixin:
    """Validation of Model data before saving to the database."""

    def check(self, is_save: bool = False) -> OutputData:
        """Validation of Model data before saving to the database."""

        # Get collection for Model.
        collection = store.MONGO_DATABASE[self.__class__.META["collection_name"]]  # type: ignore[index, attr-defined]
        # Data to save or update to the database.
        result_map: dict[str, Any] = {}
        # Get the document ID.
        doc_id: ObjectId | None = self.object_id()  # type: ignore[attr-defined]
        # Does the document exist in the database?
        is_update: bool = bool(doc_id)
        # Create an identifier for a new document.
        if is_update is False:
            doc_id = ObjectId()
        if is_save:
            if not is_update:
                self.hash.value = str(doc_id)  # type: ignore[attr-defined]
            result_map["_id"] = doc_id
        # Is there any incorrect data?
        is_error_symptom: bool = False
        # Errors from additional validation of fields.
        error_map: dict[str, str] = self.add_validation()  # type: ignore[attr-defined]
        # Current error message.
        err_msg: str | None = None
        #
        # Start checking all fields.

        #
        #
        return OutputData(
            data=result_map,
            is_valid=not is_error_symptom,
            is_update=is_update,
        )
