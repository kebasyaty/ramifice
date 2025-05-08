"""Paladins - Model instance methods."""

from .check import CheckMixin
from .delete import DeleteMixin
from .fixtures import FixtureMixin
from .password import PasswordMixin
from .save import SaveMixin
from .tools import ToolsMixin


class Paladins(
    ToolsMixin, CheckMixin, SaveMixin, PasswordMixin, FixtureMixin, DeleteMixin
):
    """Paladins - Model instance methods."""

    def __init__(self):
        super().__init__()
