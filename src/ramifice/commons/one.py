"""Requests like `find one`."""

from __future__ import annotations

__all__ = ("OneMixin",)

import logging
from typing import Any

from pymongo.asynchronous.collection import AsyncCollection
from pymongo.results import DeleteResult

from ramifice.commons.tools import (
    correct_mongo_filter,
    mongo_doc_to_raw_doc,
    password_to_none,
)
from ramifice.utils import constants, translations
from ramifice.utils.errors import ForbiddenDeleteDocError

logger = logging.getLogger(__name__)


class OneMixin:
    """Requests like `find one`."""

    @classmethod
    async def find_one(
        cls: Any,
        filter: Any | None = None,
        *args: tuple,
        **kwargs: dict[str, Any],
    ) -> dict[str, Any] | None:
        """Get a single document from the database."""
        # Get collection for current model.
        collection: AsyncCollection = constants.MONGO_DATABASE[cls.META["collection_name"]]
        # Correcting filter.
        if filter is not None:
            filter = correct_mongo_filter(cls, filter)
        # Get document.
        mongo_doc = await collection.find_one(filter, *args, **kwargs)
        if mongo_doc is not None:
            mongo_doc = password_to_none(
                cls.META["field_name_and_type"],
                mongo_doc,
            )
        return mongo_doc

    @classmethod
    async def find_one_to_raw_doc(
        cls: Any,
        filter: Any | None = None,
        *args: tuple,
        **kwargs: dict[str, Any],
    ) -> dict[str, Any] | None:
        """Find a single document and converting to raw document."""
        # Get collection for current model.
        collection: AsyncCollection = constants.MONGO_DATABASE[cls.META["collection_name"]]
        # Correcting filter.
        if filter is not None:
            filter = correct_mongo_filter(cls, filter)
        # Get document.
        raw_doc = None
        mongo_doc = await collection.find_one(filter, *args, **kwargs)
        inst_model_dict = {key: val for key, val in cls().__dict__.items() if not callable(val) and not val.ignored}
        if mongo_doc is not None:
            raw_doc = mongo_doc_to_raw_doc(
                inst_model_dict,
                mongo_doc,
                translations.CURRENT_LOCALE,
            )
        return raw_doc

    @classmethod
    async def find_one_to_instance(
        cls: Any,
        filter: Any | None = None,
        *args: tuple,
        **kwargs: dict[str, Any],
    ) -> Any | None:
        """Find a single document and convert it to a Model instance."""
        # Get collection for current model.
        collection: AsyncCollection = constants.MONGO_DATABASE[cls.META["collection_name"]]
        # Correcting filter.
        if filter is not None:
            filter = correct_mongo_filter(cls, filter)
        # Get document.
        inst_model = None
        mongo_doc = await collection.find_one(filter, *args, **kwargs)
        if mongo_doc is not None:
            # Convert document to Model instance.
            inst_model = cls.from_mongo_doc(mongo_doc)
        return inst_model

    @classmethod
    async def find_one_to_json(
        cls: Any,
        filter: Any | None = None,
        *args: tuple,
        **kwargs: dict[str, Any],
    ) -> str | None:
        """Find a single document and convert it to a JSON string."""
        # Get collection for current model.
        collection: AsyncCollection = constants.MONGO_DATABASE[cls.META["collection_name"]]
        # Correcting filter.
        if filter is not None:
            filter = correct_mongo_filter(cls, filter)
        # Get document.
        json_str: str | None = None
        mongo_doc = await collection.find_one(filter, *args, **kwargs)
        if mongo_doc is not None:
            # Convert document to Model instance.
            inst_model = cls.from_mongo_doc(mongo_doc)
            json_str = inst_model.to_json()
        return json_str

    @classmethod
    async def delete_one(
        cls: Any,
        filter: Any,
        collation: Any | None = None,
        hint: Any | None = None,
        session: Any | None = None,
        let: Any | None = None,
        comment: Any | None = None,
    ) -> DeleteResult:
        """Delete a single document matching the filter."""
        # Raises a panic if the Model cannot be removed.
        if not cls.META["is_delete_doc"]:
            msg = (
                f"Model: `{cls.META['full_model_name']}` > "
                + "META param: `is_delete_doc` (False) => "
                + "Documents of this Model cannot be removed from the database!"
            )
            logger.error(msg)
            raise ForbiddenDeleteDocError(msg)
        # Get collection for current model.
        collection: AsyncCollection = constants.MONGO_DATABASE[cls.META["collection_name"]]
        # Correcting filter.
        if filter is not None:
            filter = correct_mongo_filter(cls, filter)
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
    async def find_one_and_delete(
        cls: Any,
        filter: Any,
        projection: Any | None = None,
        sort: Any | None = None,
        hint: Any | None = None,
        session: Any | None = None,
        let: Any | None = None,
        comment: Any | None = None,
        **kwargs: dict[str, Any],
    ) -> dict[str, Any] | None:
        """Finds a single document and deletes it, returning the document."""
        # Raises a panic if the Model cannot be removed.
        if not cls.META["is_delete_doc"]:
            msg = (
                f"Model: `{cls.META['full_model_name']}` > "
                + "META param: `is_delete_doc` (False) => "
                + "Documents of this Model cannot be removed from the database!"
            )
            logger.error(msg)
            raise ForbiddenDeleteDocError(msg)
        # Get collection for current model.
        collection: AsyncCollection = constants.MONGO_DATABASE[cls.META["collection_name"]]
        # Correcting filter.
        if filter is not None:
            filter = correct_mongo_filter(cls, filter)
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
            mongo_doc = password_to_none(
                cls.META["field_name_and_type"],
                mongo_doc,
            )
        return mongo_doc
