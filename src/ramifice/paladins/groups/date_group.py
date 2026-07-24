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

from typing import Any

from babel.dates import format_date, format_datetime

from ramifice.paladins.utils import accumulate_error


class DateGroupMixin:
    """Group for checking date fields.

    Supported fields:
        DateTimeField | DateField
    """

    def date_group(self, params: dict[str, Any]) -> None:
        """Checking date fields."""
        _ = params["_"]
        f__attrs = params["field__attrs"]
        f_name = f__attrs.name
        f_type = f__attrs.field_type
        LANG_CODE = self._LANG_CODE
        # Get current value.
        f_value = params["field_value"] or f__attrs.default or None

        if f_value is None:
            if f__attrs.required:
                err_msg = _("Required field !")
                accumulate_error(err_msg, params)
            if params["is_save"]:
                params["result_map"][f_name] = None
            return

        # Validation the `max_date` field attribute.
        max_date = f__attrs.max_date
        if max_date is not None and f_value > max_date:
            value_str = (
                format_date(
                    date=f_value.date(),
                    format="medium",
                    locale=LANG_CODE,
                )
                if f_type == "DateField"
                else format_datetime(
                    datetime=f_value,
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
                if f_type == "DateField"
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
        min_date = f__attrs.min_date
        if min_date is not None and f_value < min_date:
            value_str = (
                format_date(
                    date=f_value.date(),
                    format="medium",
                    locale=LANG_CODE,
                )
                if f_type == "DateField"
                else format_datetime(
                    datetime=f_value,
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
                if f_type == "DateField"
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
            params["result_map"][f_name] = f_value
