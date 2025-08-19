"""Paladins - Model instance methods.

This module provides:

- `add_validation`: Contains an abstract method for additional validation of fields.
- `check`: Validation of Model data before saving to the database.
- `delete`: Delete document from database.
- `Hooks`: A set of abstract methods for creating hooks.
- `indexing`: Contains the method for indexing the model in the database.
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
from ramifice.paladins.indexing import IndexMixin
from ramifice.paladins.password import PasswordMixin
from ramifice.paladins.refrash import RefrashMixin
from ramifice.paladins.save import SaveMixin
from ramifice.paladins.validation import ValidationMixin


class QPaladinsMixin(
    CheckMixin,
    SaveMixin,
    PasswordMixin,
    DeleteMixin,
    RefrashMixin,
    ValidationMixin,
    AddValidMixin,
    HooksMixin,
    IndexMixin,
):
    """Paladins - Model instance methods."""

    def __init__(self) -> None:  # noqa: D107
        super().__init__()
