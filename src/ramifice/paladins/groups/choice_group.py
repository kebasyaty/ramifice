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
"""Group for checking choice fields.

Supported fields:
    ChoiceTextMultField | ChoiceTextMultDynField | ChoiceTextField
    | ChoiceTextDynField | ChoiceIntMultField | ChoiceIntMultDynField
    | ChoiceIntField | ChoiceIntDynField | ChoiceFloatMultField
    | ChoiceFloatMultDynField | ChoiceFloatField | ChoiceFloatDynField
"""

from __future__ import annotations

__all__ = ("ChoiceGroupMixin",)

from typing import Any

from ramifice.paladins.utils import accumulate_error


class ChoiceGroupMixin:
    """Group for checking choice fields.

    Supported fields:
            ChoiceTextMultField | ChoiceTextMultDynField | ChoiceTextField
            ChoiceTextDynField | ChoiceIntMultField | ChoiceIntMultDynField
            ChoiceIntField | ChoiceIntDynField | ChoiceFloatMultField
            ChoiceFloatMultDynField | ChoiceFloatField | ChoiceFloatDynField
    """

    def choice_group(self, params: dict[str, Any]) -> None:
        """Checking choice fields."""
        _ = params["_"]
        f_value = params["field_value"]
        f__attrs = params["field__attrs"]
        f__funcs = params["field__funcs"]
        f_name = f__attrs.name
        is_migrate = params["is_migration_process"]
        # Get current value.
        value = f_value or f__attrs.get("default") or None

        if value is None:
            if f__attrs.required:
                err_msg = _("Required field !")
                accumulate_error(err_msg, params)
            if params["is_save"]:
                params["result_map"][f_name] = None
            return
        # Does the field value match the possible options in choices.
        if not f__funcs.has_value(is_migrate):
            err_msg = _("Your choice does not match the options offered !")
            accumulate_error(err_msg, params)
        # Insert result.
        if params["is_save"]:
            params["result_map"][f_name] = value
