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
"""Validation of Model and printing errors to console."""

from __future__ import annotations

__all__ = ("ValidationMixin",)

from typing import Any

from termcolor import colored


class ValidationMixin:
    """Validation of Model and printing errors to console."""

    async def is_valid(self) -> bool:
        """Check data validity.

        The main use is to check data from web forms.
        It is also used to verify Models that do not migrate to the database.
        """
        result_check: dict[str, Any] = await self.check()
        return result_check["is_valid"]

    def print_err(self) -> None:
        """Printing errors to console.

        Convenient to use during development.
        """
        is_err: bool = False
        for field_name, field_data in self.__dict__.items():
            if callable(field_data):
                continue
            if len(field_data.errors) > 0:
                # title
                if not is_err:
                    print(colored("\nERRORS:", "red", attrs=["bold"]))  # ruff:ignore[print]
                    print(colored("Model: ", "blue", attrs=["bold"]), end="")  # ruff:ignore[print]
                    print(colored(f"`{self.full_model_name()}`", "blue"))  # ruff:ignore[print]
                    is_err = True
                # field name
                print(colored("Field: ", "green", attrs=["bold"]), end="")  # ruff:ignore[print]
                print(colored(f"`{field_name}`:", "green"))  # ruff:ignore[print]
                # error messages
                print(colored("\n".join(field_data.errors), "red"))  # ruff:ignore[print]
        if len(self._id.alerts) > 0:
            # title
            print(colored("AlERTS:", "yellow", attrs=["bold"]))  # ruff:ignore[print]
            # messages
            print(colored("\n".join(self._id.alerts), "yellow"), end="\n\n")  # ruff:ignore[print]
        else:
            print(end="\n\n")  # ruff:ignore[print]
