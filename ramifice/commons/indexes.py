"""Indexation documents of collection."""

from typing import Any

from pymongo.asynchronous.collection import AsyncCollection

from .. import store
from ..tools import model_is_migrated


class IndexMixin:
    """Indexation documents of collection."""

    @classmethod
    async def create_index(cls, keys, session=None, comment=None, **kwargs) -> str:
        """This is a convenience method for creating a single index."""
        # Check if this model is migrated to database.
        model_is_migrated(cls)
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
        # Create index.
        result = await collection.create_index(
            keys=keys, session=session, comment=comment, **kwargs
        )
        return result

    @classmethod
    async def index_information(cls, session=None, comment=None) -> Any:
        """Get information on this collection’s indexes."""
        # Check if this model is migrated to database.
        model_is_migrated(cls)
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
        # Get information.
        result = await collection.index_information(session=session, comment=comment)
        return result

    @classmethod
    async def list_indexes(cls, session=None, comment=None) -> Any:
        """Get a cursor over the index documents for this collection."""
        # Check if this model is migrated to database.
        model_is_migrated(cls)
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
        # Get cursor.
        cursor = await collection.list_indexes(session=session, comment=comment)
        return cursor
