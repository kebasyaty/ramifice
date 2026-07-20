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
"""Requests like `find one`."""

from __future__ import annotations

__all__ = ("OneMixin",)

import logging
from copy import deepcopy
from typing import Any

from pymongo.asynchronous.collection import AsyncCollection
from pymongo.results import DeleteResult

from ramifice.commons.utils import (
    correct_mongo_filter,
    mongo_doc_to_model_dict,
    password_to_none,
)
from ramifice.config import Config
from ramifice.errors import ForbiddenDeleteDocError
from ramifice.translator import Translator

logger = logging.getLogger(__name__)


class OneMixin:
    """Requests like `find one`."""

    @classmethod
    async def find_one(
        cls: Any,
        filter: Any | None = None,
        lang_code: str = deepcopy(Translator.DEFAULT_LOCALE),
        *args: tuple,
        **kwargs: dict[str, Any],
    ) -> dict[str, Any] | None:
        """Get a single document from the database."""
        # Get collection for current model.
        collection: AsyncCollection = Config.MONGO_DATABASE[cls.META["collection_name"]]
        # Correcting filter.
        if filter is not None:
            filter = correct_mongo_filter(cls, filter, lang_code)
        # Get document.
        mongo_doc = await collection.find_one(filter, *args, **kwargs)
        if mongo_doc is not None:
            mongo_doc = password_to_none(
                cls.META["field_name_and_type"],
                mongo_doc,
            )
        return mongo_doc

    @classmethod
    async def find_one_to_model_dict(
        cls: Any,
        filter: Any | None = None,
        lang_code: str = deepcopy(Translator.DEFAULT_LOCALE),
        *args: tuple,
        **kwargs: dict[str, Any],
    ) -> dict[str, Any] | None:
        """Find a single document and convert to Model in dictionary format."""
        # Get collection for current model.
        collection: AsyncCollection = Config.MONGO_DATABASE[cls.META["collection_name"]]
        # Correcting filter.
        if filter is not None:
            filter = correct_mongo_filter(cls, filter, lang_code)
        # Get document.
        raw_doc = None
        mongo_doc = await collection.find_one(filter, *args, **kwargs)

        if mongo_doc is not None:
            raw_doc = mongo_doc_to_model_dict(
                cls,
                mongo_doc,
                lang_code,
            )
        return raw_doc

    @classmethod
    async def find_one_to_instance_model(
        cls: Any,
        filter: Any | None = None,
        lang_code: str = deepcopy(Translator.DEFAULT_LOCALE),
        *args: tuple,
        **kwargs: dict[str, Any],
    ) -> Any | None:
        """Find a single document and convert it to a Model instance."""
        # Get collection for current model.
        collection: AsyncCollection = Config.MONGO_DATABASE[cls.META["collection_name"]]
        # Correcting filter.
        if filter is not None:
            filter = correct_mongo_filter(cls, filter, lang_code)
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
        lang_code: str = deepcopy(Translator.DEFAULT_LOCALE),
        *args: tuple,
        **kwargs: dict[str, Any],
    ) -> str | None:
        """Find a single document and convert it to a JSON string."""
        # Get collection for current model.
        collection: AsyncCollection = Config.MONGO_DATABASE[cls.META["collection_name"]]
        # Correcting filter.
        if filter is not None:
            filter = correct_mongo_filter(cls, filter, lang_code)
        # Get document.
        json_str: str | None = None
        mongo_doc = await collection.find_one(filter, *args, **kwargs)
        if mongo_doc is not None:
            # Convert document to Model instance.
            instance_model = cls.from_mongo_doc(mongo_doc)
            json_str = instance_model.to_json()
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
        lang_code: str = deepcopy(Translator.DEFAULT_LOCALE),
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
        collection: AsyncCollection = Config.MONGO_DATABASE[cls.META["collection_name"]]
        # Correcting filter.
        if filter is not None:
            filter = correct_mongo_filter(cls, filter, lang_code)
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
        lang_code: str = deepcopy(Translator.DEFAULT_LOCALE),
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
        collection: AsyncCollection = Config.MONGO_DATABASE[cls.META["collection_name"]]
        # Correcting filter.
        if filter is not None:
            filter = correct_mongo_filter(cls, filter, lang_code)
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
