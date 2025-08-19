"""Delete document from database."""

from __future__ import annotations

__all__ = ("DeleteMixin",)

import logging
from os import remove
from shutil import rmtree
from typing import Any

from anyio import to_thread
from pymongo.asynchronous.collection import AsyncCollection

from ramifice.utils import constants
from ramifice.utils.errors import ForbiddenDeleteDocError, PanicError

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
        cls_model = self.__class__
        # Raises a panic if the Model cannot be removed.
        if not cls_model.META["is_delete_doc"]:
            msg = (
                f"Model: `{cls_model.META['full_model_name']}` > "
                + "META param: `is_delete_doc` (False) => "
                + "Documents of this Model cannot be removed from the database!"
            )
            logger.warning(msg)
            raise ForbiddenDeleteDocError(msg)
        # Get documet ID.
        doc_id = self._id.value
        if doc_id is None:
            msg = (
                f"Model: `{cls_model.META['full_model_name']}` > "
                + "Field: `_id` > "
                + "Param: `value` => ID is missing."
            )
            logger.critical(msg)
            raise PanicError(msg)
        # Run hook.
        await self.pre_delete()
        # Get collection for current Model.
        collection: AsyncCollection = constants.MONGO_DATABASE[cls_model.META["collection_name"]]
        # Delete document.
        mongo_doc: dict[str, Any] = {}
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
            msg = (
                f"Model: `{cls_model.META['full_model_name']}` > "
                + "Method: `delete` => "
                + "The document was not deleted, the document is absent in the database."
            )
            logger.critical(msg)
            raise PanicError(msg)
        # Delete orphaned files and add None to field.value.
        file_data: dict[str, Any] | None = None
        for field_name, field_data in self.__dict__.items():
            if callable(field_data):
                continue
            if remove_files and not field_data.ignored:
                group = field_data.group
                if group == "file":
                    file_data = mongo_doc[field_name]
                    if file_data is not None and len(file_data["path"]) > 0:
                        await to_thread.run_sync(remove, file_data["path"])
                    file_data = None
                elif group == "img":
                    file_data = mongo_doc[field_name]
                    if file_data is not None and len(file_data["imgs_dir_path"]) > 0:
                        await to_thread.run_sync(rmtree, file_data["imgs_dir_path"])
                    file_data = None
            field_data.value = None
        # Run hook.
        await self.post_delete()
        #
        return mongo_doc
