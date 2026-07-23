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
"""Tool of Commons - A set of auxiliary methods."""

from __future__ import annotations

__all__ = (
    "correct_mongo_filter",
    "password_to_none",
    "mongo_doc_to_model_dict",
)

from copy import deepcopy
from typing import Any

from babel.dates import format_date, format_datetime
from bson import json_util

from ramifice.config import Config


def correct_mongo_filter(cls_model: Any, filter: Any, lang_code: str) -> Any:
    """Correcting filter of request.

    Corrects `TextField` fields that require localization of translation.
    """
    filter_json: str = json_util.dumps(filter)
    filter_json = (
        cls_model.META["regex_mongo_filter"]
        .sub(rf'\g<field>.{lang_code}":', filter_json)
        .replace(
            '":.',
            ".",
        )
    )
    return json_util.loads(filter_json)


def password_to_none(
    field_name_and_type: dict[str, str],
    mongo_doc: dict[str, Any],
) -> dict[str, Any]:
    """In the Mongo document, set all passwords to None."""
    for f_name, t_name in field_name_and_type.items():
        if t_name == "PasswordField":
            mongo_doc[f_name] = None
    return mongo_doc


def mongo_doc_to_model_dict(
    cls_model: Any,
    mongo_doc: dict[str, Any],
    lang_code: str,
) -> dict[str, Any]:
    """Convert Mongo document to Model document.

    Special changes:
        - `_id to id (str)`
        - `password to None`
        - `date to str`
        - `datetime to str`
    """
    UTC_TIMEZONE = deepcopy(Config.UTC_TIMEZONE)
    descriptor_fields = cls_model.META["all_descriptor_fields"]
    instance_model: Any = cls_model(lang_code)
    model_dict: dict[str, Any] = {}

    for f_name in descriptor_fields:
        value = mongo_doc.get(f_name)

        if value is None:
            model_dict[f_name] = None
            continue

        f__attrs = getattr(instance_model, f"{f_name}__attrs")
        field_type = f__attrs.field_type

        if field_type == "TextField":
            model_dict[f_name] = value.get(lang_code, "- -") if isinstance(value, dict) else value
        elif "Date" in field_type:
            if "Time" in field_type:
                model_dict[f_name] = format_datetime(
                    datetime=value,
                    format="medium",
                    tzinfo=UTC_TIMEZONE,
                    locale=lang_code,
                )
            else:
                model_dict[f_name] = format_date(
                    date=value.date(),
                    format="medium",
                    locale=lang_code,
                )
        elif field_type == "IDField":
            model_dict["id"] = str(value)
        elif field_type == "PasswordField":
            model_dict[f_name] = None
        else:
            model_dict[f_name] = value

    return model_dict
