"""General purpose query methods."""

from typing import Any

from pymongo.asynchronous.collection import AsyncCollection
from pymongo.asynchronous.command_cursor import AsyncCommandCursor

from .. import store
from ..tools import model_is_migrated


class GeneralMixin:
    """General purpose query methods."""

    @classmethod
    async def estimated_document_count(cls, comment=None, **kwargs) -> int:
        """Gets an estimate of the count of documents in a collection using collection metadata."""
        # Check if this model is migrated to database.
        model_is_migrated(cls)
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
        # Get document count.
        return await collection.estimated_document_count(comment=comment, **kwargs)

    @classmethod
    async def count_documents(cls, filter, session=None, comment=None, **kwargs) -> int:
        """Gets an estimate of the count of documents in a collection using collection metadata."""
        # Check if this model is migrated to database.
        model_is_migrated(cls)
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
        # Get document count.
        return await collection.count_documents(
            filter=filter, session=session, comment=comment, **kwargs
        )

    @classmethod
    async def aggregate(
        cls, pipeline, session=None, let=None, comment=None, **kwargs
    ) -> AsyncCommandCursor:
        """Runs an aggregation framework pipeline."""
        # Check if this model is migrated to database.
        model_is_migrated(cls)
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
        # Get document count.
        return await collection.aggregate(
            pipeline=pipeline, session=session, let=let, comment=comment, **kwargs
        )

    @classmethod
    async def distinct(
        cls, key, filter=None, session=None, comment=None, hint=None, **kwargs
    ) -> list[Any]:
        """Finds the distinct values for a specified field across a single collection.
        Returns an array of unique values for specified field of collection.
        """
        # Check if this model is migrated to database.
        model_is_migrated(cls)
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
        # Get document count.
        return await collection.distinct(
            key=key,
            filter=filter,
            session=session,
            comment=comment,
            hint=hint,
            **kwargs
        )

    @classmethod
    async def name(cls) -> str:
        """Get collection name."""
        # Check if this model is migrated to database.
        model_is_migrated(cls)
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
        # Get document count.
        return collection.name
