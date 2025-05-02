"""Paladins - Model instance methods."""

from .check import CheckMixin
from .tools import ToolsMixin


class Paladins(CheckMixin, ToolsMixin):
    """Paladins - Model instance methods."""

    def __init__(self):
        super().__init__()
