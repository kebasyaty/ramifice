"""Verification, replacement and recoverang of password."""

from typing import Any

from argon2 import PasswordHasher
from pymongo.asynchronous.collection import AsyncCollection

from ..utils import store
from ..utils.errors import OldPassNotMatchError, PanicError


class PasswordMixin:
    """Verification, replacement and recoverang of password."""

    async def verify_password(
        self,
        password: str,
        field_name: str = "password",
    ) -> bool:
        """For password verification."""
        cls_model = self.__class__
        # Get documet ID.
        doc_id = self._id.value  # type: ignore[attr-defined]
        if doc_id is None:
            msg = (
                f"Model: `{cls_model.META['full_model_name']}` > "  # type: ignore[attr-defined]
                + "Method: `verify_password` => "
                + "Cannot get document ID - ID field is empty."
            )
            raise PanicError(msg)
        # Get collection for current Model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls_model.META["collection_name"]]  # type: ignore[index, attr-defined]
        # Get document.
        mongo_doc: dict[str, Any] | None = await collection.find_one({"_id": doc_id})
        if mongo_doc is None:
            msg = (
                f"Model: `{cls_model.META['full_model_name']}` > "  # type: ignore[attr-defined]
                + "Method: `verify_password` => "
                + f"There is no document with ID `{self._id.value}` in the database."  # type: ignore[attr-defined]
            )
            raise PanicError(msg)
        # Get password hash.
        hash: str | None = mongo_doc.get(field_name)
        if hash is None:
            msg = (
                f"Model: `{cls_model.META['full_model_name']}` > "  # type: ignore[attr-defined]
                + "Method: `verify_password` => "
                + f"The model does not have a field `{field_name}`."
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
        if is_valid and ph.check_needs_rehash(hash):
            hash = ph.hash(password)
            await collection.update_one({"_id": doc_id}, {"$set": {field_name: hash}})
        #
        return is_valid

    async def update_password(
        self,
        old_password: str,
        new_password: str,
        field_name: str = "password",
    ) -> None:
        """For replace or recover password."""
        cls_model = self.__class__
        if not await self.verify_password(old_password, field_name):
            raise OldPassNotMatchError()
        # Get documet ID.
        doc_id = self._id.value  # type: ignore[attr-defined]
        # Get collection for current Model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls_model.META["collection_name"]]  # type: ignore[index, attr-defined]
        # Create hash of new passwor.
        ph = PasswordHasher()
        hash: str = ph.hash(new_password)
        await collection.update_one({"_id": doc_id}, {"$set": {field_name: hash}})
