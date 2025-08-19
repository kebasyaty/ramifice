"""Group for checking password fields.

Supported fields: PasswordField
"""

from __future__ import annotations

__all__ = ("PassGroupMixin",)

from typing import Any

from argon2 import PasswordHasher

from ramifice.paladins.tools import accumulate_error, panic_type_error
from ramifice.utils import translations
from ramifice.utils.tools import is_password


class PassGroupMixin:
    """Group for checking password fields.

    Supported fields: PasswordField
    """

    def pass_group(self, params: dict[str, Any]) -> None:
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
                err_msg = translations._("Required field !")
                accumulate_error(err_msg, params)
            if params["is_save"]:
                params["result_map"][field.name] = None
            return
        # Validation Passwor.
        if not is_password(value):
            err_msg = translations._("Invalid Password !")
            accumulate_error(err_msg, params)
            chars = "a-z A-Z 0-9 - . _ ! \" ` ' # % & , : ; < > = @ { } ~ $ ( ) * + / \\ ? [ ] ^ |"
            err_msg = translations._("Valid characters: {}").format(chars)
            accumulate_error(err_msg, params)
            err_msg = translations._("Number of characters: from 8 to 256")
            accumulate_error(err_msg, params)
        # Insert result.
        if params["is_save"]:
            ph = PasswordHasher()
            hash: str = ph.hash(value)
            params["result_map"][field.name] = hash
