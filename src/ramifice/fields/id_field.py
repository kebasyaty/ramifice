# Ramifice - ORM-pseudo-like API MongoDB for Python language.
# Copyright (c) 2024 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""Field of Model for enter identifier of document."""

from __future__ import annotations

__all__ = ("IDField",)

import logging
from typing import Any

import orjson
from bson.objectid import ObjectId

from ramifice.config import Config
from ramifice.translations import Translations

logger = logging.getLogger(__name__)


class IDField:
    """Field of Model for enter identifier of document.

    Agrs:
        label: Text label for a web form field.
        placeholder: Displays prompt text.
        hide: Hide field from user.
        disabled: Blocks access and modification of the element.
        ignored: If true, the value of this field is not saved in the database.
        hint: An alternative for the `placeholder` parameter.
        warning: Warning information.
        required: Required field.
        readonly: Specifies that the field cannot be modified by the user.
        unique: The unique value of a field in a collection.
    """

    def __init__(  # noqa: D107
        self,
        label: str = "",
        placeholder: str = "",
        hide: bool = False,
        disabled: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] = [],  # noqa: B006
        required: bool = False,
        readonly: bool = False,
        unique: bool = False,
    ) -> None:
        if Config.DEBUG:
            try:  # noqa: PLW0717
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
                if not isinstance(unique, bool):
                    raise AssertionError("Parameter `unique` - Not а `bool` type!")
            except AssertionError as err:
                logger.critical(str(err))
                raise err

        self.html_attrs: dict[str, Any] = {
            "id": "",
            "name": "",
            "label": label,
            "input_type": "text",
            "value": None,
            "placeholder": placeholder,
            "hide": hide,
            "disabled": disabled,
            "ignored": ignored,
            "hint": hint,
            "warning": warning,
            "required": required,
            "readonly": readonly,
            "unique": unique,
            "alerts": [],
            "errors": [],
            "field_type": "IDField",
            "group": "id",
        }

    def __set_name__(self, owner: Any, name: str):  # noqa: D105 pyrefly: ignore[unused-parameter]
        self.name = name
        self.internal_name = f"_{name}"
        self.field_name_html_attrs = f"{name}_html_attrs"

    def __get__(self, instance: Any, owner: Any) -> ObjectId | None:  # noqa: D105
        if instance is None:
            msg = f"The field `{self.name}` is not a class variable."
            raise AttributeError(msg)
        return instance.__dict__[self.internal_name]

    def __set__(self, instance: Any, value: ObjectId | None) -> None:  # noqa: D105 pyrefly: ignore[unused-parameter]
        if not isinstance(value, (ObjectId, type(None))):
            raise TypeError("Not а `ObjectId | None` type!")
        name = self.name
        field_name_html_attrs = self.field_name_html_attrs
        if not hasattr(instance, field_name_html_attrs):
            html_attrs = self.html_attrs
            html_attrs["id"] = f"id-{name}"
            html_attrs["name"] = name
            html_attrs["label"] = Translations._(html_attrs["label"])
            html_attrs["placeholder"] = Translations._(html_attrs["placeholder"])
            html_attrs["hint"] = Translations._(html_attrs["hint"])
            html_attrs["warning"] = [Translations._(item) for item in html_attrs["warning"]]
            instance.__dict__[field_name_html_attrs] = html_attrs
        instance.__dict__[self.internal_name] = value
        instance.__dict__[field_name_html_attrs]["value"] = value

    def to_dict(self) -> dict[str, Any]:
        """Convert object instance to a dictionary."""
        json_dict: dict[str, Any] = {}
        for name, data in self.__dict__.items():
            if not callable(data):
                if name == "value" and data is not None:
                    json_dict[name] = str(data)
                else:
                    json_dict[name] = data
        return json_dict

    def to_json(self) -> str:
        """Convert object instance to a JSON string."""
        return orjson.dumps(self.to_dict()).decode("utf-8")

    @classmethod
    def from_dict(cls, json_dict: dict[str, Any]) -> Any:
        """Convert JSON string to a object instance."""
        obj = cls()
        for name, data in json_dict.items():
            if name == "value" and data is not None:
                obj.__dict__[name] = ObjectId(data)
            else:
                obj.__dict__[name] = data
        return obj

    @classmethod
    def from_json(cls, json_str: str) -> Any:
        """Convert JSON string to a object instance."""
        json_dict = orjson.loads(json_str)
        return cls.from_dict(json_dict)
