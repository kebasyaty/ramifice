# Ramifice - ORM-pseudo-like API MongoDB for Python language.
# Copyright (c) 2024 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""Field of Model.

Type of selective float field with dynamic addition of elements.
"""

from __future__ import annotations

__all__ = ("ChoiceFloatDynField",)

import logging
from typing import Any

from ramifice.utils import constants

logger = logging.getLogger(__name__)


class ChoiceFloatDynField:
    """Field of Model.

    Type of selective integer field with dynamic addition of elements.
    For simulate relationship Many-to-One.
    Element are (add|delete) via `ModelName.unit_manager(unit)` method.

    Args:
        label: Text label for a web form field.
        hide: Hide field from user.
        disabled: Blocks access and modification of the element.
        ignored: If true, the value of this field is not saved in the database.
        hint: An alternative for the `placeholder` parameter.
        warning: Warning information.
        required: Required field.
        readonly: Specifies that the field cannot be modified by the user.
    """

    def __init__(  # noqa: D107
        self,
        label: str = "",
        hide: bool = False,
        disabled: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        required: bool = False,
        readonly: bool = False,
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
                if not isinstance(required, bool):
                    raise AssertionError("Parameter `required` - Not а `bool` type!")
                if not isinstance(readonly, bool):
                    raise AssertionError("Parameter `readonly` - Not а `bool` type!")
            except AssertionError as err:
                logger.critical(str(err))
                raise err

        self.html_attrs: dict[str, Any] = {
            "label": label,
            "value": None,
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
            "choices": None,
            "errors": [],
            "field_type": "ChoiceFloatDynField",
            "group": "choice",
        }

    def __set_name__(self, owner: Any, name: str):  # noqa: D105 pyrefly: ignore[unused-parameter]
        self.name = name
        self.field_html_attrs = f"{name}_html_attrs"

    def __get__(self, instance: Any, owner: Any) -> float | None:  # noqa: D105
        if instance is None:
            msg = f"The field `{self.name}` is not a class variable."
            raise AttributeError(msg)
        return instance.__dict__[self.name]

    def __set__(self, instance: Any, value: float | None) -> None:  # noqa: D105 pyrefly: ignore[unused-parameter]
        if not isinstance(value, (float, type(None))):
            raise TypeError("Not а `float | None` type!")
        if not hasattr(instance, self.field_html_attrs):
            instance.__dict__[self.field_html_attrs]
        instance.__dict__[self.name] = value

    def has_value(self, is_migrate: bool = False) -> bool:
        """Does the field value match the possible options in choices."""
        if is_migrate:
            return True
        value = self.value
        if value is not None:
            choices = self.choices
            if not bool(choices):
                return False
            if value not in [item[0] for item in choices]:  # type: ignore[union-attr]
                return False
        return True
