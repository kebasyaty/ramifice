"""Validation of Model data before saving to the database."""

import os
import shutil
from typing import Any

from bson.objectid import ObjectId

from .. import store
from ..types import FileData, ImageData, ResultCheck
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
):
    """Validation of Model data before saving to the database."""

    # pylint: disable=too-many-branches
    async def check(self, is_save: bool = False) -> ResultCheck:
        """Validation of Model data before saving to the database."""

        # Get the document ID.
        doc_id: ObjectId | None = self.to_obj_id()  # type: ignore[attr-defined]
        # Does the document exist in the database?
        is_update: bool = bool(doc_id)
        result_map: dict[str, Any] = {}
        # Create an identifier for a new document.
        if not is_update:
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

        # Actions in case of error.
        if params["is_error_symptom"] and is_save:
            # Reset the ObjectId for a new document.
            if not is_update:
                self.hash.value = None  # type: ignore[attr-defined]
            # Delete orphaned files.
            curr_doc: dict[str, Any] | None = (
                await params["collection"].find_one({"_id": doc_id})
                if is_update
                else None
            )
            file_data: FileData | None = None
            img_data: ImageData | None = None
            json_dict: dict[str, Any] | None = None
            for field_name, field_data in self.__dict__.items():
                if callable(field_data) or field_data.ignored:
                    continue
                group = field_data.group
                if group == "file":
                    file_data = field_data.value
                    if file_data is not None:
                        if file_data.is_new_file:
                            os.remove(file_data.path)
                        field_data.value = None
                        file_data = None
                    if curr_doc is not None:
                        json_dict = curr_doc[field_name]
                        if json_dict is not None:
                            field_data.value = FileData.from_dict(json_dict)
                            json_dict = None
                    else:
                        field_data.value = None
                elif group == "img":
                    img_data = field_data.value
                    if img_data is not None:
                        if img_data.is_new_img:
                            shutil.rmtree(img_data.imgs_dir_path)
                        field_data.value = None
                        img_data = None
                    if curr_doc is not None:
                        json_dict = curr_doc[field_name]
                        if json_dict is not None:
                            field_data.value = ImageData.from_dict(json_dict)
                            json_dict = None
                    else:
                        field_data.value = None
        #
        #
        return ResultCheck(
            data=result_map,
            is_valid=not params["is_error_symptom"],
            is_update=is_update,
        )
