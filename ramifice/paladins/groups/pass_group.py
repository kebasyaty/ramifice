"""Group for checking password fields.
Supported fields: PasswordField
"""

from typing import Any


class PassGroupMixin:
    """Group for checking password fields.
    Supported fields: PasswordField
    """

    def pass_group(self, params: dict[str, Any]) -> None:
        """Checking password fields."""
