# Ramifice - ORM-pseudo-like API MongoDB for Python language.
# Copyright (c) 2024 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""Field of Model.

Type of selective text field with static of elements.
"""

from __future__ import annotations

__all__ = ("ChoiceTextField",)

import logging
from typing import Any

from ramifice.utils import constants

logger = logging.getLogger(__name__)


class ChoiceTextField:
    """Field of Model.

    Type of selective text field with static of elements.
    With a single choice.

    Args:
        label: Text label for a web form field.
        default: Default value.
        hide: Hide field from user.
        disabled: Blocks access and modification of the element.
        required: Required field.
        readonly: Specifies that the field cannot be modified by the user.
        ignored: If true, the value of this field is not saved in the database.
        hint: An alternative for the `placeholder` parameter.
        warning: Warning information.
        choices: For a predefined set of options - [[value, Title], ...].
    """

    def __init__(  # noqa: D107
        self,
        label: str = "",
        default: str | None = None,
        hide: bool = False,
        disabled: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        required: bool = False,
        readonly: bool = False,
        choices: list[list[str]] | None = None,  # [[value, Title], ...]
    ) -> None:

        self.html_attrs: dict[str, Any] = {
            "id": "",
            "name": "",
            "label": label,
            "value": None,
            "default": default,
            "placeholder": "",
            "hide": hide,
            "disabled": disabled,
            "ignored": ignored,
            "hint": hint,
            "warning": warning,
            "required": required,
            "readonly": readonly,
            "unique": False,
            "multiple": False,
            "choices": choices,
            "errors": [],
            "field_type": "ChoiceTextField",
            "group": "choice",
        }

        if constants.DEBUG:
            try:  # noqa: PLW0717
                if choices is not None:
                    if not isinstance(choices, list):
                        raise AssertionError("Parameter `choices` - Not а `list` type!")
                    if len(choices) == 0:
                        raise AssertionError("The `choices` parameter should not contain an empty list!")
                if default is not None:
                    if not isinstance(default, str):
                        raise AssertionError("Parameter `default` - Not а `str` type!")
                    if len(default) == 0:
                        raise AssertionError("The `default` parameter should not contain an empty string!")
                    if choices is not None and not self.has_value():
                        raise AssertionError(
                            "Parameter `default` does not coincide with " + "list of permissive values in `choicees`.",
                        )
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
                if not isinstance(required, bool):
                    raise AssertionError("Parameter `required` - Not а `bool` type!")
                if not isinstance(readonly, bool):
                    raise AssertionError("Parameter `readonly` - Not а `bool` type!")
            except AssertionError as err:
                logger.critical(str(err))
                raise err

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

    def has_value(self, is_migrate: bool = False) -> bool:
        """Does the field value match the possible options in choices."""
        value = self.value
        if value is None:
            value = self.default
        if value is not None:
            choices = self.choices
            if not bool(choices):
                return False
            if value not in [item[0] for item in choices]:  # type: ignore[union-attr]
                return False
        return True
