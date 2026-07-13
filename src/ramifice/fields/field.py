# Ramifice - ORM-pseudo-like API MongoDB for Python language.
# Copyright (c) 2024 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""The main descriptor class for field types."""

from __future__ import annotations

__all__ = ("Field",)

from typing import Any

from ramifice.translations import Translations as trans


class Field:
    """The main descriptor class for field types.

    Args:
        supported_types (tuple): Tuple of types supported by the `value` parameter.
    """

    def __init__(self, supported_types: tuple) -> None:  # noqa: D107
        self.supported_types = supported_types

    def __set_name__(self, owner: Any, name: str):  # noqa: D105 pyrefly: ignore[unused-parameter]
        self.name = name
        self.field_name_html_attrs = f"{name}_html_attrs"

    def __get__(self, instance: Any, owner: Any) -> Any | None:  # noqa: D105
        if instance is None:
            msg = f"The field `{self.name}` is not a class variable."
            raise AttributeError(msg)
        return instance.__dict__[self.name]

    def __set__(self, instance: Any, value: Any | None) -> None:  # noqa: D105 pyrefly: ignore[unused-parameter]
        if not isinstance(value, self.supported_types):
            supported_types_list = [
                item.__name__ if item is not type(None) else "None" for item in self.supported_types
            ]
            msg = f"Not а `{' | '.join(supported_types_list)}` type!"
            raise TypeError(msg)
        name = self.name
        field_name_html_attrs = self.field_name_html_attrs
        if not hasattr(instance, field_name_html_attrs):
            html_attrs = self.html_attrs
            html_attrs["id"] = f"id-{name}"
            html_attrs["name"] = name
            html_attrs["label"] = trans._(html_attrs.get("label", ""))
            html_attrs["placeholder"] = trans._(html_attrs.get("placeholder", ""))
            html_attrs["hint"] = trans._(html_attrs.get("hint", ""))
            instance.__dict__[field_name_html_attrs] = html_attrs
        instance.__dict__[name] = value
        instance.__dict__[field_name_html_attrs]["value"] = value
