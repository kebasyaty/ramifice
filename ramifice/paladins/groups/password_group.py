"""Group for checking password fields.
Supported fields: PasswordField
"""

from typing import Any


class PasswordGroupMixin:
    """Group for checking password fields.
    Supported fields: PasswordField
    """

    def password_group(self, params: dict[str, Any]) -> None:
        """Checking password fields."""
