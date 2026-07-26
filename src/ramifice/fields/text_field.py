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
"""Field of Model for enter text."""

from __future__ import annotations

__all__ = ("TextField",)

import logging
from types import MethodType

from ramifice.config import Config
from ramifice.fields.field import Field, FieldCore

logger = logging.getLogger(__name__)


class TextField(Field):
    """Field of Model for enter text."""

    def __init__(
        self,
        label: str = "",
        placeholder: str = "",
        is_hide: bool = False,
        is_disable: bool = False,
        is_ignore: bool = False,
        hint: str = "",
        warning: list[str] = [],  # ruff:ignore[mutable-argument-default]
        is_textarea: bool = False,
        is_use_editor: bool = False,
        is_require: bool = False,
        is_readonly: bool = False,
        is_unique: bool = False,
        max_length: int = 256,
        # Support for several language.
        is_multilingual: bool = False,
    ) -> None:
        """Field of Model for enter text.

        Agrs:
            label: Text label for a web form field.
            placeholder: Displays prompt text.
            hide: Hide field from user.
            disabled: Blocks access and modification of the element.
            ignored: If true, the value of this field is not saved in the database.
            hint: An alternative for the `placeholder` parameter.
            warning: Warning information.
            textarea: Is it necessary to use the Textarea widget.
            use_editor: Is it necessary to use the widget of the text editor.
            required: Required field.
            readonly: Specifies that the field cannot be modified by the user.
            unique: The unique value of a field in a collection.
            max_length: The maximum line length.
            is_multilingual: Is it need support for several languages.
        """
        if Config.DEBUG:
            try:  # ruff:ignore[too-many-statements-in-try-clause]
                if not isinstance(max_length, int):
                    raise AssertionError("Parameter `max_length` - Not а `int` type!")
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
                if not isinstance(is_textarea, bool):
                    raise AssertionError("Parameter `textarea` - Not а `bool` type!")
                if not isinstance(is_use_editor, bool):
                    raise AssertionError("Parameter `use_editor` - Not а `bool` type!")
                if not isinstance(max_length, int):
                    raise AssertionError("Parameter `max_length` - Not а `int` type!")
                if not isinstance(is_multilingual, bool):
                    raise AssertionError("Parameter `is_multilingual` - Not а `bool` type!")
            except AssertionError as err:
                logger.critical(str(err))
                raise err

        Field.__init__(self, supported_types=(str, dict, type(None)))

        field_core = {
            "id": "",
            "name": "",
            "label": label,
            "input_type": "text",
            "value": None,
            "placeholder": placeholder,
            "is_hide": is_hide,
            "is_disable": is_disable,
            "is_ignore": is_ignore,
            "hint": hint,
            "warning": warning,
            "is_require": is_require,
            "is_readonly": is_readonly,
            "is_unique": is_unique,
            "is_textarea": is_textarea,
            "is_use_editor": is_use_editor,
            "max_length": max_length,
            "is_multilingual": is_multilingual,
            "errors": [],
            "field_type": "TextField",
            "group": "text",
        }

        self.__dict__["field_core"] = FieldCore(**field_core)
        self.field_core.size = MethodType(size, self.field_core)

    def __len__(self) -> int:
        """Return length of field `value`."""
        value = self.field_core.value
        if isinstance(value, str):
            return len(value)
        if isinstance(value, dict):
            count = 0
            for text in value.values():
                tmp = len(text)
                if tmp > count:
                    count = tmp
            return count
        return 0


def size(self) -> int:
    """Return length of field `value`."""
    value = self.value
    if isinstance(value, str):
        return len(value)
    if isinstance(value, dict):
        count = 0
        for text in value.values():
            tmp = len(text)
            if tmp > count:
                count = tmp
        return count
    return 0
