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
"""Field of Model.

Type of selective integer field with dynamic addition of elements.
"""

from __future__ import annotations

__all__ = ("ChoiceIntMultDynField",)

import logging
from types import MethodType
from typing import Any

from ramifice.config import Config
from ramifice.fields.field import Field, FieldCore

logger = logging.getLogger(__name__)


class ChoiceIntMultDynField(Field):
    """Field of Model.

    Type of selective integer field with dynamic addition of elements.
    For simulate relationship Many-to-Many.
    """

    def __init__(
        self,
        label: str = "",
        is_hide: bool = False,
        is_disable: bool = False,
        is_ignore: bool = False,
        hint: str = "",
        warning: list[str] = [],  # ruff:ignore[mutable-argument-default]
        is_require: bool = False,
        is_readonly: bool = False,
    ) -> None:
        """Field of Model.

        Type of selective integer field with dynamic addition of elements.
        For simulate relationship Many-to-Many.

        Args:
            label: Text label for a web form field.
            hide: Hide field from user.
            disabled: Blocks access and modification of the element.
            ignored: If true, the value of this field is not saved in the database.
            hint: An alternative for the `placeholder` parameter.
            warning: Warning information.
            required: Required field.
            readonly: Specifies that the field cannot be modified by the user.
        """
        if Config.DEBUG:
            try:  # ruff:ignore[too-many-statements-in-try-clause]
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
                if not isinstance(is_require, bool):
                    raise AssertionError("Parameter `is_require` - Not а `bool` type!")
                if not isinstance(is_readonly, bool):
                    raise AssertionError("Parameter `is_readonly` - Not а `bool` type!")
            except AssertionError as err:
                logger.critical(str(err))
                raise err

        Field.__init__(self, supported_types=(list, type(None)))

        field_core: dict[str, Any] = {
            "id": "",
            "name": "",
            "label": label,
            "value": None,
            "is_hide": is_hide,
            "is_disable": is_disable,
            "is_ignore": is_ignore,
            "hint": hint,
            "warning": warning,
            "is_require": is_require,
            "is_readonly": is_readonly,
            "unique": False,
            "is_multiple": True,
            "choices": None,
            "errors": [],
            "field_type": "ChoiceIntMultDynField",
            "group": "choice",
        }

        self.__dict__["field_core"] = FieldCore(**field_core)
        self.field_core.has_value = MethodType(has_value, self.field_core)


def has_value(self, is_migrate: bool = False) -> bool:
    """Does the field value match the possible options in choices."""
    if is_migrate:
        return True
    value = self.value
    if value is not None:
        choices = self.choices
        if len(value) == 0 or not bool(choices):
            return False
        value_list = [item[0] for item in choices]  # type: ignore[union-attr]
        for item in value:
            if item not in value_list:
                return False
    return True
