"""Commons - Model class methods."""

from .general import GeneralMixin
from .tools import ToolsMixin


class Commons(ToolsMixin, GeneralMixin):
    """Commons - Model class methods."""

    def __init__(self):
        super().__init__()
