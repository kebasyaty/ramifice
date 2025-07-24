"""AddValidMixin - Contains an abstract method for additional validation of fields."""

__all__ = ("AddValidMixin",)

from abc import ABCMeta


class AddValidMixin(metaclass=ABCMeta):
    """Contains an abstract method for additional validation of fields."""

    async def add_validation(self) -> dict[str, str]:
        """Additional validation of fields."""
        error_map: dict[str, str] = {}
        return error_map
