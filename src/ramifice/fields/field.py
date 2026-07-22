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
from datetime import datetime
from typing import Any

from dateparser import parse

from ramifice.errors import AttributeCannotBeDeleteError

logger = logging.getLogger(__name__)


class FieldCore:
    """A class for carrying field arguments and methods."""

    def __init__(self, **kwargs: dict[str, Any]) -> None:
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
        self.field_name__attrs = f"{name}__attrs"
        self.field_name__funcs = f"{name}__funcs"

    def __get__(self, instance: Any, owner: Any) -> Any | None:
        """Triggered when reading the field."""
        if instance is None:
            return self
        return getattr(instance, self.private_name, None)

    def __set__(self, instance: Any, value: Any | None) -> None:
        """Triggered when assigning a value to the field."""
        if not isinstance(value, self.supported_types):
            supported_types_list = [
                item.__name__ if item is not type(None) else "None" for item in self.supported_types
            ]
            err_msg = f"Value must be an {' | '.join(supported_types_list)}"
            logger.critical(err_msg)
            raise TypeError(err_msg)
        field_name__attrs = self.field_name__attrs
        field_attrs = self.field_attrs

        if not hasattr(instance, field_name__attrs):
            name = self.name
            field_attrs.id = f"id-{name}"
            field_attrs.name = name
            self.trans_field_attrs(instance, name)
            setattr(instance, field_name__attrs, field_attrs)
            setattr(instance, self.field_name__funcs, self.field_funcs)

        correct_value: Any | None = value
        if field_attrs.group == "date" and correct_value is not None:
            correct_value = self.correction_date_value(instance, field_attrs, value)

        setattr(instance, self.private_name, correct_value)
        getattr(instance, field_name__attrs).value = correct_value

    def __delete__(self, instance) -> None:
        """Triggered when deleting the field."""
        err_msg = f"The attribute `{self.name}` cannot be delete!"
        logger.error(err_msg)
        raise AttributeCannotBeDeleteError(self.name)

    def trans_field_attrs(self, instance: Any, field_name: str) -> None:
        """Translate field attributes."""
        _ = (
            instance._CUSTOM_TRANSLATOR.gettext
            if field_name not in ["id", "created_at", "updated_at"]
            else instance._RAMIFICE_TRANSLATOR.gettext
        )
        field_attrs = self.field_attrs

        label = field_attrs.get("label")
        field_attrs.label = _(label) if bool(label) else ""

        placeholder = field_attrs.get("placeholder")
        if placeholder is not None:
            field_attrs.placeholder = _(placeholder) if bool(placeholder) else ""

        hint = field_attrs.get("hint")
        field_attrs.hint = _(hint) if bool(hint) else ""

        warning_list = field_attrs.get("warning")
        if warning_list is not None:
            field_attrs.warning = [_(item) for item in warning_list]

    def correction_date_value(
        self,
        instance: Any,
        field_attrs: dict[str, Any],
        value: Any,
    ) -> datetime | None:
        """Correction of date value."""
        correct_value: datetime | None = None
        if isinstance(value, str):
            if "Time" in field_attrs.field_type:
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
                    correct_value = correct_value.replace(microsecond=0).replace(
                        hour=0,
                        minute=0,
                        second=0,
                        microsecond=0,
                    )
        else:
            if "Time" in field_attrs.field_type:
                correct_value = value.replace(microsecond=0)
            else:
                correct_value = value.replace(
                    hour=0,
                    minute=0,
                    second=0,
                    microsecond=0,
                )

        return correct_value
