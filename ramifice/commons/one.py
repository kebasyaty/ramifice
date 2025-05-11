"""Requests like `find one`."""

from typing import Any

from pymongo.asynchronous.collection import AsyncCollection
from pymongo.results import DeleteResult

from .. import store
from ..tools import model_is_migrated


class OneMixin:
    """Requests like `find one`."""

    @classmethod
    async def find_one_as_doc(
        cls, filter=None, *args, **kwargs
    ) -> dict[str, Any] | None:
        """Find document."""
        # Check if this model is migrated to database.
        model_is_migrated(cls)
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
        # Get document.
        mongo_doc = await collection.find_one(filter, *args, **kwargs)
        if mongo_doc is not None:
            # Convert document to Model instance.
            inst_model = cls.from_doc(mongo_doc)  # type: ignore[index, attr-defined]
            mongo_doc = inst_model.to_dict()
        return mongo_doc

    @classmethod
    async def find_one_to_instance(cls, filter=None, *args, **kwargs) -> Any | None:
        """Find document and convert it to a Model instance."""
        # Check if this model is migrated to database.
        model_is_migrated(cls)
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
        # Get document.
        inst_model = None
        mongo_doc = await collection.find_one(filter, *args, **kwargs)
        if mongo_doc is not None:
            # Convert document to Model instance.
            inst_model = cls.from_doc(mongo_doc)  # type: ignore[index, attr-defined]
        return inst_model

    @classmethod
    async def find_one_to_json(cls, filter=None, *args, **kwargs) -> str | None:
        """Find document and convert it to a json string."""
        # Check if this model is migrated to database.
        model_is_migrated(cls)
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
        # Get document.
        json_str: str | None = None
        mongo_doc = await collection.find_one(filter, *args, **kwargs)
        if mongo_doc is not None:
            # Convert document to Model instance.
            inst_model = cls.from_doc(mongo_doc)  # type: ignore[index, attr-defined]
            json_str = inst_model.to_json()
        return json_str

    @classmethod
    async def delete_one(
        cls, filter, collation=None, hint=None, session=None, let=None, comment=None
    ) -> DeleteResult:
        """Delete one document."""
        # Check if this model is migrated to database.
        model_is_migrated(cls)
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
        # Get document.
        result: DeleteResult = await collection.delete_one(
            filter=filter,
            collation=collation,
            hint=hint,
            session=session,
            let=let,
            comment=comment,
        )
        return result
