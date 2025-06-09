"""Update Model instance from database."""

from typing import Any

from pymongo.asynchronous.collection import AsyncCollection

from .. import store
from ..errors import PanicError


class RefrashMixin:
	"""Update Model instance from database."""

	async def refrash_from_db(self) -> None:
		"""Update Model instance from database."""
		cls_model = self.__class__
		# Get collection.
		collection: AsyncCollection = store.MONGO_DATABASE[cls_model.META["collection_name"]]  # type: ignore[index, attr-defined]
		mongo_doc: dict[str, Any] | None = await collection.find_one(filter={"_id": self._id.value})  # type: ignore[attr-defined]
		if mongo_doc is None:
			msg = (
				f"Model: `{self.full_model_name()}` > "  # type: ignore[attr-defined]
				+ "Method: `refrash_from_db` => "
				+ f"A document with an identifier `{self._id.value}` is not exists in the database!"  # type: ignore[attr-defined]
			)
			raise PanicError(msg)
		self.inject()  # type: ignore[attr-defined]
		self.refrash_from_mongo_doc(mongo_doc)  # type: ignore[attr-defined]
