"""Commons - Model class methods."""

from .general import GeneralMixin
from .many import ManyMixin
from .one import OneMixin
from .tools import ToolMixin


class Commons(ToolMixin, GeneralMixin, OneMixin, ManyMixin):
    """Commons - Model class methods."""

    def __init__(self):
        super().__init__()
