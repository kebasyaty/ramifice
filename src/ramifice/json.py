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

import copy
from typing import Any

import orjson
from babel.dates import format_date, format_datetime
from bson.objectid import ObjectId
from dateutil.parser import parse

from ramifice.config import Config


class JsonMixin:
    """A mixin for converting Model to a JSON-string and back to a Model."""

    def to_dict(self) -> dict[str, Any]:
        """Convert Model instance to a dictionary."""
        metadata = self.__class__.META
        descriptor_fields = metadata["all_descriptor_fields"]
        LANG_CODE = self._LANG_CODE
        json_dict: dict[str, Any] = {}

        for f_name in descriptor_fields:
            f_html_attrs = copy.deepcopy(getattr(self, f"{f_name}_html_attrs"))
            group = f_html_attrs["group"]
            value = f_html_attrs["value"]
            if value is not None:
                if group == "id":
                    f_html_attrs["value"] = str(value)
                elif group == "password":
                    f_html_attrs["value"] = None
                elif group == "date":
                    if f_html_attrs["field_type"] == "DateField":
                        f_html_attrs["value"] = format_date(
                            date=value.date(),
                            format="medium",
                            locale=LANG_CODE,
                        )
                    else:
                        f_html_attrs["value"] = format_datetime(
                            datetime=value,
                            format="medium",
                            tzinfo=Config.UTC_TIMEZONE,
                            locale=LANG_CODE,
                        )
            json_dict[f_name] = f_html_attrs

        return json_dict

    def to_json(self) -> str:
        """Convert Model instance to a JSON-string."""
        return orjson.dumps(self.to_dict()).decode("utf-8")

    @classmethod
    def from_dict(cls, json_dict: dict[str, Any]) -> Any:
        """Convert JSON-dictionary to a Model instance."""
        metadata = cls.META
        descriptor_fields = metadata["all_descriptor_fields"]
        instance = cls()

        for f_name in descriptor_fields:
            tmp_html_attrs = json_dict[f_name]
            group = tmp_html_attrs["group"]
            value = tmp_html_attrs["value"]

            if value is not None:
                if group == "id":
                    tmp_html_attrs["value"] = ObjectId(value)
                elif group == "password":
                    tmp_html_attrs["value"] = value
                elif group == "date":
                    tmp_html_attrs["value"] = parse(value)

            setattr(instance, f_name, tmp_html_attrs["value"])
            f_html_attrs = getattr(instance, f"{f_name}_html_attrs")
            for key, val in tmp_html_attrs.items():
                f_html_attrs[key] = val

        return instance

    @classmethod
    def from_json(cls, json_str: str) -> Any:
        """Convert JSON-string to a Model instance."""
        json_dict = orjson.loads(json_str)
        return cls.from_dict(json_dict)
