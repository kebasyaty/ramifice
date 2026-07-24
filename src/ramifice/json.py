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


from copy import deepcopy
from typing import Any

import orjson
from babel.dates import format_date, format_datetime
from bson.objectid import ObjectId
from dateparser import parse

from ramifice.config import Config
from ramifice.translator import Translator


class JsonMixin:
    """A mixin for converting Model to a JSON-string and back to a Model."""

    def to_dict(self) -> dict[str, Any]:
        """Convert Model instance to a dictionary."""
        metadata = self.__class__.META
        descriptor_fields = metadata["all_descriptor_fields"]
        LANG_CODE = self._LANG_CODE
        UTC_TIMEZONE = self._UTC_TIMEZONE
        json_dict: dict[str, Any] = {}

        for f_name in descriptor_fields:
            tmp__attrs = deepcopy(getattr(self, f"{f_name}__attrs"))
            field_type = tmp__attrs.field_type
            value = tmp__attrs.value

            if value is not None:
                if field_type == "IDField":
                    tmp__attrs.value = str(value)
                elif field_type == "PasswordField":
                    tmp__attrs.value = None
                elif field_type == "TextField":
                    tmp__attrs.value = value.get(LANG_CODE, "- -") if isinstance(value, dict) else value
                elif "Date" in field_type:
                    if "Time" in field_type:
                        tmp__attrs.value = format_datetime(
                            datetime=value,
                            format="medium",
                            tzinfo=UTC_TIMEZONE,
                            locale=LANG_CODE,
                        )
                    else:
                        tmp__attrs.value = format_date(
                            date=value,
                            format="medium",
                            locale=LANG_CODE,
                        )
            json_dict[f_name] = tmp__attrs.to_dict()

        return json_dict

    def to_json(self) -> str:
        """Convert Model instance to a JSON-string."""
        return orjson.dumps(self.to_dict()).decode("utf-8")

    @classmethod
    def from_dict(
        cls,
        json_dict: dict[str, Any],
        lang_code: str = deepcopy(Translator.DEFAULT_LOCALE),
    ) -> Any:
        """Convert JSON-dictionary to a Model instance."""
        metadata = cls.META
        descriptor_fields = metadata["all_descriptor_fields"]
        DATEPARSER_SETTINGS = deepcopy(Config.DATEPARSER_SETTINGS)
        # pyrefly: ignore [bad-argument-count]
        instance: Any = cls(lang_code)

        for f_name in descriptor_fields:
            tmp__attrs_dict = deepcopy(json_dict[f_name])
            field_type = tmp__attrs_dict["field_type"]
            value = tmp__attrs_dict["value"]

            if value is not None:
                if field_type == "IDField":
                    tmp__attrs_dict["value"] = ObjectId(value)
                elif field_type == "PasswordField":
                    tmp__attrs_dict["value"] = value
                elif "Date" in field_type:
                    if "Time" in field_type:
                        tmp__attrs_dict["value"] = parse(
                            value,
                            settings=DATEPARSER_SETTINGS,
                        ).replace(microsecond=0)
                    else:
                        tmp__attrs_dict["value"] = parse(
                            value,
                            settings=DATEPARSER_SETTINGS,
                        ).date()

            setattr(instance, f_name, tmp__attrs_dict["value"])
            f__attrs = getattr(instance, f"{f_name}__attrs")
            for key, val in tmp__attrs_dict.items():
                f__attrs.__dict__[key] = val

        return instance

    @classmethod
    def from_json(cls, json_str: str) -> Any:
        """Convert JSON-string to a Model instance."""
        json_dict = orjson.loads(json_str)
        return cls.from_dict(json_dict)
