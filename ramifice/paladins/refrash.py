"""Update Model instance from database."""

from datetime import datetime
from typing import Any

from pymongo.asynchronous.collection import AsyncCollection

from .. import store
from ..errors import PanicError


class RefrashMixin:
    """Create or update document in database."""

    async def refrash_model(self) -> None:
        """Update Model instance from database."""
        # Get collection.
        collection: AsyncCollection = store.MONGO_DATABASE[self.__class__.META["collection_name"]]  # type: ignore[index, attr-defined]
        mongo_doc: dict[str, Any] | None = await collection.find_one(filter={"_id": self._id.value})  # type: ignore[index, attr-defined]
        if mongo_doc is None:
            msg = (
                f"Model: `{self.full_model_name()}` > "  # type: ignore[attr-defined]
                + "Method: `refrash_model` => "
                + f"A document with an identifier `{self._id.value}` is not exists in the database!"  # type: ignore[index, attr-defined]
            )
            raise PanicError(msg)
        self.refrash_from_doc(mongo_doc)  # type: ignore[index, attr-defined]
