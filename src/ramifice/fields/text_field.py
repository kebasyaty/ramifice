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
from typing import Any

from ramifice.config import Config
from ramifice.fields.field import Field

logger = logging.getLogger(__name__)


class TextField(Field):
    """Field of Model for enter text."""

    def __init__(
        self,
        label: str = "",
        placeholder: str = "",
        hide: bool = False,
        disabled: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] = [],  # ruff:ignore[mutable-argument-default]
        textarea: bool = False,
        use_editor: bool = False,
        required: bool = False,
        readonly: bool = False,
        unique: bool = False,
        max_length: int = 256,
        # Support for several language.
        multi_language: bool = False,
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
            multi_language: Is it need support for several languages.
        """
        if Config.DEBUG:
            try:  # ruff:ignore[too-many-statements-in-try-clause]
                if not isinstance(max_length, int):
                    raise AssertionError("Parameter `max_length` - Not а `int` type!")
                if not isinstance(label, str):
                    raise AssertionError("Parameter `label` - Not а `str` type!")
                if not isinstance(disabled, bool):
                    raise AssertionError("Parameter `disabled` - Not а `bool` type!")
                if not isinstance(hide, bool):
                    raise AssertionError("Parameter `hide` - Not а `bool` type!")
                if not isinstance(ignored, bool):
                    raise AssertionError("Parameter `ignored` - Not а `bool` type!")
                if not isinstance(hint, str):
                    raise AssertionError("Parameter `hint` - Not а `str` type!")
                if not isinstance(warning, list):
                    raise AssertionError("Parameter `warning` - Not а `list` type!")
                if not isinstance(placeholder, str):
                    raise AssertionError("Parameter `placeholder` - Not а `str` type!")
                if not isinstance(required, bool):
                    raise AssertionError("Parameter `required` - Not а `bool` type!")
                if not isinstance(readonly, bool):
                    raise AssertionError("Parameter `readonly` - Not а `bool` type!")
                if not isinstance(unique, bool):
                    raise AssertionError("Parameter `unique` - Not а `bool` type!")
                if not isinstance(textarea, bool):
                    raise AssertionError("Parameter `textarea` - Not а `bool` type!")
                if not isinstance(use_editor, bool):
                    raise AssertionError("Parameter `use_editor` - Not а `bool` type!")
                if not isinstance(max_length, int):
                    raise AssertionError("Parameter `max_length` - Not а `int` type!")
                if not isinstance(multi_language, bool):
                    raise AssertionError("Parameter `multi_language` - Not а `int` type!")
            except AssertionError as err:
                logger.critical(str(err))
                raise err

        Field.__init__(self, supported_types=(str, dict, type(None)))

        self.html_attrs: dict[str, Any] = {
            "id": "",
            "name": "",
            "label": label,
            "input_type": "text",
            "value": None,
            "placeholder": placeholder,
            "hide": hide,
            "disabled": disabled,
            "ignored": ignored,
            "hint": hint,
            "warning": warning,
            "required": required,
            "readonly": readonly,
            "unique": unique,
            "textarea": textarea,
            "use_editor": use_editor,
            "max_length": max_length,
            "multi_language": multi_language,
            "errors": [],
            "field_type": "TextField",
            "group": "text",
        }

    def __len__(self) -> int:
        """Return length of field `value`."""
        value = self.html_attrs["value"]
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
