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
"""Field of Model for enter boolean value."""

from __future__ import annotations

__all__ = ("BooleanField",)

import logging
from typing import Any

from ramifice.config import Config
from ramifice.fields.field import Field, FieldCore

logger = logging.getLogger(__name__)


class BooleanField(Field):
    """Field of Model for enter boolean value."""

    def __init__(
        self,
        label: str = "",
        default: bool = False,
        is_hide: bool = False,
        is_disable: bool = False,
        is_ignore: bool = False,
        hint: str = "",
        warning: list[str] = [],  # ruff:ignore[mutable-argument-default]
    ) -> None:
        """Field of Model for enter boolean value.

        Args:
            label: Text label for a web form field.
            default: Default value.
            is_hide: Hide field from user.
            is_disable: Blocks access and modification of the element.
            is_ignore: If true, the value of this field is not saved in the database.
            hint: An alternative for the `placeholder` parameter.
            warning: Warning information.
        """
        if Config.DEBUG:
            try:  # ruff:ignore[too-many-statements-in-try-clause]
                if default is not None and not isinstance(default, bool):
                    raise AssertionError("Parameter `default` - Not а `bool` type!")
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
            except AssertionError as err:
                logger.critical(str(err))
                raise err

        Field.__init__(self, supported_types=(bool, type(None)))

        field_core: dict[str, Any] = {
            "id": "",
            "name": "",
            "label": label,
            "input_type": "checkbox",
            "value": None,
            "default": default,
            "is_hide": is_hide,
            "is_disable": is_disable,
            "is_ignore": is_ignore,
            "hint": hint,
            "warning": warning,
            "errors": [],
            "field_type": "BooleanField",
            "group": "bool",
        }

        self.__dict__["field_core"] = FieldCore(**field_core)
