# Ramifice - ORM-pseudo-like API MongoDB for Python language.
# Copyright (c) 2024 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""Field of Model for automatic generation of string `slug`."""

from __future__ import annotations

__all__ = ("SlugField",)

import logging
from typing import Any

from ramifice.utils import constants

logger = logging.getLogger(__name__)


class SlugField:
    """Field of Model for automatic generation of string `slug`.

    Convenient to use for Url addresses.

    Agrs:
        label: Text label for a web form field.
        placeholder: Displays prompt text.
        hide: Hide field from user.
        disabled: Blocks access and modification of the element.
        ignored: If true, the value of this field is not saved in the database.
        hint: An alternative for the `placeholder` parameter.
        warning: Warning information.
        readonly: Specifies that the field cannot be modified by the user.
        slug_sources: List of sources fields.
    """

    def __init__(  # noqa: D107
        self,
        label: str = "",
        placeholder: str = "",
        hide: bool = False,
        disabled: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        readonly: bool = False,
        slug_sources: list[str] = ["_id"],  # noqa: B006
    ) -> None:
        if constants.DEBUG:
            try:  # noqa: PLW0717
                if not isinstance(label, str):
                    raise AssertionError("Parameter `default` - Not а `str` type!")
                if not isinstance(disabled, bool):
                    raise AssertionError("Parameter `disabled` - Not а `bool` type!")
                if not isinstance(hide, bool):
                    raise AssertionError("Parameter `hide` - Not а `bool` type!")
                if not isinstance(ignored, bool):
                    raise AssertionError("Parameter `ignored` - Not а `bool` type!")
                if not isinstance(ignored, bool):
                    raise AssertionError("Parameter `ignored` - Not а `bool` type!")
                if not isinstance(hint, str):
                    raise AssertionError("Parameter `hint` - Not а `str` type!")
                if warning is not None and not isinstance(warning, list):
                    raise AssertionError("Parameter `warning` - Not а `list` type!")
                if not isinstance(placeholder, str):
                    raise AssertionError("Parameter `placeholder` - Not а `str` type!")
                if not isinstance(readonly, bool):
                    raise AssertionError("Parameter `readonly` - Not а `bool` type!")
                if not isinstance(slug_sources, list):
                    raise AssertionError("Parameter `slug_sources` - Not а `list` type!")
            except AssertionError as err:
                logger.critical(str(err))
                raise err

        self.html_attrs: dict[str, Any] = {
            "label": label,
            "input_type": "text",
            "value": None,
            "placeholder": placeholder,
            "hide": hide,
            "disabled": disabled,
            "ignored": ignored,
            "hint": hint,
            "warning": warning,
            "required": False,
            "readonly": readonly,
            "unique": True,
            "slug_sources": slug_sources,
            "errors": [],
            "field_type": "SlugField",
            "group": "slug",
        }

    def __set_name__(self, owner: Any, name: str):  # noqa: D105 pyrefly: ignore[unused-parameter]
        self.name = name
        self.field_html_attrs = f"{name}_html_attrs"

    def __get__(self, instance: Any, owner: Any) -> str | None:  # noqa: D105
        if instance is None:
            msg = f"The field `{self.name}` is not a class variable."
            raise AttributeError(msg)
        return instance.__dict__[self.name]

    def __set__(self, instance: Any, value: str | None) -> None:  # noqa: D105 pyrefly: ignore[unused-parameter]
        if not isinstance(value, (str, type(None))):
            raise TypeError("Not а `str | None` type!")
        if not hasattr(instance, self.field_html_attrs):
            instance.__dict__[self.field_html_attrs] = self.html_attrs
        instance.__dict__[self.name] = value
