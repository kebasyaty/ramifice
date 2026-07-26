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
"""Field of Model for enter (int) number."""

from __future__ import annotations

__all__ = ("IntegerField",)

import logging
from typing import Any, Literal

from ramifice.config import Config
from ramifice.fields.field import Field, FieldCore

logger = logging.getLogger(__name__)


class IntegerField(Field):
    """Field of Model for enter (int) number.

    Agrs:
        label: Text label for a web form field.
        placeholder: Displays prompt text.
        default: Value by default.
        hide: Hide field from user.
        disabled: Blocks access and modification of the element.
        ignored: If true, the value of this field is not saved in the database.
        hint: An alternative for the `placeholder` parameter.
        warning: Warning information.
        required: Required field.
        readonly: Specifies that the field cannot be modified by the user.
        unique: The unique value of a field in a collection.
        max_number: Maximum allowed number.
        min_number: Minimum allowed number.
        step: Increment step for numeric fields.
        input_type: Field type - `number` or `range`.
    """

    def __init__(  # ruff:ignore[undocumented-public-init]
        self,
        label: str = "",
        placeholder: str = "",
        default: int | None = None,
        is_hide: bool = False,
        is_disable: bool = False,
        is_ignore: bool = False,
        hint: str = "",
        warning: list[str] = [],  # ruff:ignore[mutable-argument-default]
        is_require: bool = False,
        is_readonly: bool = False,
        is_unique: bool = False,
        max_number: int | None = None,
        min_number: int | None = None,
        step: int = 1,
        input_type: Literal["number", "range"] = "number",
    ) -> None:
        if Config.DEBUG:
            try:  # ruff:ignore[too-many-statements-in-try-clause]
                if input_type not in ["number", "range"]:
                    raise AssertionError(
                        "Parameter `input_type` - Invalid input type! "
                        + "The permissible value of `number` or `range`.",
                    )
                if max_number is not None and not isinstance(max_number, int):
                    raise AssertionError("Parameter `max_number` - Not а number `int` type!")
                if min_number is not None and not isinstance(min_number, int):
                    raise AssertionError("Parameter `min_number` - Not а number `int` type!")
                if not isinstance(step, int):
                    raise AssertionError("Parameter `step` - Not а number `int` type!")
                if max_number is not None and min_number is not None and max_number <= min_number:
                    raise AssertionError("The `max_number` parameter should be more than the `min_number`!")
                if default is not None:
                    if not isinstance(default, int):
                        raise AssertionError("Parameter `default` - Not а number `int` type!")
                    if max_number is not None and default > max_number:
                        raise AssertionError("Parameter `default` is more `max_number`!")
                    if max_number is not None and default < min_number:
                        raise AssertionError("Parameter `default` is less `min_number`!")
                if not isinstance(label, str):
                    raise AssertionError("Parameter `label` - Not а `str` type!")
                if not isinstance(is_disable, bool):
                    raise AssertionError("Parameter `is_disable` - Not а `bool` type!")
                if not isinstance(is_hide, bool):
                    raise AssertionError("Parameter `is_hide` - Not а `bool` type!")
                if not isinstance(is_ignore, bool):
                    raise AssertionError("Parameter `is_ignore` - Not а `bool` type!")
                if not isinstance(hint, str):
                    raise AssertionError("Parameter `hint` - Not а `str` type!")
                if not isinstance(warning, list):
                    raise AssertionError("Parameter `warning` - Not а `list` type!")
                if not isinstance(placeholder, str):
                    raise AssertionError("Parameter `placeholder` - Not а `str` type!")
                if not isinstance(is_require, bool):
                    raise AssertionError("Parameter `is_require` - Not а `bool` type!")
                if not isinstance(is_readonly, bool):
                    raise AssertionError("Parameter `is_readonly` - Not а `bool` type!")
                if not isinstance(is_unique, bool):
                    raise AssertionError("Parameter `unique` - Not а `bool` type!")
            except AssertionError as err:
                logger.critical(str(err))
                raise err

        Field.__init__(self, supported_types=(int, type(None)))

        field_core: dict[str, Any] = {
            "id": "",
            "name": "",
            "label": label,
            "input_type": input_type,
            "value": None,
            "default": default,
            "placeholder": placeholder,
            "is_hide": is_hide,
            "is_disable": is_disable,
            "is_ignore": is_ignore,
            "hint": hint,
            "warning": warning,
            "is_require": is_require,
            "is_readonly": is_readonly,
            "is_unique": is_unique,
            "max_number": max_number,
            "min_number": min_number,
            "step": step,
            "errors": [],
            "field_type": "IntegerField",
            "group": "number",
        }

        self.__dict__["field_core"] = FieldCore(**field_core)
