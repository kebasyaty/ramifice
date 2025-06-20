"""IndexMixin - Contains abstract method for indexing the model in the database."""

from abc import ABCMeta


class IndexMixin(metaclass=ABCMeta):
    """Contains the method for indexing the model in the database."""

    @classmethod
    async def indexing(cls) -> None:
        """For set up and start indexing."""
