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
"""Field of Model for enter identifier of document."""

from __future__ import annotations

__all__ = ("IDField",)

import logging
from typing import Any

from bson.objectid import ObjectId

from ramifice.config import Config
from ramifice.fields.field import Field, FieldCore

logger = logging.getLogger(__name__)


class IDField(Field):
    """Field of Model for enter identifier of document."""

    def __init__(
        self,
        label: str = "",
        placeholder: str = "",
        is_hide: bool = False,
        is_disable: bool = False,
        is_ignore: bool = False,
        hint: str = "",
        warning: list[str] = [],  # ruff:ignore[mutable-argument-default]
        is_require: bool = False,
        is_readonly: bool = False,
        is_unique: bool = False,
    ) -> None:
        """Field of Model for enter identifier of document.

        Agrs:
            label: Text label for a web form field.
            placeholder: Displays prompt text.
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
                if not isinstance(label, str):
                    raise AssertionError("Parameter `label` - Not а `str` type!")
                if not isinstance(is_disable, bool):
                    raise AssertionError("Parameter `disabled` - Not а `bool` type!")
                if not isinstance(is_hide, bool):
                    raise AssertionError("Parameter `hide` - Not а `bool` type!")
                if not isinstance(is_ignore, bool):
                    raise AssertionError("Parameter `ignored` - Not а `bool` type!")
                if not isinstance(hint, str):
                    raise AssertionError("Parameter `hint` - Not а `str` type!")
                if not isinstance(warning, list):
                    raise AssertionError("Parameter `warning` - Not а `list` type!")
                if not isinstance(placeholder, str):
                    raise AssertionError("Parameter `placeholder` - Not а `str` type!")
                if not isinstance(is_require, bool):
                    raise AssertionError("Parameter `required` - Not а `bool` type!")
                if not isinstance(is_readonly, bool):
                    raise AssertionError("Parameter `readonly` - Not а `bool` type!")
                if not isinstance(is_unique, bool):
                    raise AssertionError("Parameter `unique` - Not а `bool` type!")
            except AssertionError as err:
                logger.critical(str(err))
                raise err

        Field.__init__(self, supported_types=(ObjectId, type(None)))

        field_core: dict[str, Any] = {
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
            "alerts": [],
            "errors": [],
            "field_type": "IDField",
            "group": "id",
        }

        self.__dict__["field_core"] = FieldCore(**field_core)
        self.__dict__["field_funcs"] = FieldCore()
