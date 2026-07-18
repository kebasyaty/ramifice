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

from typing import Any

from dateutil.parser import parse

from ramifice.errors import AttributeCannotBeDeleteError


class Field:
    """The main descriptor class for field types.

    Args:
        supported_types (tuple): Tuple of types supported by the `value` parameter.
    """

    def __init__(self, supported_types: tuple) -> None:  # noqa: D107
        self.supported_types = supported_types

    def __set_name__(self, owner: Any, name: str) -> None:  # noqa: D105 pyrefly: ignore[unused-parameter]
        self.name = name
        self.private_name = f"_{name}"
        self.field_name_html_attrs = f"{name}_html_attrs"

    def __get__(self, instance: Any, owner: Any) -> Any | None:
        """Triggered when reading the field."""
        if instance is None:
            return self
        return getattr(instance, self.private_name, None)

    def __set__(self, instance: Any, value: Any | None) -> None:  # pyrefly: ignore[unused-parameter]
        """Triggered when assigning a value to the field."""
        if not isinstance(value, self.supported_types):
            supported_types_list = [
                item.__name__ if item is not type(None) else "None" for item in self.supported_types
            ]
            msg = f"Value must be an {' | '.join(supported_types_list)}"
            raise TypeError(msg)
        field_name_html_attrs = self.field_name_html_attrs
        html_attrs = self.html_attrs

        if not hasattr(instance, field_name_html_attrs):
            name = self.name
            html_attrs["id"] = f"id-{name}"
            html_attrs["name"] = name
            self.trans_field_attrs(instance, name)
            setattr(instance, field_name_html_attrs, html_attrs)

        correct_value: Any | None = value
        if html_attrs["group"] == "date" and isinstance(value, str):
            correct_value = parse(value)

        setattr(instance, self.private_name, correct_value)
        getattr(instance, field_name_html_attrs)["value"] = correct_value

    def __delete__(self, instance) -> None:
        """Triggered when deleting the field."""
        raise AttributeCannotBeDeleteError(self.name)

    def trans_field_attrs(self, instance: Any, field_name: str) -> None:
        """Translate field attributes."""
        gettext = (
            instance.__dict__["_RAMIFICE_TRANSLATOR"].gettext
            if field_name in ["id", "created_at", "updated_at"]
            else instance.__dict__["_CUSTOM_TRANSLATOR"].gettext
        )
        html_attrs = self.html_attrs

        label = html_attrs.get("label")
        html_attrs["label"] = gettext(label) if bool(label) else ""

        placeholder = html_attrs.get("placeholder")
        if placeholder is not None:
            html_attrs["placeholder"] = gettext(placeholder) if bool(placeholder) else ""

        hint = html_attrs.get("hint")
        html_attrs["hint"] = gettext(hint) if bool(hint) else ""

        warning_list = html_attrs.get("warning")
        if warning_list is not None:
            html_attrs["warning"] = [gettext(item) for item in warning_list]
