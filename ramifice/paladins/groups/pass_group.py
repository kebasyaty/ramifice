"""Group for checking password fields.
Supported fields: PasswordField
"""

from typing import Any

from argon2 import PasswordHasher

from ... import translations


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
        if value is None:
            if field.required:
                err_msg = translations.gettext("Required field !")
                self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
            if params["is_save"]:
                params["result_map"][field.name] = None
            return
        # Validation Passwor.
        if not field.is_valid(value):
            err_msg = translations.gettext("Invalid Password !")
            self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
            err_msg = translations.gettext("Valid characters: {chars}").format(
                char="a-z A-Z 0-9 - . _ ! \" ` ' # % & , : ; < > = @ { } ~ $ ( ) * + / \\ ? [ ] ^ |"
            )
            self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
            err_msg = translations.gettext(
                "Number of characters: from {min_num} to {max_num}"
            ).format(min_num=8, max_num=256)
            self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
        # Insert result.
        if params["is_save"]:
            ph = PasswordHasher()
            hash: str = ph.hash(value)
            params["result_map"][field.name] = hash
