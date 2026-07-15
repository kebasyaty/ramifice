# Ramifice - ORM-pseudo-like API MongoDB for Python language.
# Copyright (c) 2024 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""The main descriptor class for field types."""

from __future__ import annotations

__all__ = ("Field",)

from typing import Any

from dateutil.parser import parse

from ramifice.translations import Translations


class Field:
    """The main descriptor class for field types.

    Args:
        supported_types (tuple): Tuple of types supported by the `value` parameter.
    """

    def __init__(self, supported_types: tuple) -> None:  # noqa: D107
        self.supported_types = supported_types

    def __set_name__(self, owner: Any, name: str):  # noqa: D105 pyrefly: ignore[unused-parameter]
        self.name = name
        self.internal_name = f"_{name}"
        self.field_name_html_attrs = f"{name}_html_attrs"

    def __get__(self, instance: Any, owner: Any) -> Any | None:  # noqa: D105
        if instance is None:
            msg = f"The field `{self.name}` is not a class variable."
            raise AttributeError(msg)
        return instance.__dict__[self.internal_name]

    def __set__(self, instance: Any, value: Any | None) -> None:  # noqa: D105 pyrefly: ignore[unused-parameter]
        if not isinstance(value, self.supported_types):
            supported_types_list = [
                item.__name__ if item is not type(None) else "None" for item in self.supported_types
            ]
            msg = f"Not а `{' | '.join(supported_types_list)}` type!"
            raise TypeError(msg)

        field_name_html_attrs = self.field_name_html_attrs
        html_attrs = self.html_attrs

        if not hasattr(instance, field_name_html_attrs):
            name = self.name
            html_attrs["id"] = f"id-{name}"
            html_attrs["name"] = name

            label = html_attrs.get("label")
            html_attrs["label"] = Translations._(label) if bool(label) else ""

            placeholder = html_attrs.get("placeholder")
            if placeholder is not None:
                html_attrs["placeholder"] = Translations._(placeholder) if bool(placeholder) else ""

            hint = html_attrs.get("hint")
            html_attrs["hint"] = Translations._(hint) if bool(hint) else ""

            warning_list = html_attrs.get("warning")
            if warning_list is not None:
                html_attrs["warning"] = [Translations._(item) for item in warning_list]

            instance.__dict__[field_name_html_attrs] = html_attrs

        correct_value: Any | None = value
        if html_attrs["group"] == "date" and isinstance(value, str):
            correct_value = parse(value)

        instance.__dict__[self.internal_name] = correct_value
        instance.__dict__[field_name_html_attrs]["value"] = correct_value
