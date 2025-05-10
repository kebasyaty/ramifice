"""Commons - Model class methods."""

from .general import GeneralMixin
from .tools import ToolMixin


class Commons(ToolMixin, GeneralMixin):
    """Commons - Model class methods."""

    def __init__(self):
        super().__init__()
