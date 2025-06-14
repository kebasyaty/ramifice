"""Paladins - Model instance methods."""

from .check import CheckMixin
from .delete import DeleteMixin
from .password import PasswordMixin
from .refrash import RefrashMixin
from .save import SaveMixin
from .validation import ValidationMixin


class QPaladinsMixin(
    CheckMixin,
    SaveMixin,
    PasswordMixin,
    DeleteMixin,
    RefrashMixin,
    ValidationMixin,
):
    """Paladins - Model instance methods."""

    def __init__(self) -> None:  # noqa: D107
        super().__init__()
