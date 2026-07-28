"""Properties for the Model metaclass."""

from __future__ import annotations

from typing import Any

from pymongo.asynchronous.collection import AsyncCollection
from pymongo.asynchronous.database import AsyncDatabase

from ramifice.config import Config


class MetaProperties(type):
    """Properties for the Model metaclass."""

    @property
    def META(cls) -> dict[str, Any]:
        """Model metadata."""
        return cls._META

    @property
    def collection_name(cls) -> str:
        """The name of the model instance in the database."""
        metadata = cls.META
        # Get collection for current model.
        collection: AsyncCollection = Config.MONGO_DATABASE[metadata["collection_name"]]
        return collection.name

    @property
    def collection_full_name(cls) -> str:
        """The full name of the model instance in the database.

        The full name is of the form `database_name.collection_name`.
        """
        metadata = cls.META
        # Get collection for current model.
        collection: AsyncCollection = Config.MONGO_DATABASE[metadata["collection_name"]]
        return collection.full_name

    @property
    def database(cls) -> AsyncDatabase:
        """AsyncBatabase for a model instance."""
        metadata = cls.META
        # Get collection for current model.
        collection: AsyncCollection = Config.MONGO_DATABASE[metadata["collection_name"]]
        return collection.database

    @property
    def collection(cls) -> AsyncCollection:
        """AsyncCollection for a model instance."""
        metadata = cls.META
        # Get collection for current model.
        collection: AsyncCollection = Config.MONGO_DATABASE[metadata["collection_name"]]
        return collection
