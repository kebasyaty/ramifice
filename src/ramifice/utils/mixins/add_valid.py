"""Ramifice - AddValidMixin - Contains an abstract method for additional validation of fields."""

__all__ = ("AddValidMixin",)

from abc import ABCMeta


class AddValidMixin(metaclass=ABCMeta):
    """Ramifice - Contains an abstract method for additional validation of fields."""

    async def add_validation(self) -> dict[str, str]:
        """Ramifice - Additional validation of fields."""
        error_map: dict[str, str] = {}
        return error_map
