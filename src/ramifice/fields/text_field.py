# Ramifice - ORM-pseudo-like API MongoDB for Python language.
# Copyright (c) 2024 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""Field of Model for enter text."""

from __future__ import annotations

__all__ = ("TextField",)

import logging
from typing import Any

from ramifice.utils import constants

logger = logging.getLogger(__name__)


class TextField:
    """Field of Model for enter text.

    Agrs:
        label: Text label for a web form field.
        placeholder: Displays prompt text.
        hide: Hide field from user.
        disabled: Blocks access and modification of the element.
        ignored: If true, the value of this field is not saved in the database.
        hint: An alternative for the `placeholder` parameter.
        warning: Warning information.
        textarea: Is it necessary to use the Textarea widget.
        use_editor: Is it necessary to use the widget of the text editor.
        required: Required field.
        readonly: Specifies that the field cannot be modified by the user.
        unique: The unique value of a field in a collection.
        maxlength: The maximum line length.
        multi_language: Is it need support for several languages.
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
        textarea: bool = False,
        use_editor: bool = False,
        required: bool = False,
        readonly: bool = False,
        unique: bool = False,
        maxlength: int = 256,
        # Support for several language.
        multi_language: bool = False,
    ) -> None:
        if constants.DEBUG:
            try:  # noqa: PLW0717
                if not isinstance(maxlength, int):
                    raise AssertionError("Parameter `maxlength` - Not а `int` type!")
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
                if not isinstance(required, bool):
                    raise AssertionError("Parameter `required` - Not а `bool` type!")
                if not isinstance(readonly, bool):
                    raise AssertionError("Parameter `readonly` - Not а `bool` type!")
                if not isinstance(unique, bool):
                    raise AssertionError("Parameter `unique` - Not а `bool` type!")
                if not isinstance(textarea, bool):
                    raise AssertionError("Parameter `textarea` - Not а `bool` type!")
                if not isinstance(use_editor, bool):
                    raise AssertionError("Parameter `use_editor` - Not а `bool` type!")
                if not isinstance(maxlength, int):
                    raise AssertionError("Parameter `maxlength` - Not а `int` type!")
                if not isinstance(multi_language, bool):
                    raise AssertionError("Parameter `multi_language` - Not а `int` type!")
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
            "textarea": textarea,
            "use_editor": use_editor,
            "maxlength": maxlength,
            "multi_language": multi_language,
            "errors": [],
            "field_type": "TextField",
            "group": "text",
        }

    def __len__(self) -> int:
        """Return length of field `value`."""
        value = self.value
        if isinstance(value, str):
            return len(value)
        if isinstance(value, dict):
            count = 0
            for text in value.values():
                tmp = len(text)
                if tmp > count:
                    count = tmp
            return count
        return 0

    def __set_name__(self, owner: Any, name: str):  # noqa: D105 pyrefly: ignore[unused-parameter]
        self.name = name
        self.field_name_html_attrs = f"{name}_html_attrs"

    def __get__(self, instance: Any, owner: Any) -> str | dict[str, str] | None:  # noqa: D105
        if instance is None:
            msg = f"The field `{self.name}` is not a class variable."
            raise AttributeError(msg)
        return instance.__dict__[self.name]

    def __set__(self, instance: Any, value: str | dict[str, str] | None) -> None:  # noqa: D105 pyrefly: ignore[unused-parameter]
        if not isinstance(value, (str, type(None))):
            raise TypeError("Not а `str | dict | None` type!")
        field_name_html_attrs = self.field_name_html_attrs
        if not hasattr(instance, field_name_html_attrs):
            name = self.name
            html_attrs = self.html_attrs
            html_attrs["id"] = f"id-{name}"
            html_attrs["name"] = name
            instance.__dict__[field_name_html_attrs] = html_attrs
        instance.__dict__[self.name] = value
        instance.__dict__[field_name_html_attrs]["value"] = value
