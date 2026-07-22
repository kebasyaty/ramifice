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
"""Field of Model for enter date and time."""

from __future__ import annotations

__all__ = ("DateTimeField",)

import logging
from datetime import datetime
from typing import Any

from dateparser import parse

from ramifice.config import Config
from ramifice.fields.field import Field, FieldCore

logger = logging.getLogger(__name__)


class DateTimeField(Field):
    """Field of Model for enter date and time."""

    def __init__(
        self,
        label: str = "",
        placeholder: str = "",
        default: datetime | str | None = None,
        hide: bool = False,
        disabled: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] = [],  # ruff:ignore[mutable-argument-default]
        required: bool = False,
        readonly: bool = False,
        max_date: datetime | str | None = None,
        min_date: datetime | str | None = None,
    ) -> None:
        """Field of Model for enter date and time.

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
            max_date: Maximum allowed date and time.
            min_date: Minimum allowed date and time.
        """
        if Config.DEBUG:
            try:  # ruff:ignore[too-many-statements-in-try-clause]
                if not isinstance(max_date, (datetime, str, type(None))):
                    raise AssertionError("Parameter `max_date` - Not а `datetime|str|None` type!")
                if not isinstance(min_date, (datetime, str, type(None))):
                    raise AssertionError("Parameter `min_date` - Not а `datetime|str|None` type!")
                if not isinstance(default, (datetime, str, type(None))):
                    raise AssertionError("Parameter `default` - Not а `datetime|str|None` type!")
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
            except AssertionError as err:
                logger.critical(str(err))
                raise err

        Field.__init__(self, supported_types=(datetime, str, type(None)))

        default = self.correction_datetime(default)
        max_date = self.correction_datetime(max_date)
        min_date = self.correction_datetime(min_date)

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

        field_attrs: dict[str, Any] = {
            "id": "",
            "name": "",
            "label": label,
            "input_type": "datetime",
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
            "unique": False,
            "max_date": max_date,
            "min_date": min_date,
            "errors": [],
            "field_type": "DateTimeField",
            "group": "date",
        }

        self.__dict__["field_attrs"] = FieldCore(**field_attrs)
        self.__dict__["field_funcs"] = FieldCore()

    def correction_datetime(
        self,
        value: Any | None,
    ) -> datetime | None:
        """Correction of datetime value."""
        if value is None:
            return None

        correct_value: datetime | None = None

        if isinstance(value, str):
            correct_value = parse(
                value,
                settings=Config.DATEPARSER_SETTINGS,
            )
            if correct_value is not None:
                correct_value = correct_value.replace(microsecond=0).replace(
                    hour=0,
                    minute=0,
                    second=0,
                    microsecond=0,
                )
        else:
            correct_value = value.replace(
                hour=0,
                minute=0,
                second=0,
                microsecond=0,
            )

        return correct_value
