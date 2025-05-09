"""Verification, replacement and recoverang of password."""

from typing import Any

from argon2 import PasswordHasher
from pymongo.asynchronous.collection import AsyncCollection

from .. import store
from ..errors import PanicError
from ..tools import model_is_migrated


class PasswordMixin:
    """Verification, replacement and recoverang of password."""

    async def verify_password(
        self,
        password: str,
        field_name: str = "password",
    ) -> bool:
        """For password verification."""
        cls_model = self.__class__
        # Check if this model is migrated to database.
        model_is_migrated(cls_model)
        # Get documet ID.
        doc_id = self.to_obj_id()  # type: ignore[index, attr-defined]
        if doc_id is None:
            msg = (
                f"Model: `{cls_model.META["full_model_name"]}` > "  # type: ignore[index, attr-defined]
                + "Method: `verify_password` => "
                + "Cannot get document ID - Hash field is empty."
            )
            raise PanicError(msg)
        # Get collection for current Model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls_model.META["collection_name"]]  # type: ignore[index, attr-defined]
        # Get document.
        mongo_doc: dict[str, Any] | None = await collection.find_one({"_id": doc_id})
        if mongo_doc is None:
            msg = (
                f"Model: `{cls_model.META["full_model_name"]}` > "  # type: ignore[index, attr-defined]
                + "Method: `verify_password` => "
                + f"There is no document with ID `{self.hash.value}` in the database."  # type: ignore[index, attr-defined]
            )
            raise PanicError(msg)
        # Get password hash.
        hash = mongo_doc.get(field_name)
        if hash is None:
            msg = (
                f"Model: `{cls_model.META["full_model_name"]}` > "  # type: ignore[index, attr-defined]
                + "Method: `verify_password` => "
                + f"The model does not have a field `{field_name}`."  # type: ignore[index, attr-defined]
            )
            raise PanicError(msg)
        # Password verification.
        is_valid: bool = False
        ph = PasswordHasher()
        try:
            is_valid = ph.verify(hash, password)
        except:
            pass
        #
        return is_valid
