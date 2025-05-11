"""Commons - Model class methods."""

from .general import GeneralMixin
from .tools import ToolMixin
from .one import OneMixin


class Commons(ToolMixin, GeneralMixin, OneMixin):
    """Commons - Model class methods."""

    def __init__(self):
        super().__init__()
