"""General purpose query methods."""

from pymongo.asynchronous.collection import AsyncCollection
from pymongo.asynchronous.command_cursor import AsyncCommandCursor

from .. import store
from ..errors import PanicError


class GeneralMixin:
    """General purpose query methods."""

    @classmethod
    async def estimated_document_count(cls, comment=None, **kwargs) -> int:
        """Gets an estimate of the count of documents in a collection using collection metadata."""
        if not cls.META["is_migrat_model"]:  # type: ignore[attr-defined]
            msg = (
                f"Model: `{cls.META["full_model_name"]}` > "  # type: ignore[attr-defined]
                + "Param: `is_migrat_model` (False) => "
                + "This Model is not migrated to database!"
            )
            raise PanicError(msg)
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
        # Get document count.
        return await collection.estimated_document_count(comment=comment, **kwargs)

    @classmethod
    async def count_documents(cls, filter, session=None, comment=None, **kwargs) -> int:
        """Gets an estimate of the count of documents in a collection using collection metadata."""
        if not cls.META["is_migrat_model"]:  # type: ignore[attr-defined]
            msg = (
                f"Model: `{cls.META["full_model_name"]}` > "  # type: ignore[attr-defined]
                + "Param: `is_migrat_model` (False) => "
                + "This Model is not migrated to database!"
            )
            raise PanicError(msg)
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
        if not cls.META["is_migrat_model"]:  # type: ignore[attr-defined]
            msg = (
                f"Model: `{cls.META["full_model_name"]}` > "  # type: ignore[attr-defined]
                + "Param: `is_migrat_model` (False) => "
                + "This Model is not migrated to database!"
            )
            raise PanicError(msg)
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
        # Get document count.
        return await collection.aggregate(
            pipeline=pipeline, session=session, let=let, comment=comment, **kwargs
        )
