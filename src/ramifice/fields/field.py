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
"""The main descriptor class for field types."""

from __future__ import annotations

__all__ = ("Field",)

import logging
from collections.abc import Callable
from copy import deepcopy
from datetime import date, datetime
from typing import Any

from dateparser import parse

from ramifice.errors import AttributeCannotBeDeleteError
from ramifice.translator import Translator

logger = logging.getLogger(__name__)


class FieldCore:
    """A class for carrying field arguments and methods."""

    def __init__(self, **kwargs: dict[str, Any]) -> None:
        self.current_locale = Translator.DEFAULT_LOCALE

        for key, value in kwargs.items():
            self.__dict__[key] = value

    def __delattr__(self, name: str) -> None:
        """Blocked Deleter."""
        raise AttributeCannotBeDeleteError(name)

    def get(self, name: str) -> Any | None:
        """Get the value by attribute name."""
        return self.__dict__.get(name)

    def to_dict(self) -> dict[str, Any]:
        """Convert FieldCore instance to a dictionary."""
        result: dict[str, Any] = {}
        for key, value in self.__dict__.items():
            if not isinstance(value, Callable):
                result[key] = value
        return result


class Field:
    """The main descriptor class for all field types."""

    def __init__(self, supported_types: tuple) -> None:
        """The main descriptor class for field types.

        Args:
            supported_types (tuple): Tuple of types supported by the `value` parameter.
        """
        self.supported_types = supported_types

    def __set_name__(self, owner: Any, name: str) -> None:  # ruff:ignore[undocumented-magic-method]
        self.name = name
        self.private_name = f"_{name}"
        self.field_name__core = f"{name}__core"
        self.field_name__core = f"{name}__core"

    def __get__(self, instance: Any, owner: Any) -> Any | None:
        """Triggered when reading the field."""
        if instance is None:
            return self

        value = getattr(instance, self.private_name)
        field_core = self.field_core
        if field_core.field_type == "TextField" and isinstance(value, dict):
            value = value.get(instance._LANG_CODE, "- -")

        return value

    def __set__(self, instance: Any, value: Any | None) -> None:
        """Triggered when assigning a value to the field."""
        if not isinstance(value, self.supported_types):
            supported_types_list = [
                item.__name__ if item is not type(None) else "None" for item in self.supported_types
            ]
            err_msg = f"Value must be an {' | '.join(supported_types_list)}"
            logger.critical(err_msg)
            raise TypeError(err_msg)
        field_name__core = self.field_name__core

        if not hasattr(instance, field_name__core):
            name = self.name
            field_core = deepcopy(self.field_core)
            field_core.id = f"id-{name}"
            field_core.name = name
            self.trans_field_core(instance, field_core, name)
            setattr(instance, field_name__core, field_core)

        field_core = getattr(instance, field_name__core)
        correct_value: Any | None = value
        if field_core.group == "date" and correct_value is not None:
            correct_value = self.correction_date_value(instance, field_core, value)

        setattr(instance, self.private_name, correct_value)
        field_core.value = correct_value

    def __delete__(self, instance) -> None:
        """Triggered when deleting the field."""
        err_msg = f"The attribute `{self.name}` cannot be delete!"
        logger.error(err_msg)
        raise AttributeCannotBeDeleteError(self.name)

    def trans_field_core(
        self,
        instance: Any,
        field_core: dict[str, Any],
        field_name: str,
    ) -> None:
        """Translate field attributes."""
        _ = (
            instance._CUSTOM_TRANSLATOR.gettext
            if field_name not in ["id", "created_at", "updated_at"]
            else instance._RAMIFICE_TRANSLATOR.gettext
        )

        label = field_core.get("label")
        field_core.label = _(label) if bool(label) else ""

        placeholder = field_core.get("placeholder")
        if placeholder is not None:
            field_core.placeholder = _(placeholder) if bool(placeholder) else ""

        hint = field_core.get("hint")
        field_core.hint = _(hint) if bool(hint) else ""

        warning_list = field_core.get("warning")
        if warning_list is not None:
            field_core.warning = [_(item) for item in warning_list]

    @staticmethod
    def correction_date_value(
        instance: Any,
        field_core: dict[str, Any],
        value: Any,
    ) -> datetime | date | None:
        """Correction of date value."""
        correct_value: datetime | date | None = None

        if isinstance(value, str):
            if "Time" in field_core.field_type:
                correct_value = parse(
                    value,
                    settings=instance._DATEPARSER_SETTINGS,
                )
                if correct_value is not None:
                    correct_value = correct_value.replace(microsecond=0)
            else:
                correct_value = parse(
                    value,
                    settings=instance._DATEPARSER_SETTINGS,
                )
                if correct_value is not None:
                    correct_value = correct_value.date()
        elif "Time" in field_core.field_type:
            correct_value = value.replace(microsecond=0)
        else:
            correct_value = value

        return correct_value
