"""General purpose query methods."""

from typing import Any

from pymongo.asynchronous.collection import AsyncCollection
from pymongo.asynchronous.command_cursor import AsyncCommandCursor
from pymongo.asynchronous.database import AsyncDatabase
from pymongo.results import BulkWriteResult

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
        #
        return await collection.estimated_document_count(comment=comment, **kwargs)

    @classmethod
    async def count_documents(cls, filter, session=None, comment=None, **kwargs) -> int:
        """Gets an estimate of the count of documents in a collection using collection metadata."""
        # Check if this model is migrated to database.
        model_is_migrated(cls)
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
        #
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
        #
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
        #
        return await collection.distinct(
            key=key,
            filter=filter,
            session=session,
            comment=comment,
            hint=hint,
            **kwargs
        )

    @classmethod
    def collection_name(cls) -> str:
        """Get collection name."""
        # Check if this model is migrated to database.
        model_is_migrated(cls)
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
        #
        return collection.name

    @classmethod
    def collection_full_name(cls) -> str:
        """The full name of this AsyncCollection.
        The full name is of the form database_name.collection_name.
        """
        # Check if this model is migrated to database.
        model_is_migrated(cls)
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
        #
        return collection.full_name

    @classmethod
    def database(cls) -> AsyncDatabase:
        """Get AsyncBatabase for the current Model."""
        # Check if this model is migrated to database.
        model_is_migrated(cls)
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
        #
        return collection.database

    @classmethod
    def collection(cls) -> AsyncCollection:
        """Get AsyncCollection for the current Model."""
        # Check if this model is migrated to database.
        model_is_migrated(cls)
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
        #
        return collection

    @classmethod
    async def bulk_write(
        cls,
        requests,
        ordered=True,
        bypass_document_validation=None,
        session=None,
        comment=None,
        let=None,
    ) -> BulkWriteResult:
        """Executes multiple write operations.
        An error will be raised if the requests parameter is empty.
        """
        # Check if this model is migrated to database.
        model_is_migrated(cls)
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
        #
        return await collection.bulk_write(
            requests=requests,
            ordered=ordered,
            bypass_document_validation=bypass_document_validation,
            session=session,
            comment=comment,
            let=let,
        )
