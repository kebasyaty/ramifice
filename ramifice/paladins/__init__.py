"""Paladins - Model instance methods."""

from .check import CheckMixin
from .fixtures import FixtureMixin
from .save import SaveMixin
from .tools import ToolsMixin


class Paladins(ToolsMixin, CheckMixin, SaveMixin, FixtureMixin):
    """Paladins - Model instance methods."""

    def __init__(self):
        super().__init__()
