"""Requests like `find one`."""

from typing import Any

from pymongo.asynchronous.collection import AsyncCollection
from pymongo.results import DeleteResult

from .. import store
from ..errors import PanicError


class OneMixin:
    """Requests like `find one`."""

    @classmethod
    async def find_one(
        cls,
        filter: Any | None = None,
        *args,
        **kwargs,
    ) -> dict[str, Any] | None:
        """Find a single document."""
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
        # Get document.
        mongo_doc = await collection.find_one(filter, *args, **kwargs)
        if mongo_doc is not None:
            mongo_doc = cls.password_to_none(mongo_doc)  # type: ignore[attr-defined]
        return mongo_doc

    @classmethod
    async def find_one_to_raw_doc(
        cls,
        filter: Any | None = None,
        *args,
        **kwargs,
    ) -> dict[str, Any] | None:
        """Find a single document."""
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
        # Get document.
        raw_doc = None
        mongo_doc = await collection.find_one(filter, *args, **kwargs)
        if mongo_doc is not None:
            raw_doc = cls.mongo_doc_to_raw_doc(mongo_doc)  # type: ignore[attr-defined]
        return raw_doc

    @classmethod
    async def find_one_to_instance(
        cls,
        filter: Any | None = None,
        *args,
        **kwargs,
    ) -> Any | None:
        """Find a single document and convert it to a Model instance."""
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
        # Get document.
        inst_model = None
        mongo_doc = await collection.find_one(filter, *args, **kwargs)
        if mongo_doc is not None:
            # Convert document to Model instance.
            inst_model = cls.from_mongo_doc(mongo_doc)  # type: ignore[attr-defined]
        return inst_model

    @classmethod
    async def find_one_to_json(
        cls,
        filter: Any | None = None,
        *args,
        **kwargs,
    ) -> str | None:
        """Find a single document and convert it to a JSON string."""
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
        # Get document.
        json_str: str | None = None
        mongo_doc = await collection.find_one(filter, *args, **kwargs)
        if mongo_doc is not None:
            # Convert document to Model instance.
            inst_model = cls.from_mongo_doc(mongo_doc)  # type: ignore[attr-defined]
            json_str = inst_model.to_json()
        return json_str

    @classmethod
    async def delete_one(
        cls,
        filter: Any,
        collation: Any | None = None,
        hint: Any | None = None,
        session: Any | None = None,
        let: Any | None = None,
        comment: Any | None = None,
    ) -> DeleteResult:
        """Find a single document and delete it."""
        # Raises a panic if the Model cannot be removed.
        if not cls.META["is_delete_doc"]:  # type: ignore[attr-defined]
            msg = (
                f"Model: `{cls.META['full_model_name']}` > "  # type: ignore[attr-defined]
                + "META param: `is_delete_doc` (False) => "
                + "Documents of this Model cannot be removed from the database!"
            )
            raise PanicError(msg)
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
        # Get document.
        result: DeleteResult = await collection.delete_one(
            filter=filter,
            collation=collation,
            hint=hint,
            session=session,
            let=let,
            comment=comment,
        )
        return result

    @classmethod
    async def find_one_and_delete(  # type: ignore[no-untyped-def]
        cls,
        filter: Any,
        projection: Any | None = None,
        sort: Any | None = None,
        hint: Any | None = None,
        session: Any | None = None,
        let: Any | None = None,
        comment: Any | None = None,
        **kwargs,
    ) -> dict[str, Any] | None:
        """Find a single document and delete it, return original."""
        # Raises a panic if the Model cannot be removed.
        if not cls.META["is_delete_doc"]:  # type: ignore[attr-defined]
            msg = (
                f"Model: `{cls.META['full_model_name']}` > "  # type: ignore[attr-defined]
                + "META param: `is_delete_doc` (False) => "
                + "Documents of this Model cannot be removed from the database!"
            )
            raise PanicError(msg)
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
        # Get document.
        mongo_doc: dict[str, Any] | None = await collection.find_one_and_delete(
            filter=filter,
            projection=projection,
            sort=sort,
            hint=hint,
            session=session,
            let=let,
            comment=comment,
            **kwargs,
        )
        if mongo_doc is not None:
            mongo_doc = cls.password_to_none(mongo_doc)  # type: ignore[attr-defined]
        return mongo_doc
