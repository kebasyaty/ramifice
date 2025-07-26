"""Ramifice - IndexMixin - Contains abstract method for indexing the model in the database."""

__all__ = ("IndexMixin",)

from abc import ABCMeta


class IndexMixin(metaclass=ABCMeta):
    """Ramifice - Contains the method for indexing the model in the database."""

    @classmethod
    async def indexing(cls) -> None:
        """Ramifice - Set up and start indexing."""
