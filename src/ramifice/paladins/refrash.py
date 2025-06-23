"""Update Model instance from database."""

from typing import Any

from pymongo.asynchronous.collection import AsyncCollection

from ..utils import globals
from ..utils.errors import PanicError
from .tools import refresh_from_mongo_doc


class RefrashMixin:
    """Update Model instance from database."""

    async def refrash_from_db(self) -> None:
        """Update Model instance from database."""
        cls_model = self.__class__
        # Get collection.
        collection: AsyncCollection = globals.MONGO_DATABASE[cls_model.META["collection_name"]]
        mongo_doc: dict[str, Any] | None = await collection.find_one(filter={"_id": self._id.value})
        if mongo_doc is None:
            msg = (
                f"Model: `{self.full_model_name()}` > "
                + "Method: `refrash_from_db` => "
                + f"A document with an identifier `{self._id.value}` is not exists in the database!"
            )
            raise PanicError(msg)
        self.inject()
        refresh_from_mongo_doc(self, mongo_doc)
