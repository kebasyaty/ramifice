"""General purpose query methods."""

from __future__ import annotations

__all__ = ("GeneralMixin",)

from typing import Any

from pymongo.asynchronous.collection import AsyncCollection
from pymongo.asynchronous.command_cursor import AsyncCommandCursor
from pymongo.asynchronous.database import AsyncDatabase

from ramifice.commons.tools import correct_mongo_filter
from ramifice.utils import constants, translations


class GeneralMixin:
    """General purpose query methods."""

    @classmethod
    def from_mongo_doc(
        cls,
        mongo_doc: dict[str, Any],
    ) -> Any:
        """Create object instance from Mongo document."""
        obj: Any = cls()
        lang: str = translations.CURRENT_LOCALE
        for name, data in mongo_doc.items():
            field = obj.__dict__.get(name)
            if field is None:
                continue
            if field.field_type == "TextField":
                field.value = data.get(lang, "- -") if data is not None else None
            elif field.group == "pass":
                field.value = None
            else:
                field.value = data
        return obj

    @classmethod
    async def estimated_document_count(  # type: ignore[no-untyped-def]
        cls,
        comment: Any | None = None,
        **kwargs,
    ) -> int:
        """Get an estimate of the number of documents in this collection using collection metadata."""
        # Get collection for current model.
        collection: AsyncCollection = constants.MONGO_DATABASE[cls.META["collection_name"]]
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
        """Count the number of documents in this collection."""
        # Get collection for current model.
        collection: AsyncCollection = constants.MONGO_DATABASE[cls.META["collection_name"]]
        # Correcting filter.
        if filter is not None:
            filter = correct_mongo_filter(cls, filter)

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
        """Perform an aggregation using the aggregation framework on this collection."""
        # Get collection for current model.
        collection: AsyncCollection = constants.MONGO_DATABASE[cls.META["collection_name"]]
        # Correcting filter.
        if pipeline is not None:
            pipeline = correct_mongo_filter(cls, pipeline)

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
        """Get a list of distinct values for key among all documents in this collection.

        Returns an array of unique values for specified field of collection.
        """
        # Get collection for current model.
        collection: AsyncCollection = constants.MONGO_DATABASE[cls.META["collection_name"]]
        # Correcting filter.
        if filter is not None:
            filter = correct_mongo_filter(cls, filter)

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
        """The name of this AsyncCollection."""
        # Get collection for current model.
        collection: AsyncCollection = constants.MONGO_DATABASE[cls.META["collection_name"]]
        #
        return collection.name

    @classmethod
    def collection_full_name(cls) -> str:
        """The full name of this AsyncCollection.

        The full name is of the form database_name.collection_name.
        """
        # Get collection for current model.
        collection: AsyncCollection = constants.MONGO_DATABASE[cls.META["collection_name"]]
        #
        return collection.full_name

    @classmethod
    def database(cls) -> AsyncDatabase:
        """Get AsyncBatabase for the current Model."""
        # Get collection for current model.
        collection: AsyncCollection = constants.MONGO_DATABASE[cls.META["collection_name"]]
        #
        return collection.database

    @classmethod
    def collection(cls) -> AsyncCollection:
        """Get AsyncCollection for the current Model."""
        # Get collection for current model.
        collection: AsyncCollection = constants.MONGO_DATABASE[cls.META["collection_name"]]
        #
        return collection
