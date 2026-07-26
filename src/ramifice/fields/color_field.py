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
"""Field of Model for enter color code."""

from __future__ import annotations

__all__ = ("ColorField",)

import logging
from types import MethodType
from typing import Any

from ramifice.config import Config
from ramifice.fields.field import Field, FieldCore

logger = logging.getLogger(__name__)


class ColorField(Field):
    """Field of Model for enter color code.

    Default value is #000000 (black).

    Samples:
    #ffffff | #fff | #f2f2f2 | #f2f2f200 | rgb(255,0,24) |
    rgba(255,0,24,0.5) | rgba(#fff,0.5) | hsl(120,100%,50%) |
    hsla(170,23%,25%,0.2) | 0x00ffff
    """

    def __init__(
        self,
        label: str = "",
        placeholder: str = "",
        default: str | None = "#000000",
        is_hide: bool = False,
        is_disable: bool = False,
        is_ignore: bool = False,
        hint: str = "",
        warning: list[str] = [],  # ruff:ignore[mutable-argument-default]
        is_require: bool = False,
        is_readonly: bool = False,
        is_unique: bool = False,
    ) -> None:
        """Field of Model for enter color code.

        Default value is #000000 (black).

        Samples:
        #ffffff | #fff | #f2f2f2 | #f2f2f200 | rgb(255,0,24) |
        rgba(255,0,24,0.5) | rgba(#fff,0.5) | hsl(120,100%,50%) |
        hsla(170,23%,25%,0.2) | 0x00ffff

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
        """
        if Config.DEBUG:
            try:  # ruff:ignore[too-many-statements-in-try-clause]
                if default is not None:
                    if not isinstance(default, str):
                        raise AssertionError("Parameter `default` - Not а `str` type!")
                    if len(default) == 0:
                        raise AssertionError("The `default` parameter should not contain an empty string!")
                    if Config.REGEX["color_code"].match(default) is None:
                        raise AssertionError("Parameter `default` - Not а color code!")
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

        Field.__init__(self, supported_types=(str, type(None)))

        field_core: dict[str, Any] = {
            "id": "",
            "name": "",
            "label": label,
            "input_type": "text",
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
            "errors": [],
            "field_type": "ColorField",
            "group": "text",
        }

        self.__dict__["field_core"] = FieldCore(**field_core)
        self.field_core.size = MethodType(size, self.field_core)


def size(self) -> int:
    """Return length of field `value`."""
    value = self.value
    if isinstance(value, str):
        return len(value)
    return 0
