# Ramifice - ORM-pseudo-like API MongoDB for Python language.
# Copyright (c) 2024 Gennady Kostyunin
# SPDX-License-Identifier: MIT
#
# Copyright 2024-present MongoDB, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""General purpose query methods."""

from __future__ import annotations

__all__ = ("GeneralMixin",)

from copy import deepcopy
from typing import Any

from pymongo.asynchronous.collection import AsyncCollection
from pymongo.asynchronous.command_cursor import AsyncCommandCursor
from pymongo.asynchronous.database import AsyncDatabase

from ramifice.commons.utils import correct_mongo_filter
from ramifice.config import Config
from ramifice.translator import Translator


class GeneralMixin:
    """General purpose query methods."""

    @classmethod
    def from_mongo_doc(
        cls,
        mongo_doc: dict[str, Any],
        lang_code: str = deepcopy(Translator.DEFAULT_LOCALE),
    ) -> Any:
        """Create a Model instance from a Mongo document."""
        descriptor_fields = cls.META["all_descriptor_fields"]
        # pyrefly: ignore [bad-argument-count]
        instance: Any = cls(lang_code)

        for f_name in descriptor_fields:
            value = mongo_doc.get(f_name) if f_name != "id" else "_id"

            if value is None:
                continue

            f__html_attrs = getattr(instance, f"{f_name}__html_attrs")
            field_type = f__html_attrs["field_type"]

            if field_type == "TextField":
                field_type["value"] = value.get(lang_code, "- -") if isinstance(value, dict) else value
            elif field_type == "PasswordField":
                field_type["value"] = None
            else:
                field_type["value"] = value

            setattr(instance, f_name, field_type["value"])

        return instance

    @classmethod
    async def estimated_document_count(  # type: ignore[no-untyped-def]
        cls,
        comment: Any | None = None,
        **kwargs,
    ) -> int:
        """Get an estimate of the number of documents in this collection using collection metadata."""
        # Get collection for current model.
        collection: AsyncCollection = Config.MONGO_DATABASE[cls.META["collection_name"]]
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
        lang_code: str = deepcopy(Translator.DEFAULT_LOCALE),
        **kwargs,
    ) -> int:
        """Count the number of documents in this collection."""
        # Get collection for current model.
        collection: AsyncCollection = Config.MONGO_DATABASE[cls.META["collection_name"]]
        # Correcting filter.
        if filter is not None:
            filter = correct_mongo_filter(cls, filter, lang_code)

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
        lang_code: str = deepcopy(Translator.DEFAULT_LOCALE),
        **kwargs,
    ) -> AsyncCommandCursor:
        """Perform an aggregation using the aggregation framework on this collection."""
        # Get collection for current model.
        collection: AsyncCollection = Config.MONGO_DATABASE[cls.META["collection_name"]]
        # Correcting filter.
        if pipeline is not None:
            pipeline = correct_mongo_filter(cls, pipeline, lang_code)

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
        lang_code: str = deepcopy(Translator.DEFAULT_LOCALE),
        **kwargs,
    ) -> list[Any]:
        """Get a list of distinct values for key among all documents in this collection.

        Returns an array of unique values for specified field of collection.
        """
        # Get collection for current model.
        collection: AsyncCollection = Config.MONGO_DATABASE[cls.META["collection_name"]]
        # Correcting filter.
        if filter is not None:
            filter = correct_mongo_filter(cls, filter, lang_code)

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
        collection: AsyncCollection = Config.MONGO_DATABASE[cls.META["collection_name"]]
        #
        return collection.name

    @classmethod
    def collection_full_name(cls) -> str:
        """The full name of this AsyncCollection.

        The full name is of the form database_name.collection_name.
        """
        # Get collection for current model.
        collection: AsyncCollection = Config.MONGO_DATABASE[cls.META["collection_name"]]
        #
        return collection.full_name

    @classmethod
    def database(cls) -> AsyncDatabase:
        """Get AsyncBatabase for the current Model."""
        # Get collection for current model.
        collection: AsyncCollection = Config.MONGO_DATABASE[cls.META["collection_name"]]
        #
        return collection.database

    @classmethod
    def collection(cls) -> AsyncCollection:
        """Get AsyncCollection for the current Model."""
        # Get collection for current model.
        collection: AsyncCollection = Config.MONGO_DATABASE[cls.META["collection_name"]]
        #
        return collection
