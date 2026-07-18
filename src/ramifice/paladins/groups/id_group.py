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
"""Group for checking id fields.

Supported fields:
    IDField
"""

from __future__ import annotations

__all__ = ("IDGroupMixin",)

from typing import Any

from bson.objectid import ObjectId

from ramifice.paladins.utils import accumulate_error, panic_type_error


class IDGroupMixin:
    """Group for checking id fields.

    Supported fields:
        IDField
    """

    def id_group(self, params: dict[str, Any]) -> None:
        """Checking id fields."""
        _ = params["_"]
        field = params["field_data"]
        # Get current value.
        value = field.value

        if not isinstance(value, (ObjectId, type(None))):
            panic_type_error("ObjectId | None", params)

        if value is None:
            if field.required:
                err_msg = _("Required field !")
                accumulate_error(err_msg, params)
            if params["is_save"]:
                params["result_map"][field.name] = None
            return
        # Validation of the MongoDB identifier in a string form.
        if not ObjectId.is_valid(value):
            err_msg = _("Invalid document ID !")
            accumulate_error(err_msg, params)
        # Insert result.
        if params["is_save"]:
            params["result_map"][field.name] = value
