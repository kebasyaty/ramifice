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
"""Group for checking integer fields.

Supported fields:
    IntegerField | FloatField
"""

from __future__ import annotations

__all__ = ("NumberGroupMixin",)

from typing import Any

from ramifice.paladins.utils import (
    accumulate_error,
    check_uniqueness,
)


class NumberGroupMixin:
    """Group for checking integer fields.

    Supported fields:
        IntegerField | FloatField
    """

    async def number_group(self, params: dict[str, Any]) -> None:
        """Checking number fields."""
        _ = params["_"]
        f_value = params["field_value"]
        f__attrs = params["field__attrs"]
        f_name = f__attrs.name
        # Get current value.
        value = f_value

        if value is None:
            value = f__attrs.default

        if value is None:
            if f__attrs.required:
                err_msg = _("Required field !")
                accumulate_error(err_msg, params)
            if params["is_save"]:
                params["result_map"][f_name] = None
            return
        # Validation the `max_number` field attribute.
        max_number = f__attrs.max_number
        if max_number is not None and value > max_number:
            err_msg = _(
                "The value {} must not be greater than max={} !",
            ).format(value, max_number)
            accumulate_error(err_msg, params)
        # Validation the `min_number` field attribute.
        min_number = f__attrs.min_number
        if min_number is not None and value < min_number:
            err_msg = _(
                "The value {} must not be less than min={} !",
            ).format(value, min_number)
            accumulate_error(err_msg, params)
        # Validation the `unique` field attribute.
        if f__attrs.unique and not await check_uniqueness(value, params, f_name):
            err_msg = _("Is not unique !")
            accumulate_error(err_msg, params)
        # Insert result.
        if params["is_save"]:
            params["result_map"][f_name] = value
