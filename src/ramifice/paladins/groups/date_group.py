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
"""Group for checking date fields.

Supported fields:
    DateTimeField | DateField
"""

from __future__ import annotations

__all__ = ("DateGroupMixin",)

from datetime import datetime
from typing import Any

from babel.dates import format_date, format_datetime

from ramifice.paladins.utils import (
    accumulate_error,
    panic_type_error,
)


class DateGroupMixin:
    """Group for checking date fields.

    Supported fields:
        DateTimeField | DateField
    """

    def date_group(self, params: dict[str, Any]) -> None:
        """Checking date fields."""
        _ = self._RAMIFICE_TRANSLATOR.gettext
        LANG_CODE = self._LANG_CODE

        field = params["field_data"]
        # Get current value.
        value = field.value or field.default or None

        if not isinstance(value, (datetime, type(None))):
            panic_type_error("datetime | None", params)

        if value is None:
            if field.required:
                err_msg = _("Required field !")
                accumulate_error(err_msg, params)
            if params["is_save"]:
                params["result_map"][field.name] = None
            return

        # Validation the `max_date` field attribute.
        max_date = field.max_date
        if max_date is not None and value > max_date:
            value_str = (
                format_date(
                    date=value.date(),
                    format="medium",
                    locale=LANG_CODE,
                )
                if field.field_type == "DateField"
                else format_datetime(
                    datetime=value,
                    format="medium",
                    locale=LANG_CODE,
                )
            )
            max_date_str = (
                format_date(
                    date=max_date.date(),
                    format="medium",
                    locale=LANG_CODE,
                )
                if field.field_type == "DateField"
                else format_datetime(
                    datetime=max_date,
                    format="medium",
                    locale=LANG_CODE,
                )
            )
            err_msg = _(
                "The date {} must not be greater than max={} !",
            ).format(value_str, max_date_str)
            accumulate_error(err_msg, params)
        # Validation the `min_date` field attribute.
        min_date = field.min_date
        if min_date is not None and value < min_date:
            value_str = (
                format_date(
                    date=value.date(),
                    format="medium",
                    locale=LANG_CODE,
                )
                if field.field_type == "DateField"
                else format_datetime(
                    datetime=value,
                    format="medium",
                    locale=LANG_CODE,
                )
            )
            min_date_str = (
                format_date(
                    date=min_date.date(),
                    format="medium",
                    locale=LANG_CODE,
                )
                if field.field_type == "DateField"
                else format_datetime(
                    datetime=min_date,
                    format="medium",
                    locale=LANG_CODE,
                )
            )
            err_msg = _(
                "The date {} must not be less than min={} !",
            ).format(value_str, min_date_str)
            accumulate_error(err_msg, params)
        # Insert result.
        if params["is_save"]:
            params["result_map"][field.name] = value
