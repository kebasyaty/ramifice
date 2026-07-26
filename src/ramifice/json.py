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
"""A mixin for converting models to a JSON string and back to a Model."""

from __future__ import annotations

__all__ = ("JsonMixin",)


import logging
from copy import deepcopy
from typing import Any

import orjson
from babel.dates import format_date, format_datetime
from bson.objectid import ObjectId
from dateparser import parse

logger = logging.getLogger(__name__)


class JsonMixin:
    """A mixin for converting Model to a JSON-string and back to a Model."""

    def to_json_dict(self) -> dict[str, Any]:
        """Convert Model instance to a dictionary."""
        metadata = self.__class__.META
        DESCRIPTOR_FIELDS = metadata["all_descriptor_fields"]
        LANG_CODE = self._LANG_CODE
        UTC_TIMEZONE = self._UTC_TIMEZONE
        json_dict: dict[str, Any] = {}

        for f_name in DESCRIPTOR_FIELDS:
            tmp__core = deepcopy(getattr(self, f"{f_name}__core"))
            field_type = tmp__core.field_type
            value = tmp__core.value

            if value is not None:
                if field_type == "IDField":
                    tmp__core.value = str(value)
                elif field_type == "PasswordField":
                    tmp__core.value = None
                elif field_type == "TextField":
                    tmp__core.value = value.get(LANG_CODE, "- -") if isinstance(value, dict) else value
                elif "Date" in field_type:
                    if "Time" in field_type:
                        tmp__core.value = format_datetime(
                            datetime=value,
                            format="medium",
                            tzinfo=UTC_TIMEZONE,
                            locale=LANG_CODE,
                        )
                    else:
                        tmp__core.value = format_date(
                            date=value,
                            format="medium",
                            locale=LANG_CODE,
                        )
            json_dict[f_name] = tmp__core.to_dict()

        return json_dict

    def to_json(self) -> str:
        """Convert Model instance to a JSON-string."""
        return orjson.dumps(self.to_json_dict()).decode("utf-8")

    @classmethod
    def from_json_dict(
        cls,
        json_dict: dict[str, Any],
    ) -> Any:
        """Convert JSON-dictionary to a Model instance."""
        metadata = cls.META
        DESCRIPTOR_FIELDS = metadata["all_descriptor_fields"]
        current_locale = json_dict.get("current_locale")

        if current_locale is None:
            err_msg = "It looks like you are using JSON format for Ajax and not Model."
            logger.critical(err_msg)
            raise ValueError(err_msg)

        # pyrefly: ignore [bad-argument-count]
        instance_model: Any = cls(current_locale)
        DATEPARSER_SETTINGS = instance_model.dateparser_settings

        for f_name in DESCRIPTOR_FIELDS:
            tmp__core_dict = deepcopy(json_dict[f_name])
            field_type = tmp__core_dict["field_type"]
            value = tmp__core_dict["value"]

            if value is not None:
                if field_type == "IDField":
                    tmp__core_dict["value"] = ObjectId(value)
                elif "Date" in field_type:
                    if "Time" in field_type:
                        tmp__core_dict["value"] = parse(
                            value,
                            settings=DATEPARSER_SETTINGS,
                        ).replace(microsecond=0)
                    else:
                        tmp__core_dict["value"] = parse(
                            value,
                            settings=DATEPARSER_SETTINGS,
                        ).date()
                else:
                    tmp__core_dict["value"] = value

            setattr(instance_model, f_name, tmp__core_dict["value"])
            f__core = getattr(instance_model, f"{f_name}__core")
            for key, val in tmp__core_dict.items():
                f__core.__dict__[key] = val

        return instance_model

    @classmethod
    def from_json(
        cls,
        json_str: str,
    ) -> Any:
        """Convert JSON-string from web request to a Model instance."""
        json_dict = orjson.loads(json_str)
        return cls.from_json_dict(json_dict)

    @classmethod
    def from_ajax_json(cls, json_str: str, lang_code: str) -> Any:
        """Convert JSON-string to a Model instance."""
        metadata = cls.META
        DESCRIPTOR_FIELDS = metadata["all_descriptor_fields"]
        json_dict = orjson.loads(json_str)
        # pyrefly: ignore [bad-argument-count]
        instance_model: Any = cls(lang_code)
        DATEPARSER_SETTINGS = instance_model.dateparser_settings

        for f_name in DESCRIPTOR_FIELDS:
            value = json_dict.get(f_name if f_name != "_id" else "id")

            if value is None:
                continue

            f__core = getattr(instance_model, f"{f_name}__core")
            field_type = f__core.field_type

            if field_type == "IDField":
                setattr(instance_model, f_name, ObjectId(value))
            elif "Date" in field_type:
                if "Time" in field_type:
                    setattr(
                        instance_model,
                        f_name,
                        parse(
                            value,
                            settings=DATEPARSER_SETTINGS,
                        ).replace(microsecond=0),
                    )
                else:
                    setattr(
                        instance_model,
                        f_name,
                        parse(
                            value,
                            settings=DATEPARSER_SETTINGS,
                        ).date(),
                    )
            else:
                setattr(instance_model, f_name, value)

        return instance_model
