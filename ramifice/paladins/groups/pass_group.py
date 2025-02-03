"""Group for checking password fields.
Supported fields: PasswordField
"""

import hashlib
from typing import Any


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
        value = field.value or field.default
        if value is None:
            if field.required:
                err_msg = "Required field !"
                self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
            if params["is_save"]:
                params["result_map"][field.name] = None
            return
        # Validation Passwor.
        if not field.is_valid(value):
            err_msg = "Invalid Passwor !"
            self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
        # Insert result.
        if params["is_save"]:
            password = value.encode("utf-8")
            _hash = hashlib.sha256(password)
            _hash.update(password)
            params["result_map"][field.name] = _hash.digest()
