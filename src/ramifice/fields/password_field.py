# Ramifice - ORM-pseudo-like API MongoDB for Python language.
# Copyright (c) 2024 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""Field of Model for enter password."""

from __future__ import annotations

__all__ = ("PasswordField",)

import logging
from typing import Any

import orjson

from ramifice.utils import constants

logger = logging.getLogger(__name__)


class PasswordField:
    r"""Field of Model for enter password.

    Attention:
        - `Regular expression:` ^[-._!"`'#%&,:;<>=@{}~$()*+/\\?[]^|a-zA-Z0-9]{8,256}$
        - `Valid characters:` a-z A-Z 0-9 - . _ ! " ` ' # % & , : ; < > = @ { } ~ $ ( ) * + / \\ ? [ ] ^ |
        - `Number of characters:` from 8 to 256.

    Agrs:
        label: Text label for a web form field.
        placeholder: Displays prompt text.
        hide: Hide field from user.
        ignored: If true, the value of this field is not saved in the database.
        hint: An alternative for the `placeholder` parameter.
        warning: Warning information.
        required: Required field.
    """

    def __init__(  # noqa: D107
        self,
        label: str = "",
        placeholder: str = "",
        hide: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        required: bool = False,
    ) -> None:
        if constants.DEBUG:
            try:  # noqa: PLW0717
                if not isinstance(label, str):
                    raise AssertionError("Parameter `default` - Not а `str` type!")
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
                if not isinstance(required, bool):
                    raise AssertionError("Parameter `required` - Not а `bool` type!")
            except AssertionError as err:
                logger.critical(str(err))
                raise err

        self.html_attrs: dict[str, Any] = {
            "label": label,
            "input_type": "password",
            "value": None,
            "placeholder": placeholder,
            "hide": hide,
            "ignored": ignored,
            "hint": hint,
            "warning": warning,
            "required": required,
            "errors": [],
            "field_type": "PasswordField",
            "group": "password",
        }

    def __set_name__(self, owner: Any, name: str):  # noqa: D105 pyrefly: ignore[unused-parameter]
        self.name = name
        self.field_html_attrs = f"{name}_html_attrs"

    def __get__(self, instance: Any, owner: Any) -> str:  # noqa: D105
        if instance is None:
            msg = f"The field `{self.name}` is not a class variable."
            raise AttributeError(msg)
        return instance.__dict__[self.name]

    def __set__(self, instance: Any, value: str) -> None:  # noqa: D105 pyrefly: ignore[unused-parameter]
        if not isinstance(value, (str, type(None))):
            raise TypeError("Not а `str` type!")
        if not hasattr(instance, self.field_html_attrs):
            instance.__dict__[self.field_html_attrs] = self.html_attrs
        instance.__dict__[self.name] = value

    def to_dict(self) -> dict[str, Any]:
        """Convert object instance to a dictionary."""
        json_dict: dict[str, Any] = {}
        for name, data in self.__dict__.items():
            if not callable(data):
                json_dict[name] = data if name != "value" else None
        return json_dict

    def to_json(self) -> str:
        """Convert object instance to a JSON string."""
        return orjson.dumps(self.to_dict()).decode("utf-8")

    @classmethod
    def from_dict(cls, json_dict: dict[str, Any]) -> Any:
        """Convert JSON string to a object instance."""
        obj = cls()
        for name, data in json_dict.items():
            obj.__dict__[name] = data
        return obj

    @classmethod
    def from_json(cls, json_str: str) -> Any:
        """Convert JSON string to a object instance."""
        json_dict = orjson.loads(json_str)
        return cls.from_dict(json_dict)
