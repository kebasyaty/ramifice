"""Tools - A set of additional auxiliary methods for Paladins."""

import os
import shutil
from datetime import datetime
from typing import Any

from pymongo.asynchronous.collection import AsyncCollection
from termcolor import colored

from .. import store
from ..errors import PanicError
from ..tools import model_is_migrated
from ..types import CheckResult, FileData, ImageData


class ToolsMixin:
    """A set of additional auxiliary methods for Paladins."""

    async def is_valid(self) -> bool:
        """Check data validity.
        The main use is to check data from web forms.
        """
        result_check: CheckResult = await self.check()  # type: ignore[attr-defined]
        return result_check.is_valid

    def print_err(self) -> None:
        """Printing errors to the console.
        Convenient to use during development.
        """
        is_err: bool = False
        for field_name, field_data in self.__dict__.items():
            if callable(field_data):
                continue
            if len(field_data.errors) > 0:
                # title
                if not is_err:
                    print(colored("\nERRORS:", "red", attrs=["bold"]))
                    print(colored("Model: ", "blue", attrs=["bold"]), end="")
                    print(colored(f"`{self.full_model_name()}`", "blue"))  # type: ignore[attr-defined]
                    is_err = True
                # field name
                print(colored("Field: ", "green", attrs=["bold"]), end="")
                print(colored(f"`{field_name}`:", "green"))
                # error messages
                print(colored("\n".join(field_data.errors), "red"))
        if len(self.hash.alerts) > 0:  # type: ignore[attr-defined]
            # title
            print(colored("AlERTS:", "yellow", attrs=["bold"]))
            # messages
            print(colored("\n".join(self.hash.alerts), "yellow"), end="\n\n")  # type: ignore[attr-defined]
        else:
            print(end="\n\n")

    def accumulate_error(self, err_msg: str, params: dict[str, Any]) -> None:
        """For accumulating errors to ModelName.field_name.errors"""
        if not params["field_data"].hide:
            params["field_data"].errors.append(err_msg)
            if not params["is_error_symptom"]:
                params["is_error_symptom"] = True
        else:
            msg = (
                f">>hidden field<< - Model: `{self.full_model_name()}` > "  # type: ignore[attr-defined]
                + f"Field: `{params["field_data"].name}`"
                + f" => {err_msg}"
            )
            raise PanicError(msg)

    async def check_uniqueness(
        self,
        value: str | int | float | datetime,
        params: dict[str, Any],
    ) -> bool:
        """Check the uniqueness of the value in the collection."""
        q_filter = {
            "$and": [
                {"_id": {"$ne": params["doc_id"]}},
                {params["field_data"].name: value},
            ],
        }
        return await params["collection"].find_one(q_filter) is None

    def ignored_fields_to_none(self):
        """Reset the values ​​of ignored fields to None."""
        for _, field_data in self.__dict__.items():
            if (
                not callable(field_data)
                and field_data.ignored
                and field_data.name != "hash"
            ):
                field_data.value = None

    def update_from_doc(self, mongo_doc: dict[str, Any]):
        """Update object instance from Mongo document."""
        for name, data in mongo_doc.items():
            if data is None:
                continue
            if name == "_id":
                self.__dict__["hash"].value = str(data)
                continue
            field = self.__dict__[name]
            if field.group != "pass":
                if field.group == "date":
                    if field.input_type == "date":
                        data = data.strftime("%Y-%m-%d")
                    else:
                        data = data.strftime("%Y-%m-%dT%H:%M:%S")
                elif field.group == "file":
                    data = FileData.from_doc(data)
                elif field.group == "img":
                    data = ImageData.from_doc(data)
                field.value = data
            else:
                field.value = None

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
        # Get collection.
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
