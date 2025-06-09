"""For indexing the Model in the database."""

from abc import ABCMeta


class IndexMixin(metaclass=ABCMeta):
    """For indexing the Model in the database."""

    @classmethod
    async def indexing(cls) -> None:
        """For set up and start indexing."""
