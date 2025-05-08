"""Delete document from database."""

import os
import shutil
from typing import Any

from pymongo.asynchronous.collection import AsyncCollection

from .. import store
from ..errors import PanicError
from ..tools import model_is_migrated


class DeleteMixin:
    """Delete document from database."""

    async def delete(
        self,
        delete_files: bool = True,
        projection=None,
        sort=None,
        hint=None,
        session=None,
        let=None,
        comment=None,
        **kwargs,
    ) -> dict[str, Any]:
        """Delete document from database."""
        cls_model = self.__class__
        # Check if this model is migrated to database.
        model_is_migrated(cls_model)
        #
        if not cls_model.META["is_delete_doc"]:  # type: ignore[index, attr-defined]
            msg = (
                f"Model: `{cls_model.META["full_model_name"]}` > "  # type: ignore[index, attr-defined]
                + "Param: `is_delete_doc` (False) => "
                + "Documents of this Model cannot be removed from the database!"
            )
            raise PanicError(msg)
        # Get documet ID.
        doc_id = self.to_obj_id()  # type: ignore[index, attr-defined]
        if doc_id is None:
            msg = (
                f"Model: `{cls_model.META["full_model_name"]}` > "  # type: ignore[index, attr-defined]
                + "Field: `hash` > "
                + "Param: `value` => Hash is missing."
            )
            raise PanicError(msg)
        # Run hook.
        self.pre_delete()  # type: ignore[index, attr-defined]
        # Get collection for current Model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls_model.META["collection_name"]]  # type: ignore[index, attr-defined]
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
                f"Model: `{cls_model.META["full_model_name"]}` > "  # type: ignore[index, attr-defined]
                + "Method: `delete` => "
                + "The document was not deleted, the document is absent in the database."
            )
            raise PanicError(msg)
        # Delete orphaned files.
        file_data: dict[str, Any] | None = None
        for field_name, field_data in self.__dict__.items():
            if callable(field_data):
                continue
            if delete_files and not field_data.ignored:
                group = field_data.group
                if group == "file":
                    file_data = mongo_doc[field_name]
                    if file_data is not None and len(file_data["path"]) > 0:
                        os.remove(file_data["path"])
                    file_data = None
                elif group == "img":
                    file_data = mongo_doc[field_name]
                    if file_data is not None and len(file_data["imgs_dir_path"]) > 0:
                        shutil.rmtree(file_data["imgs_dir_path"])
                    file_data = None
            field_data.value = None
        # Run hook.
        self.post_delete()  # type: ignore[index, attr-defined]
        #
        return mongo_doc
