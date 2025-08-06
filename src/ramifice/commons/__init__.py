"""Commons - Model class methods."""

__all__ = ("QCommonsMixin",)

from ramifice.commons.general import GeneralMixin
from ramifice.commons.indexes import IndexMixin
from ramifice.commons.many import ManyMixin
from ramifice.commons.one import OneMixin
from ramifice.commons.unit_manager import UnitMixin


class QCommonsMixin(
    GeneralMixin,
    OneMixin,
    ManyMixin,
    IndexMixin,
    UnitMixin,
):
    """Commons - Model class methods."""

    def __init__(self) -> None:  # noqd: D107
        super().__init__()
