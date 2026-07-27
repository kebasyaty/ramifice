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
"""Unit - Data management in dynamic fields."""

from __future__ import annotations

__all__ = ("Unit",)

import logging
from collections.abc import Callable
from typing import Any

from ramifice.errors import PanicError

logger = logging.getLogger(__name__)


class Unit:
    """Unit of information for `choices` parameter in dynamic field types.

    Args:
        field: The name of the dynamic field.
        title: The name of the choice item.
        value: The value of the choice item.
        is_delete: True - if you need to remove the item of choice.
    """

    def __init__(  # ruff:ignore[undocumented-public-init]
        self,
        field: str,
        title: dict[str, str],  # Example: {"en": "Title", "ru": "Заголовок"}
        value: float | int | str,
        is_delete: bool = False,
    ) -> None:
        # Check the match of types.
        if not isinstance(field, str):
            err_msg = "Class: `Unit` > Field: `field` => Not а `str` type!"
            raise PanicError(err_msg)
        if not isinstance(title, dict):
            err_msg = (
                "Class: `Unit` > Field: `title` => Not а `str` type! " + 'Example: {"en": "Title", "ru": "Заголовок"}'
            )
            raise PanicError(err_msg)
        if not isinstance(value, (float, int, str)):
            err_msg = "Class: `Unit` > Field: `value` => Not a `float | int | str` type!"
            raise PanicError(err_msg)
        if not isinstance(is_delete, bool):
            err_msg = "Class: `Unit` > Field: `is_delete` => Not a `bool` type!"
            raise PanicError(err_msg)

        self.field = field
        self.title = title
        self.value = value
        self.is_delete = is_delete

        self.check_empty_arguments()

    def check_empty_arguments(self) -> None:
        """Check the arguments (field|title|value) for empty values.

        Returns:
            `None`

        Raises:
            Raised exception `PanicError` if argument (field|title|value) of Unit is empty.
        """
        field_name: str = ""

        if len(self.field) == 0:
            field_name = "field"
        elif len(self.title) == 0:
            field_name = "title"
        elif isinstance(self.value, str) and len(self.value) == 0:
            field_name = "value"

        if len(field_name) > 0:
            err_msg = (
                "Method: `unit_manager` > "
                + "Argument: `unit` > "
                + f"Field: `{field_name}` => "
                + "Must not be empty!"
            )
            logger.critical(err_msg)
            raise PanicError(err_msg)

    def to_dict(self) -> dict[str, Any]:
        """Convert Unit instance to a dictionary."""
        unit_dict: dict[str, Any] = {}
        for key, value in self.__dict__.items():
            if not isinstance(value, Callable):
                unit_dict[key] = value
        return unit_dict
