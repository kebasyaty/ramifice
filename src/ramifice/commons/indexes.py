"""Indexation documents of collection."""

from typing import Any

from pymongo.asynchronous.collection import AsyncCollection

from .. import store


class IndexMixin:
	"""Indexation documents of collection."""

	@classmethod
	async def create_index(cls, keys, session=None, comment=None, **kwargs) -> str:
		"""Creates an index on this collection."""
		# Get collection for current model.
		collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
		# Create index.
		result: str = await collection.create_index(
			keys=keys,
			session=session,
			comment=comment,
			**kwargs,
		)
		return result

	@classmethod
	async def drop_index(cls, index_or_name, session=None, comment=None, **kwargs) -> None:
		"""Drops the specified index on this collection."""
		# Get collection for current model.
		collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
		# Delete index.
		await collection.drop_index(
			index_or_name=index_or_name,
			session=session,
			comment=comment,
			**kwargs,
		)

	@classmethod
	async def create_indexes(cls, indexes, session=None, comment=None, **kwargs) -> list[str]:
		"""Create one or more indexes on this collection."""
		# Get collection for current model.
		collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
		# Create indexes.
		result: list[str] = await collection.create_indexes(
			indexes=indexes,
			session=session,
			comment=comment,
			**kwargs,
		)
		return result

	@classmethod
	async def drop_indexes(cls, session=None, comment=None, **kwargs) -> None:
		"""Drops all indexes on this collection."""
		# Get collection for current model.
		collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
		# Delete indexes.
		await collection.drop_indexes(session=session, comment=comment, **kwargs)

	@classmethod
	async def index_information(cls, session=None, comment=None) -> Any:
		"""Get information on this collection’s indexes."""
		# Get collection for current model.
		collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
		# Get information.
		result = await collection.index_information(session=session, comment=comment)
		return result

	@classmethod
	async def list_indexes(cls, session=None, comment=None) -> Any:
		"""Get a cursor over the index documents for this collection."""
		# Get collection for current model.
		collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
		# Get cursor.
		cursor = await collection.list_indexes(session=session, comment=comment)
		return cursor
