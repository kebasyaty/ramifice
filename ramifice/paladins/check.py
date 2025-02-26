"""Validation of Model data before saving to the database."""

from typing import Any

from bson.objectid import ObjectId

from .. import store
from ..types import OutputData
from .groups import (
    BoolGroupMixin,
    ChoiceGroupMixin,
    DateGroupMixin,
    FileGroupMixin,
    HashGroupMixin,
    ImgGroupMixin,
    NumGroupMixin,
    PassGroupMixin,
    SlugGroupMixin,
    TextGroupMixin,
)
from .tools import ToolsMixin


class CheckMixin(
    BoolGroupMixin,
    ChoiceGroupMixin,
    DateGroupMixin,
    FileGroupMixin,
    HashGroupMixin,
    ImgGroupMixin,
    NumGroupMixin,
    PassGroupMixin,
    SlugGroupMixin,
    TextGroupMixin,
    ToolsMixin,
):
    """Validation of Model data before saving to the database."""

    # pylint: disable=too-many-branches
    async def check(self, is_save: bool = False) -> OutputData:
        """Validation of Model data before saving to the database."""

        # Get the document ID.
        doc_id: ObjectId | None = self.to_obj_id()  # type: ignore[attr-defined]
        # Does the document exist in the database?
        is_update: bool = bool(doc_id)
        result_map: dict[str, Any] = {}
        # Create an identifier for a new document.
        if is_update is False:
            doc_id = ObjectId()
        if is_save:
            if not is_update:
                self.hash.value = str(doc_id)  # type: ignore[attr-defined]
            result_map["_id"] = doc_id
        # Errors from additional validation of fields.
        error_map: dict[str, str] = self.add_validation() or {}  # type: ignore[attr-defined]
        #
        params: dict[str, Any] = {
            "doc_id": doc_id,
            "is_save": is_save,
            "is_update": is_update,  # Does the document exist in the database?
            "is_error_symptom": False,  # Is there any incorrect data?
            "result_map": {},  # Data to save or update to the database.
            "collection": store.MONGO_DATABASE[self.__class__.META["collection_name"]],  # type: ignore[index, attr-defined]
            "field_data": None,
        }
        #
        # Run checking fields.
        for field_name, field_data in self.__dict__.items():
            if callable(field_data):
                continue
            # Reset a field errors to exclude duplicates.
            field_data.errors = []
            # Check additional validation.
            err_msg = error_map.get(field_name)
            if bool(err_msg):
                field_data.errors.append(err_msg)
            # Checking the fields by groups.
            if not field_data.ignored:
                group = field_data.group
                params["field_data"] = field_data
                if group == "text":
                    await self.text_group(params)
                elif group == "num":
                    await self.num_group(params)
                elif group == "date":
                    self.date_group(params)
                elif group == "img":
                    self.img_group(params)
                elif group == "file":
                    self.file_group(params)
                elif group == "choice":
                    self.choice_group(params)
                elif group == "bool":
                    self.bool_group(params)
                elif group == "hash":
                    self.hash_group(params)
                elif group == "slug":
                    self.slug_group(params)
                elif group == "pass":
                    self.pass_group(params)

        #
        #
        return OutputData(
            data=result_map,
            is_valid=not params["is_error_symptom"],
            is_update=is_update,
        )
