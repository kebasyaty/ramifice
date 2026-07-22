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
"""Field of Model for enter password."""

from __future__ import annotations

__all__ = ("PasswordField",)

import logging
from typing import Any

from ramifice.config import Config
from ramifice.fields.field import Field, FieldCore

logger = logging.getLogger(__name__)


class PasswordField(Field):
    r"""Field of Model for enter password.

    Attention:
        - `Regular expression:` ^[-._!"`'#%&,:;<>=@{}~$()*+/\\?[]^|a-zA-Z0-9]{8,256}$
        - `Valid characters:` a-z A-Z 0-9 - . _ ! " ` ' # % & , : ; < > = @ { } ~ $ ( ) * + / \\ ? [ ] ^ |
        - `Number of characters:` from 8 to 256.
    """

    def __init__(
        self,
        label: str = "",
        placeholder: str = "",
        hide: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] = [],  # ruff:ignore[mutable-argument-default]
        required: bool = False,
    ) -> None:
        r"""Field of Model for enter password.

        Attention:
            - `Regular expression:` ^[-._!"`'#%&,:;<>=@{}~$()*+/\\?[]^|a-zA-Z0-9]{8,256}$
            - `Valid characters:` a-z A-Z 0-9 - . _ ! " ` ' # % & , : ; < > = @ { } ~ $ ( ) * + / \\ ? [ ] ^ |
            - `Number of characters:` from 8 to 256.

        Agrs:
            label: Text label for a web form field.
            placeholder: Displays prompt text.
            hide: Hide field from user.
            ignored: If true, the value of this field is not saved in the database.
            hint: An alternative for the `placeholder` parameter.
            warning: Warning information.
            required: Required field.
        """
        if Config.DEBUG:
            try:  # ruff:ignore[too-many-statements-in-try-clause]
                if not isinstance(label, str):
                    raise AssertionError("Parameter `label` - Not а `str` type!")
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
            except AssertionError as err:
                logger.critical(str(err))
                raise err

        Field.__init__(self, supported_types=(str, type(None)))

        field_attrs: dict[str, Any] = {
            "id": "",
            "name": "",
            "label": label,
            "input_type": "password",
            "value": None,
            "placeholder": placeholder,
            "hide": hide,
            "ignored": ignored,
            "hint": hint,
            "disabled": False,
            "warning": warning,
            "required": required,
            "errors": [],
            "field_type": "PasswordField",
            "group": "password",
        }

        self.__dict__["field_attrs"] = FieldCore(**field_attrs)
        self.__dict__["field__funcs"] = FieldCore()
