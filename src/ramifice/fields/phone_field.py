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
"""Field of Model for enter phone number."""

from __future__ import annotations

__all__ = ("PhoneField",)

import logging
from typing import Any

import phonenumbers

from ramifice.config import Config
from ramifice.fields.field import Field, FieldCore

logger = logging.getLogger(__name__)


class PhoneField(Field):
    """Field of Model for enter phone number.

    Attention:
        By default is used validator `phonenumbers.is_valid_number()`.
    """

    def __init__(
        self,
        label: str = "",
        placeholder: str = "",
        default: str | None = None,
        hide: bool = False,
        disabled: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] = [],  # ruff:ignore[mutable-argument-default]
        required: bool = False,
        readonly: bool = False,
        unique: bool = False,
    ) -> None:
        """Field of Model for enter phone number.

        Attention:
            By default is used validator `phonenumbers.is_valid_number()`.

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
                    try:
                        phone_default = phonenumbers.parse(default)
                        if not phonenumbers.is_valid_number(phone_default):
                            raise AssertionError()
                    except phonenumbers.phonenumberutil.NumberParseException:
                        raise AssertionError("Parameter `default` - Invalid Phone number!")  # ruff:ignore[raise-without-from-inside-except]
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
            except AssertionError as err:
                logger.critical(str(err))
                raise err

        Field.__init__(self, supported_types=(str, type(None)))

        field_attrs: dict[str, Any] = {
            "id": "",
            "name": "",
            "label": label,
            "input_type": "tel",
            "value": None,
            "default": default,
            "placeholder": placeholder,
            "hide": hide,
            "disabled": disabled,
            "ignored": ignored,
            "hint": hint,
            "warning": warning,
            "required": required,
            "readonly": readonly,
            "unique": unique,
            "errors": [],
            "field_type": "PhoneField",
            "group": "text",
        }

        self.__dict__["field_attrs"] = FieldCore(**field_attrs)
        self.__dict__["field_funcs"] = FieldCore(size=self.size)

    def size(self) -> int:
        """Return length of field `value`."""
        value = self.field_attrs.value
        if isinstance(value, str):
            return len(value)
        return 0
