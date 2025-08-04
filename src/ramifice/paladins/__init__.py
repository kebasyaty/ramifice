"""Ramifice - Paladins - Model instance methods."""

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
    """Ramifice - Paladins - Model instance methods."""

    def __init__(self) -> None:  # noqa: D107
        super().__init__()
