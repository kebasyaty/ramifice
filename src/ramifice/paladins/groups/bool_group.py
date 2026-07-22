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
"""Group for checking boolean fields.

Supported fields:
    BooleanField
"""

from __future__ import annotations

__all__ = ("BoolGroupMixin",)

from typing import Any

from ramifice.paladins.utils import panic_type_error


class BoolGroupMixin:
    """Group for checking boolean fields.

    Supported fields:
        BooleanField
    """

    def bool_group(self, params: dict[str, Any]) -> None:
        """Checking boolean fields."""
        field = params["field_value"]
        # Get current value.
        value = field.value

        if not isinstance(value, (bool, type(None))):
            panic_type_error("bool | None", params)

        if not params["is_update"] and value is None:
            value = field.default
        # Insert result.
        if params["is_save"]:
            params["result_map"][field.name] = bool(value)
