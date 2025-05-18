"""Queries like `find many`."""

from typing import Any

from pymongo.asynchronous.collection import AsyncCollection
from pymongo.asynchronous.cursor import AsyncCursor, CursorType

from .. import store
from ..tools import model_is_migrated


class ManyMixin:
    """Queries like `find many`."""

    async def find_many(
        cls,
        filter=None,
        projection=None,
        skip=0,
        limit=0,
        no_cursor_timeout=False,
        cursor_type=CursorType.NON_TAILABLE,
        sort=None,
        allow_partial_results=False,
        oplog_replay=False,
        batch_size=0,
        collation=None,
        hint=None,
        max_scan=None,
        max_time_ms=None,
        max=None,
        min=None,
        return_key=False,
        show_record_id=False,
        snapshot=False,
        comment=None,
        session=None,
        allow_disk_use=None,
    ) -> list[dict[str, Any]]:
        """Find documents matching with Model."""
        # Check if this model is migrated to database.
        model_is_migrated(cls)
        # Get collection for current model.
        collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
        # Get documents.
        doc_list: list[dict[str, Any]] = []
        cursor: AsyncCursor = collection.find(
            filter=filter,
            projection=projection,
            skip=skip,
            limit=limit or cls.META["db_query_docs_limit"],  # type: ignore[index, attr-defined]
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
            snapshot=snapshot,
            comment=comment,
            session=session,
            allow_disk_use=allow_disk_use,
        )
        async for mongo_doc in cursor:
            doc_list.append(cls.mongo_doc_to_model_doc(mongo_doc))  # type: ignore[index, attr-defined]

        return doc_list
