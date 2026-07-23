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
"""Tool of Paladins - A set of auxiliary methods."""

from __future__ import annotations

__all__ = (
    "ignored_fields_to_none",
    "refresh_from_mongo_doc",
    "accumulate_error",
    "check_uniqueness",
)

import logging
from typing import Any

from ramifice.errors import PanicError

logger = logging.getLogger(__name__)


def ignored_fields_to_none(instance_model: Any) -> None:
    """Reset the values of ignored fields to None."""
    descriptor_fields = instance_model.__class__.META["all_descriptor_fields"]

    for f_name in descriptor_fields:
        f__attrs = getattr(instance_model, f"{f_name}__attrs")
        if f__attrs.ignored:
            f__attrs.value = None
            setattr(instance_model, f_name, None)


def refresh_from_mongo_doc(instance_model: Any, mongo_doc: dict[str, Any]) -> None:
    """Update object instance from Mongo document."""
    lang_code = instance_model._LANG_CODE

    for mongo_f_name, mongo_value in mongo_doc.items():
        f_name = mongo_f_name if mongo_f_name != "_id" else "id"
        f__attrs = getattr(instance_model, f"{f_name}__attrs")
        field_type = f__attrs.field_type

        if field_type == "TextField" and f__attrs.multi_language:
            f__attrs.value = mongo_value.get(lang_code, "- -") if isinstance(mongo_value, dict) else mongo_value
        elif field_type == "PasswordField":
            f__attrs.value = None
        else:
            f__attrs.value = mongo_value
        setattr(instance_model, f_name, mongo_value)


def accumulate_error(error_message: str, params: dict[str, Any]) -> None:
    """Accumulating errors to ModelName.field_name.errors ."""
    f__attrs = params["field__attrs"]

    if not f__attrs.hide:
        f__attrs.errors.append(error_message)
        if not params["is_error_symptom"]:
            params["is_error_symptom"] = True
    else:
        err_msg = (
            f">>hidden field<< -> Model: `{params['full_model_name']}` > "
            + f"Field: `{f__attrs.name}`"
            + f" => {error_message}"
        )
        logger.critical(err_msg)
        raise PanicError(err_msg)


async def check_uniqueness(
    value: str | int | float,
    params: dict[str, Any],
    field_name: str | None = None,
    is_multi_language: bool = False,
) -> bool:
    """Checking the uniqueness of the value in the collection."""
    q_filter = None

    if is_multi_language:
        lang_filter = [{f"{field_name}.{lang}": value} for lang in params["LANGUAGES"]]
        q_filter = {
            "$and": [
                {"_id": {"$ne": params["doc_id"]}},
                {"$or": lang_filter},
            ],
        }
    else:
        q_filter = {
            "$and": [
                {"_id": {"$ne": params["doc_id"]}},
                {field_name: value},
            ],
        }
    return await params["collection"].find_one(q_filter) is None
