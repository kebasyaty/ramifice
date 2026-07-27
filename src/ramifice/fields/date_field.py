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
"""Field of Model for enter date."""

from __future__ import annotations

__all__ = ("DateField",)

import logging
from datetime import date
from typing import Any

from dateparser import parse

from ramifice.config import Config
from ramifice.fields.field import Field, FieldCore

logger = logging.getLogger(__name__)


class DateField(Field):
    """Field of Model for enter date."""

    def __init__(
        self,
        label: str = "",
        placeholder: str = "",
        default: date | str | None = None,
        is_hide: bool = False,
        is_disable: bool = False,
        is_ignore: bool = False,
        hint: str = "",
        warning: list[str] = [],  # ruff:ignore[mutable-argument-default]
        is_require: bool = False,
        is_readonly: bool = False,
        max_date: date | str | None = None,
        min_date: date | str | None = None,
    ) -> None:
        """Field of Model for enter date.

        Agrs:
            label: Text label for a web form field.
            placeholder: Displays prompt text.
            default: Value by default.
            is_hide: Hide field from user.
            is_disable: Blocks access and modification of the element.
            is_ignore: If true, the value of this field is not saved in the database.
            hint: An alternative for the `placeholder` parameter.
            warning: Warning information.
            required: Required field.
            readonly: Specifies that the field cannot be modified by the user.
            max_date: Maximum allowed date.
            min_date: Minimum allowed date.
        """
        if Config.DEBUG:
            try:  # ruff:ignore[too-many-statements-in-try-clause]
                if not isinstance(max_date, (date, str, type(None))):
                    raise AssertionError("Parameter `max_date` - Not а `date|str|None` type!")
                if not isinstance(min_date, (date, str, type(None))):
                    raise AssertionError("Parameter `min_date` - Not а `date|str|None` type!")
                if not isinstance(default, (date, str, type(None))):
                    raise AssertionError("Parameter `default` - Not а `date|str|None` type!")
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
            except AssertionError as err:
                logger.critical(str(err))
                raise err

        Field.__init__(self, supported_types=(date, str, type(None)))

        default = self.correction_date(default)
        max_date = self.correction_date(max_date)
        min_date = self.correction_date(min_date)

        if Config.DEBUG:
            try:  # ruff:ignore[too-many-statements-in-try-clause]
                if max_date is not None and min_date is not None and max_date <= min_date:
                    raise AssertionError("The `max_date` parameter should be more than the `min_date`!")
                if default is not None:
                    if max_date is not None and default > max_date:
                        raise AssertionError("Parameter `default` is more `max_date`!")
                    if min_date is not None and default < min_date:
                        raise AssertionError("Parameter `default` is less `min_date`!")
            except AssertionError as err:
                logger.critical(str(err))
                raise err

        field_core: dict[str, Any] = {
            "id": "",
            "name": "",
            "label": label,
            "input_type": "date",
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
            "unique": False,
            "max_date": max_date,
            "min_date": min_date,
            "errors": [],
            "field_type": "DateField",
            "group": "date",
        }

        self.__dict__["field_core"] = FieldCore(**field_core)

    @staticmethod
    def correction_date(value: Any | None) -> date | None:
        """Correction of date value."""
        if value is None:
            return None

        correct_value: date | None = None

        if isinstance(value, str):
            correct_value = parse(
                value,
                settings=Config.DATEPARSER_SETTINGS,
            )
            if correct_value is not None:
                correct_value = correct_value.date()
        else:
            correct_value = value

        return correct_value
