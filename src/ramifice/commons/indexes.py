"""Ramifice - Indexation documents of collection."""

__all__ = ("IndexMixin",)

from typing import Any

from pymongo.asynchronous.collection import AsyncCollection

from ramifice.utils import constants


class IndexMixin:
    """Ramifice - Indexation documents of collection."""

    @classmethod
    async def create_index(  # type: ignore[no-untyped-def]
        cls,
        keys: Any,
        session: Any | None = None,
        comment: Any | None = None,
        **kwargs,
    ) -> str:
        """Ramifice - Creates an index on this collection."""
        # Get collection for current model.
        collection: AsyncCollection = constants.MONGO_DATABASE[cls.META["collection_name"]]
        # Create index.
        result: str = await collection.create_index(
            keys=keys,
            session=session,
            comment=comment,
            **kwargs,
        )
        return result

    @classmethod
    async def drop_index(  # type: ignore[no-untyped-def]
        cls,
        index_or_name: Any,
        session: Any | None = None,
        comment: Any | None = None,
        **kwargs,
    ) -> None:
        """Ramifice - Drops the specified index on this collection."""
        # Get collection for current model.
        collection: AsyncCollection = constants.MONGO_DATABASE[cls.META["collection_name"]]
        # Delete index.
        await collection.drop_index(
            index_or_name=index_or_name,
            session=session,
            comment=comment,
            **kwargs,
        )

    @classmethod
    async def create_indexes(  # type: ignore[no-untyped-def]
        cls,
        indexes: Any,
        session: Any | None = None,
        comment: Any | None = None,
        **kwargs,
    ) -> list[str]:
        """Ramifice - Create one or more indexes on this collection."""
        # Get collection for current model.
        collection: AsyncCollection = constants.MONGO_DATABASE[cls.META["collection_name"]]
        # Create indexes.
        result: list[str] = await collection.create_indexes(
            indexes=indexes,
            session=session,
            comment=comment,
            **kwargs,
        )
        return result

    @classmethod
    async def drop_indexes(  # type: ignore[no-untyped-def]
        cls,
        session: Any | None = None,
        comment: Any | None = None,
        **kwargs,
    ) -> None:
        """Ramifice - Drops all indexes on this collection."""
        # Get collection for current model.
        collection: AsyncCollection = constants.MONGO_DATABASE[cls.META["collection_name"]]
        # Delete indexes.
        await collection.drop_indexes(session=session, comment=comment, **kwargs)

    @classmethod
    async def index_information(
        cls,
        session: Any | None = None,
        comment: Any | None = None,
    ) -> Any:
        """Ramifice - Get information on this collection’s indexes."""
        # Get collection for current model.
        collection: AsyncCollection = constants.MONGO_DATABASE[cls.META["collection_name"]]
        # Get information.
        result = await collection.index_information(session=session, comment=comment)
        return result

    @classmethod
    async def list_indexes(
        cls,
        session: Any | None = None,
        comment: Any | None = None,
    ) -> Any:
        """Ramifice - Get a cursor over the index documents for this collection."""
        # Get collection for current model.
        collection: AsyncCollection = constants.MONGO_DATABASE[cls.META["collection_name"]]
        # Get cursor.
        cursor = await collection.list_indexes(session=session, comment=comment)
        return cursor
