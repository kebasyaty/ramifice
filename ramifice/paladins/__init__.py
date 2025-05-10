"""Paladins - Model instance methods."""

from .check import CheckMixin
from .delete import DeleteMixin
from .password import PasswordMixin
from .save import SaveMixin
from .tools import ToolMixin


class Paladins(ToolMixin, CheckMixin, SaveMixin, PasswordMixin, DeleteMixin):
    """Paladins - Model instance methods."""

    def __init__(self):
        super().__init__()
