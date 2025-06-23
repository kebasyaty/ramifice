"""General purpose query methods."""

from typing import Any

from pymongo.asynchronous.collection import AsyncCollection
from pymongo.asynchronous.command_cursor import AsyncCommandCursor
from pymongo.asynchronous.database import AsyncDatabase

from ..utils import store


class GeneralMixin:
    """General purpose query methods."""

    @classmethod
    async def estimated_document_count(  # type: ignore[no-untyped-def]
        cls,
        comment: Any | None = None,
        **kwargs,
    ) -> int:
        """Gets an estimate of the count of documents in a collection using collection metadata."""
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]
        #
        return await collection.estimated_document_count(
            comment=comment,
            **kwargs,
        )

    @classmethod
    async def count_documents(  # type: ignore[no-untyped-def]
        cls,
        filter: Any,
        session: Any | None = None,
        comment: Any | None = None,
        **kwargs,
    ) -> int:
        """Gets an estimate of the count of documents in a collection using collection metadata."""
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]
        #
        return await collection.count_documents(
            filter=filter,
            session=session,
            comment=comment,
            **kwargs,
        )

    @classmethod
    async def aggregate(  # type: ignore[no-untyped-def]
        cls,
        pipeline: Any,
        session: Any | None = None,
        let: Any | None = None,
        comment: Any | None = None,
        **kwargs,
    ) -> AsyncCommandCursor:
        """Runs an aggregation framework pipeline."""
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]
        #
        return await collection.aggregate(
            pipeline=pipeline,
            session=session,
            let=let,
            comment=comment,
            **kwargs,
        )

    @classmethod
    async def distinct(  # type: ignore[no-untyped-def]
        cls,
        key: Any,
        filter: Any | None = None,
        session: Any | None = None,
        comment: Any | None = None,
        hint: Any | None = None,
        **kwargs,
    ) -> list[Any]:
        """Finds the distinct values for a specified field across a single collection.

        Returns an array of unique values for specified field of collection.
        """
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]
        #
        return await collection.distinct(
            key=key,
            filter=filter,
            session=session,
            comment=comment,
            hint=hint,
            **kwargs,
        )

    @classmethod
    def collection_name(cls) -> str:
        """Get collection name."""
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]
        #
        return collection.name

    @classmethod
    def collection_full_name(cls) -> str:
        """The full name of this AsyncCollection.

        The full name is of the form database_name.collection_name.
        """
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]
        #
        return collection.full_name

    @classmethod
    def database(cls) -> AsyncDatabase:
        """Get AsyncBatabase for the current Model."""
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]
        #
        return collection.database

    @classmethod
    def collection(cls) -> AsyncCollection:
        """Get AsyncCollection for the current Model."""
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]
        #
        return collection
