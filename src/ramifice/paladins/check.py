"""Validation of Model data before saving to the database."""

from __future__ import annotations

__all__ = ("CheckMixin",)

import logging
from os import remove
from shutil import rmtree
from typing import Any, assert_never

from anyio import to_thread
from bson.objectid import ObjectId
from pymongo.asynchronous.collection import AsyncCollection

from ramifice.paladins.groups import (
    BoolGroupMixin,
    ChoiceGroupMixin,
    DateGroupMixin,
    FileGroupMixin,
    IDGroupMixin,
    ImgGroupMixin,
    NumGroupMixin,
    PassGroupMixin,
    SlugGroupMixin,
    TextGroupMixin,
)
from ramifice.utils import constants

logger = logging.getLogger(__name__)


class CheckMixin(
    BoolGroupMixin,
    ChoiceGroupMixin,
    DateGroupMixin,
    FileGroupMixin,
    IDGroupMixin,
    ImgGroupMixin,
    NumGroupMixin,
    PassGroupMixin,
    SlugGroupMixin,
    TextGroupMixin,
):
    """Validation of Model data before saving to the database."""

    async def check(
        self,
        is_save: bool = False,
        collection: AsyncCollection | None = None,
        is_migration_process: bool = False,
    ) -> dict[str, Any]:
        """Validation of Model data before saving to the database.

        It is also used to verify Models that do not migrate to the database.
        """
        cls_model = self.__class__

        # Get the document ID.
        doc_id: ObjectId | None = self._id.value
        # Does the document exist in the database?
        is_update: bool = doc_id is not None
        # Create an identifier for a new document.
        if is_save and not is_update:
            doc_id = ObjectId()
            self._id.value = doc_id

        result_map: dict[str, Any] = {}
        # Errors from additional validation of fields.
        error_map: dict[str, str] = await self.add_validation()
        # Get Model collection.
        if collection is None:
            collection = constants.MONGO_DATABASE[cls_model.META["collection_name"]]
        # Create params for *_group methods.
        params: dict[str, Any] = {
            "doc_id": doc_id,
            "is_save": is_save,
            "is_update": is_update,  # Does the document exist in the database?
            "is_error_symptom": False,  # Is there any incorrect data?
            "result_map": result_map,  # Data to save or update to the database.
            "collection": collection,
            "field_data": None,
            "full_model_name": cls_model.META["full_model_name"],
            "is_migration_process": is_migration_process,
            "curr_doc": (await collection.find_one({"_id": doc_id}) if is_save and is_update else None),
        }

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
                if not params["is_error_symptom"]:
                    params["is_error_symptom"] = True
            # Checking the fields by groups.
            if not field_data.ignored:
                params["field_data"] = field_data
                match field_data.group:
                    case "text":
                        await self.text_group(params)
                    case "num":
                        await self.num_group(params)
                    case "date":
                        self.date_group(params)
                    case "img":
                        await self.img_group(params)
                    case "file":
                        await self.file_group(params)
                    case "choice":
                        self.choice_group(params)
                    case "bool":
                        self.bool_group(params)
                    case "id":
                        self.id_group(params)
                    case "slug":
                        await self.slug_group(params)
                    case "pass":
                        self.pass_group(params)
                    case _ as unreachable:
                        msg: str = f"Unacceptable group `{unreachable}`!"
                        logger.critical(msg)
                        assert_never(unreachable)

        # Actions in case of error.
        if is_save:
            if params["is_error_symptom"]:
                # Reset the ObjectId for a new document.
                if not is_update:
                    self._id.value = None
                # Delete orphaned files.
                curr_doc: dict[str, Any] | None = params["curr_doc"]
                for field_name, field_data in self.__dict__.items():
                    if callable(field_data) or field_data.ignored:
                        continue
                    match field_data.group:
                        case "file":
                            file_data = result_map.get(field_name)
                            if file_data is not None:
                                if file_data["is_new_file"]:
                                    await to_thread.run_sync(remove, file_data["path"])
                                field_data.value = None
                            if curr_doc is not None:
                                field_data.value = curr_doc[field_name]
                        case "img":
                            img_data = result_map.get(field_name)
                            if img_data is not None:
                                if img_data["is_new_img"]:
                                    await to_thread.run_sync(rmtree, img_data["imgs_dir_path"])
                                field_data.value = None
                            if curr_doc is not None:
                                field_data.value = curr_doc[field_name]
            else:
                for field_name, field_data in self.__dict__.items():
                    if callable(field_data) or field_data.ignored:
                        continue
                    match field_data.group:
                        case "file":
                            file_data = result_map.get(field_name)
                            if file_data is not None:
                                file_data["is_new_file"] = False
                        case "img":
                            img_data = result_map.get(field_name)
                            if img_data is not None:
                                img_data["is_new_img"] = False
        #
        return {
            "data": result_map,
            "is_valid": not params["is_error_symptom"],
            "is_update": is_update,
        }
