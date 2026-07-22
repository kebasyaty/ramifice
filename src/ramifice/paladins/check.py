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
from xloft import NamedTuple

from ramifice.config import Config
from ramifice.paladins.groups import (
    BoolGroupMixin,
    ChoiceGroupMixin,
    DateGroupMixin,
    FileGroupMixin,
    IDGroupMixin,
    ImgGroupMixin,
    NumberGroupMixin,
    PasswordGroupMixin,
    SlugGroupMixin,
    TextGroupMixin,
)

logger = logging.getLogger(__name__)


class CheckMixin(
    BoolGroupMixin,
    ChoiceGroupMixin,
    DateGroupMixin,
    FileGroupMixin,
    IDGroupMixin,
    ImgGroupMixin,
    NumberGroupMixin,
    PasswordGroupMixin,
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
        metadata = self.__class__.META
        descriptor_fields = self.__class__.META["all_descriptor_fields"]

        # Get the document ID.
        doc_id: ObjectId | None = self.id.value
        # Does the document exist in the database?
        is_update: bool = doc_id is not None
        # Create an identifier for a new document.
        if is_save and not is_update:
            doc_id = ObjectId()
            self.id = doc_id

        result_map: dict[str, Any] = {}
        # Errors from additional validation of fields.
        error_map: NamedTuple = await self.add_validation()
        # Get Model collection.
        if collection is None:
            collection = Config.MONGO_DATABASE[metadata["collection_name"]]
        # Create params for *_group methods.
        params: dict[str, Any] = {
            "doc_id": doc_id,
            "is_save": is_save,
            "is_update": is_update,  # Does the document exist in the database?
            "is_error_symptom": False,  # Is there any incorrect data?
            "result_map": result_map,  # Data to save or update to the database.
            "collection": collection,
            "field_value": None,
            "f__attrs": None,
            "f__funcs": None,
            "full_model_name": metadata["full_model_name"],
            "is_migration_process": is_migration_process,
            "curr_doc": (await collection.find_one({"_id": doc_id}) if is_save and is_update else None),
            "_": self._RAMIFICE_TRANSLATOR.gettext,
        }

        # Run checking fields.
        for field_name in descriptor_fields:
            f__attrs = getattr(self, f"{field_name}__attrs")
            # Reset a field errors to exclude duplicates.
            f__attrs["errors"] = []
            # Check additional validation.
            err_msg = error_map[field_name]
            if err_msg is not None:
                f__attrs["errors"].append(err_msg)
                if not params["is_error_symptom"]:
                    params["is_error_symptom"] = True
            # Checking the fields by groups.
            if not f__attrs["ignored"]:
                params["field_value"] = getattr(self, field_name)
                params["f__attrs"] = f__attrs
                match f__attrs["group"]:
                    case "text":
                        await self.text_group(params)
                    case "number":
                        await self.number_group(params)
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
                    case "password":
                        self.password_group(params)
                    case _ as unreachable:
                        err_msg: str = f"Unacceptable group `{unreachable}`!"
                        logger.critical(err_msg)
                        assert_never(unreachable)

        # Actions in case of error.
        if is_save:
            if params["is_error_symptom"]:
                # Reset the ObjectId for a new document.
                if not is_update:
                    # pyrefly: ignore [bad-assignment]
                    self.id = None
                # Delete orphaned files.
                curr_doc: dict[str, Any] | None = params["curr_doc"]

                for field_name in descriptor_fields:
                    f__attrs = getattr(self, f"{field_name}__attrs")

                    match f__attrs["group"]:
                        case "file":
                            file_data = result_map.get(field_name)
                            if file_data is not None:
                                if file_data["is_new_file"]:
                                    await to_thread.run_sync(remove, file_data["path"])
                                f__attrs["value"] = None
                                setattr(self, field_name, None)
                            if curr_doc is not None:
                                f__attrs["value"] = curr_doc[field_name]
                                setattr(self, field_name, curr_doc[field_name])
                        case "img":
                            img_data = result_map.get(field_name)
                            if img_data is not None:
                                if img_data["is_new_img"]:
                                    # pyrefly: ignore [incompatible-overload-residual]
                                    await to_thread.run_sync(rmtree, img_data["imgs_dir_path"])
                                f__attrs["value"] = None
                                setattr(self, field_name, None)
                            if curr_doc is not None:
                                f__attrs["value"] = curr_doc[field_name]
                                setattr(self, field_name, curr_doc[field_name])
            else:
                for field_name in descriptor_fields:
                    f__attrs = getattr(self, f"{field_name}__attrs")

                    if f__attrs["ignored"]:
                        continue

                    match f__attrs["group"]:
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
