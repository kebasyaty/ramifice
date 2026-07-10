# Ramifice - ORM-pseudo-like API MongoDB for Python language.
# Copyright (c) 2024 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""Field of Model for enter boolean value."""

from __future__ import annotations

__all__ = ("BooleanField",)

import logging
from typing import Any

from ramifice.utils import constants

logger = logging.getLogger(__name__)


class BooleanField:
    """Field of Model for enter boolean value.

    Args:
        label: Text label for a web form field.
        default: Default value.
        hide: Hide field from user.
        disabled: Blocks access and modification of the element.
        ignored: If true, the value of this field is not saved in the database.
        hint: An alternative for the `placeholder` parameter.
        warning: Warning information.
    """

    def __init__(  # noqa: D107
        self,
        label: str = "",
        default: bool = False,
        hide: bool = False,
        disabled: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
    ) -> None:
        if constants.DEBUG:
            try:  # noqa: PLW0717
                if default is not None and not isinstance(default, bool):
                    raise AssertionError("Parameter `default` - Not а `bool` type!")
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
            except AssertionError as err:
                logger.critical(str(err))
                raise err

        self.html_attrs: dict[str, Any] = {
            "label": label,
            "input_type": "checkbox",
            "value": None,
            "default": default,
            "hide": hide,
            "disabled": disabled,
            "ignored": ignored,
            "hint": hint,
            "warning": warning,
            "errors": [],
            "field_type": "BooleanField",
            "group": "bool",
        }

    def __set_name__(self, owner: Any, name: str):  # noqa: D105 pyrefly: ignore[unused-parameter]
        self.name = name
        self.field_html_attrs = f"{name}_html_attrs"

    def __get__(self, instance: Any, owner: Any) -> bool | None:  # noqa: D105
        if instance is None:
            msg = f"The field `{self.name}` is not a class variable."
            raise AttributeError(msg)
        return instance.__dict__[self.name]

    def __set__(self, instance: Any, value: bool | None) -> None:  # noqa: D105 pyrefly: ignore[unused-parameter]
        if not isinstance(value, (bool, type(None))):
            raise TypeError("Not а `bool | None` type!")
        if not hasattr(instance, self.field_html_attrs):
            instance.__dict__[self.field_html_attrs]
        instance.__dict__[self.name] = value
