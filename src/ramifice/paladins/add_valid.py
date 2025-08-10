"""AddValidMixin - Contains an abstract method for additional validation of fields."""

__all__ = ("AddValidMixin",)

from abc import abstractmethod

from xloft import NamedTuple


class AddValidMixin:
    """Contains an abstract method for additional validation of fields."""

    @abstractmethod
    async def add_validation(self) -> NamedTuple:
        """Additional validation of fields."""
        return NamedTuple()
