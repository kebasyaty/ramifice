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
"""Paladins - Model instance methods.

This module provides:

- `add_validation`: Contains an abstract method for additional validation of fields.
- `check`: Validation of Model data before saving to the database.
- `delete`: Delete document from database.
- `Hooks`: A set of abstract methods for creating hooks.
- `password`: Verification, replacement and recoverang of password.
- `refrash_from_db`: Update Model instance from database.
- `save`: Create or update document in database.
- `Tools`: A set of auxiliary methods.
- `is_valid`: Validation of Model.
- `print_err`: Printing errors to console.
"""

from __future__ import annotations

__all__ = ("QPaladinsMixin",)

from ramifice.paladins.add_valid import AddValidMixin
from ramifice.paladins.check import CheckMixin
from ramifice.paladins.delete import DeleteMixin
from ramifice.paladins.hooks import HooksMixin
from ramifice.paladins.password import PasswordMixin
from ramifice.paladins.refrash import RefrashMixin
from ramifice.paladins.save import SaveMixin
from ramifice.paladins.validation import ValidationMixin


class QPaladinsMixin(  # noqa: RUF067
    CheckMixin,
    SaveMixin,
    PasswordMixin,
    DeleteMixin,
    RefrashMixin,
    ValidationMixin,
    AddValidMixin,
    HooksMixin,
):
    """Paladins - Model instance methods."""

    def __init__(self) -> None:  # noqa: D107
        super().__init__()
