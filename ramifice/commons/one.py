"""Requests like `find one`."""

from typing import Any

from pymongo.asynchronous.collection import AsyncCollection

from .. import store
from ..tools import model_is_migrated


class OneMixin:
    """Requests like `find one`."""

    @classmethod
    async def find_one_to_instance(
        cls, filter=None, *args, **kwargs
    ) -> dict[str, Any] | None:
        """Finds the document and converts it to a Model instance."""
        # Check if this model is migrated to database.
        model_is_migrated(cls)
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
        # Get document.
        mongo_doc = await collection.find_one(filter, *args, **kwargs)
        inst_model = None
        if mongo_doc is not None:
            inst_model = cls.from_doc(mongo_doc)  # type: ignore[index, attr-defined]
        return inst_model
