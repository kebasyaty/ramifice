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
"""Group for checking password fields.

Supported fields: PasswordField
"""

from __future__ import annotations

__all__ = ("PasswordGroupMixin",)

from typing import Any

from argon2 import PasswordHasher

from ramifice.paladins.utils import accumulate_error
from ramifice.utils import is_password


class PasswordGroupMixin:
    """Group for checking password fields.

    Supported fields: PasswordField
    """

    def password_group(self, params: dict[str, Any]) -> None:
        """Checking password fields."""
        _ = params["_"]
        f__core = params["field_core"]
        f_name = f__core.name
        # When updating the document, skip the verification.
        if params["is_update"]:
            setattr(self, f_name, None)
            return
        # Get current value.
        f_value = f__core.value or None

        if f_value is None:
            if f__core.is_require:
                err_msg = _("Required field !")
                accumulate_error(err_msg, params)
            if params["is_save"]:
                params["result_map"][f_name] = None
            return
        # Validation Passwor.
        if not is_password(f_value):
            err_msg = _("Invalid Password !")
            accumulate_error(err_msg, params)
            chars = "a-z A-Z 0-9 - . _ ! \" ` ' # % & , : ; < > = @ { } ~ $ ( ) * + / \\ ? [ ] ^ |"
            err_msg = _("Valid characters: {}").format(chars)
            accumulate_error(err_msg, params)
            err_msg = _("Number of characters: from 8 to 256")
            accumulate_error(err_msg, params)
        # Insert result.
        if params["is_save"]:
            ph = PasswordHasher()
            hash: str = ph.hash(f_value)
            params["result_map"][f_name] = hash
