# Ramifice - ORM-pseudo-like API MongoDB for Python language.
# Copyright (c) 2024 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""Group for checking password fields.

Supported fields: PasswordField
"""

from __future__ import annotations

__all__ = ("PasswordGroupMixin",)

from typing import Any

from argon2 import PasswordHasher

from ramifice.paladins.utils import accumulate_error, panic_type_error
from ramifice.translations import Translations
from ramifice.utils import is_password


class PasswordGroupMixin:
    """Group for checking password fields.

    Supported fields: PasswordField
    """

    def password_group(self, params: dict[str, Any]) -> None:
        """Checking password fields."""
        field = params["field_data"]
        # When updating the document, skip the verification.
        if params["is_update"]:
            params["field_data"].value = None
            return
        # Get current value.
        value = field.value or None

        if not isinstance(value, (str, type(None))):
            panic_type_error("str | None", params)

        if value is None:
            if field.required:
                err_msg = Translations._("Required field !")
                accumulate_error(err_msg, params)
            if params["is_save"]:
                params["result_map"][field.name] = None
            return
        # Validation Passwor.
        if not is_password(value):
            err_msg = Translations._("Invalid Password !")
            accumulate_error(err_msg, params)
            chars = "a-z A-Z 0-9 - . _ ! \" ` ' # % & , : ; < > = @ { } ~ $ ( ) * + / \\ ? [ ] ^ |"
            err_msg = Translations._("Valid characters: {}").format(chars)
            accumulate_error(err_msg, params)
            err_msg = Translations._("Number of characters: from 8 to 256")
            accumulate_error(err_msg, params)
        # Insert result.
        if params["is_save"]:
            ph = PasswordHasher()
            hash: str = ph.hash(value)
            params["result_map"][field.name] = hash
