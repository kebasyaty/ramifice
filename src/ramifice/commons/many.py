"""Queries like `find many`."""

import json
from typing import Any

from pymongo.asynchronous.collection import AsyncCollection
from pymongo.asynchronous.cursor import AsyncCursor, CursorType
from pymongo.results import DeleteResult

from ..utils import store
from ..utils.errors import PanicError
from .tools import mongo_doc_to_raw_doc, password_to_none


class ManyMixin:
    """Queries like `find many`."""

    @classmethod
    async def find_many(
        cls,
        filter: Any | None = None,
        projection: Any | None = None,
        skip: int = 0,
        limit: int = 0,
        no_cursor_timeout: bool = False,
        cursor_type: int = CursorType.NON_TAILABLE,
        sort: Any | None = None,
        allow_partial_results: bool = False,
        oplog_replay: bool = False,
        batch_size: int = 0,
        collation: Any | None = None,
        hint: Any | None = None,
        max_scan: Any | None = None,
        max_time_ms: Any | None = None,
        max: Any | None = None,
        min: Any | None = None,
        return_key: bool = False,
        show_record_id: bool = False,
        comment: Any | None = None,
        session: Any | None = None,
        allow_disk_use: Any | None = None,
    ) -> list[dict[str, Any]]:
        """Find documents."""
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]
        # Get documents.
        doc_list: list[dict[str, Any]] = []
        cursor: AsyncCursor = collection.find(
            filter=filter,
            projection=projection,
            skip=skip,
            limit=limit or cls.META["db_query_docs_limit"],
            no_cursor_timeout=no_cursor_timeout,
            cursor_type=cursor_type,
            sort=sort,
            allow_partial_results=allow_partial_results,
            oplog_replay=oplog_replay,
            batch_size=batch_size,
            collation=collation,
            hint=hint,
            max_scan=max_scan,
            max_time_ms=max_time_ms,
            max=max,
            min=min,
            return_key=return_key,
            show_record_id=show_record_id,
            comment=comment,
            session=session,
            allow_disk_use=allow_disk_use,
        )
        field_name_and_type = cls.META["field_name_and_type"]
        async for mongo_doc in cursor:
            doc_list.append(password_to_none(field_name_and_type, mongo_doc))
        return doc_list

    @classmethod
    async def find_many_to_raw_docs(
        cls,
        filter: Any | None = None,
        projection: Any | None = None,
        skip: int = 0,
        limit: int = 0,
        no_cursor_timeout: bool = False,
        cursor_type: int = CursorType.NON_TAILABLE,
        sort: Any | None = None,
        allow_partial_results: bool = False,
        oplog_replay: bool = False,
        batch_size: int = 0,
        collation: Any | None = None,
        hint: Any | None = None,
        max_scan: Any | None = None,
        max_time_ms: Any | None = None,
        max: Any | None = None,
        min: Any | None = None,
        return_key: bool = False,
        show_record_id: bool = False,
        comment: Any | None = None,
        session: Any | None = None,
        allow_disk_use: Any | None = None,
    ) -> list[dict[str, Any]]:
        """Find documents and convert to a raw documents.

        Special changes:
            _id to str
            password to None
            date to str
            datetime to str
        """
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]
        # Get documents.
        doc_list: list[dict[str, Any]] = []
        cursor: AsyncCursor = collection.find(
            filter=filter,
            projection=projection,
            skip=skip,
            limit=limit or cls.META["db_query_docs_limit"],
            no_cursor_timeout=no_cursor_timeout,
            cursor_type=cursor_type,
            sort=sort,
            allow_partial_results=allow_partial_results,
            oplog_replay=oplog_replay,
            batch_size=batch_size,
            collation=collation,
            hint=hint,
            max_scan=max_scan,
            max_time_ms=max_time_ms,
            max=max,
            min=min,
            return_key=return_key,
            show_record_id=show_record_id,
            comment=comment,
            session=session,
            allow_disk_use=allow_disk_use,
        )
        field_name_and_type = cls.META["field_name_and_type"]
        async for mongo_doc in cursor:
            doc_list.append(mongo_doc_to_raw_doc(field_name_and_type, mongo_doc))
        return doc_list

    @classmethod
    async def find_many_to_json(
        cls,
        filter: Any | None = None,
        projection: Any | None = None,
        skip: int = 0,
        limit: int = 0,
        no_cursor_timeout: bool = False,
        cursor_type: int = CursorType.NON_TAILABLE,
        sort: Any | None = None,
        allow_partial_results: bool = False,
        oplog_replay: bool = False,
        batch_size: int = 0,
        collation: Any | None = None,
        hint: Any | None = None,
        max_scan: Any | None = None,
        max_time_ms: Any | None = None,
        max: Any | None = None,
        min: Any | None = None,
        return_key: bool = False,
        show_record_id: bool = False,
        comment: Any | None = None,
        session: Any | None = None,
        allow_disk_use: Any | None = None,
    ) -> str | None:
        """Find documents and convert to a json string."""
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]
        # Get documents.
        doc_list: list[dict[str, Any]] = []
        cursor: AsyncCursor = collection.find(
            filter=filter,
            projection=projection,
            skip=skip,
            limit=limit or cls.META["db_query_docs_limit"],
            no_cursor_timeout=no_cursor_timeout,
            cursor_type=cursor_type,
            sort=sort,
            allow_partial_results=allow_partial_results,
            oplog_replay=oplog_replay,
            batch_size=batch_size,
            collation=collation,
            hint=hint,
            max_scan=max_scan,
            max_time_ms=max_time_ms,
            max=max,
            min=min,
            return_key=return_key,
            show_record_id=show_record_id,
            comment=comment,
            session=session,
            allow_disk_use=allow_disk_use,
        )
        field_name_and_type = cls.META["field_name_and_type"]
        async for mongo_doc in cursor:
            doc_list.append(mongo_doc_to_raw_doc(field_name_and_type, mongo_doc))
        return json.dumps(doc_list) if len(doc_list) > 0 else None

    @classmethod
    async def delete_many(
        cls,
        filter: Any,
        collation: Any | None = None,
        hint: Any | None = None,
        session: Any | None = None,
        let: Any | None = None,
        comment: Any | None = None,
    ) -> DeleteResult:
        """Find documents matching with Model."""
        # Raises a panic if the Model cannot be removed.
        if not cls.META["is_delete_doc"]:
            msg = (
                f"Model: `{cls.META['full_model_name']}` > "
                + "META param: `is_delete_doc` (False) => "
                + "Documents of this Model cannot be removed from the database!"
            )
            raise PanicError(msg)
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]
        # Delete documents.
        result: DeleteResult = await collection.delete_many(
            filter=filter,
            collation=collation,
            hint=hint,
            session=session,
            let=let,
            comment=comment,
        )
        return result
