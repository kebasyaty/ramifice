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
"""Field of Model.

Type of selective float field with static of elements.
"""

from __future__ import annotations

__all__ = ("ChoiceFloatMultField",)

import logging
from typing import Any

from ramifice.config import Config
from ramifice.fields.field import Field

logger = logging.getLogger(__name__)


class ChoiceFloatMultField(Field):
    """Field of Model.

    Type of selective float field with static of elements.
    With multiple choice.

    Args:
        label: Text label for a web form field.
        default: Default value.
        hide: Hide field from user.
        disabled: Blocks access and modification of the element.
        ignored: If true, the value of this field is not saved in the database.
        hint: An alternative for the `placeholder` parameter.
        warning: Warning information.
        required: Required field.
        readonly: Specifies that the field cannot be modified by the user.
        choices: For a predefined set of options - [[value, Title], ...].
    """

    def __init__(  # noqa: D107
        self,
        label: str = "",
        default: list[float] | None = None,
        hide: bool = False,
        disabled: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] = [],  # noqa: B006
        required: bool = False,
        readonly: bool = False,
        choices: list[list[float | str]] | None = None,  # [[value, Title], ...]
    ) -> None:

        Field.__init__(self, supported_types=(list, type(None)))

        self.html_attrs: dict[str, Any] = {
            "id": "",
            "name": "",
            "label": label,
            "value": None,
            "default": default,
            "hide": hide,
            "disabled": disabled,
            "ignored": ignored,
            "hint": hint,
            "warning": warning,
            "required": required,
            "readonly": readonly,
            "unique": False,
            "multiple": True,
            "choices": choices,
            "errors": [],
            "field_type": "ChoiceFloatMultField",
            "group": "choice",
        }

        if Config.DEBUG:
            try:  # noqa: PLW0717
                if choices is not None:
                    if not isinstance(choices, list):
                        raise AssertionError("Parameter `choices` - Not а `list` type!")
                    if len(choices) == 0:
                        raise AssertionError("The `choices` parameter should not contain an empty list!")
                if default is not None:
                    if not isinstance(default, list):
                        raise AssertionError("Parameter `default` - Not а `list` type!")
                    if len(default) == 0:
                        raise AssertionError("The `default` parameter should not contain an empty list!")
                    if choices is not None and not self.has_value():
                        raise AssertionError(
                            "Parameter `default` does not coincide with " + "list of permissive values in `choicees`.",
                        )
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
                if not isinstance(required, bool):
                    raise AssertionError("Parameter `required` - Not а `bool` type!")
                if not isinstance(readonly, bool):
                    raise AssertionError("Parameter `readonly` - Not а `bool` type!")
            except AssertionError as err:
                logger.critical(str(err))
                raise err

    def has_value(self, is_migrate: bool = False) -> bool:
        """Does the field value match the possible options in choices."""
        value = self.html_attrs["value"]
        if value is None:
            value = self.html_attrs["default"]
        if value is not None:
            choices = self.html_attrs["choices"]
            if len(value) == 0 or not bool(choices):
                return False
            value_list = [item[0] for item in choices]  # type: ignore[union-attr]
            for item in value:
                if item not in value_list:
                    return False
        return True
