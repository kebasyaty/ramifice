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
"""Delete document from database."""

from __future__ import annotations

__all__ = ("DeleteMixin",)

import logging
from os import remove
from shutil import rmtree
from typing import Any

from anyio import to_thread
from pymongo.asynchronous.collection import AsyncCollection

from ramifice.config import Config
from ramifice.errors import ForbiddenDeleteDocError, PanicError

logger = logging.getLogger(__name__)


class DeleteMixin:
    """Delete document from database."""

    async def delete(
        self,
        remove_files: bool = True,
        projection: Any | None = None,
        sort: Any | None = None,
        hint: Any | None = None,
        session: Any | None = None,
        let: Any | None = None,
        comment: Any | None = None,
        **kwargs: dict[str, Any],
    ) -> dict[str, Any]:
        """Delete document from database."""
        metadata = self.__class__.META
        # Raises a panic if the Model cannot be removed.
        if not metadata["is_delete_doc"]:
            err_msg = (
                f"Model: `{metadata['full_model_name']}` > "
                + "META param: `is_delete_doc` (False) => "
                + "Documents of this Model cannot be removed from the database!"
            )
            logger.warning(err_msg)
            raise ForbiddenDeleteDocError(err_msg)
        # Get documet ID.
        doc_id = self.id
        if doc_id is None:
            err_msg = f"Model: `{metadata['full_model_name']}` > " + "Field: `id` => ID is missing."
            logger.critical(err_msg)
            raise PanicError(err_msg)
        # Run hook.
        await self.pre_delete()
        # Get collection for current Model.
        collection: AsyncCollection = Config.MONGO_DATABASE[metadata["collection_name"]]
        # Delete document.
        mongo_doc: dict[str, Any] | None = {}
        mongo_doc = await collection.find_one_and_delete(
            filter={"_id": doc_id},
            projection=projection,
            sort=sort,
            hint=hint,
            session=session,
            let=let,
            comment=comment,
            **kwargs,
        )
        # If the document failed to delete.
        if not bool(mongo_doc):
            err_msg = (
                f"Model: `{metadata['full_model_name']}` > "
                + "Method: `delete` => "
                + "The document was not deleted, the document is absent in the database."
            )
            logger.critical(err_msg)
            raise PanicError(err_msg)
        # Delete orphaned files and add None to field.value.
        file_data: dict[str, Any] | None = None
        for f_name in metadata["all_descriptor_fields"]:
            f_attrs = getattr(self, f"{f_name}__attrs")
            if remove_files and not f_attrs.ignored:
                group = f_attrs.group
                if group == "file":
                    file_data = mongo_doc[f_name]
                    if file_data is not None and len(f_attrs.value["path"]) > 0:
                        await to_thread.run_sync(remove, f_attrs.value["path"])
                    file_data = None
                elif group == "img":
                    file_data = mongo_doc[f_name]
                    if file_data is not None and len(f_attrs.value["imgs_dir_path"]) > 0:
                        # pyrefly: ignore [incompatible-overload-residual]
                        await to_thread.run_sync(rmtree, f_attrs.value["imgs_dir_path"])
                    file_data = None
            setattr(self, f_name, None)
        # Run hook.
        await self.post_delete()
        #
        return mongo_doc
