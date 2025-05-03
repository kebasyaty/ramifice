"""Paladins - Model instance methods."""

from .check import CheckMixin
from .save import SaveMixin
from .tools import ToolsMixin


class Paladins(ToolsMixin, CheckMixin, SaveMixin):
    """Paladins - Model instance methods."""

    def __init__(self):
        super().__init__()
