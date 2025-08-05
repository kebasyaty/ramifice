"""AddValidMixin - Contains an abstract method for additional validation of fields."""

__all__ = ("AddValidMixin",)

from abc import ABCMeta

from xloft import NamedTuple


class AddValidMixin(metaclass=ABCMeta):
    """Contains an abstract method for additional validation of fields."""

    async def add_validation(self) -> NamedTuple:
        """Additional validation of fields."""
        return NamedTuple()
