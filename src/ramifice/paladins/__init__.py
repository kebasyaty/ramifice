"""Paladins - Model instance methods."""

from .check import CheckMixin
from .delete import DeleteMixin
from .password import PasswordMixin
from .refrash import RefrashMixin
from .save import SaveMixin
from .tools import ToolMixin


class QPaladinsMixin(
    ToolMixin,
    CheckMixin,
    SaveMixin,
    PasswordMixin,
    DeleteMixin,
    RefrashMixin,
):
    """Paladins - Model instance methods."""

    def __init__(self):
        super().__init__()
