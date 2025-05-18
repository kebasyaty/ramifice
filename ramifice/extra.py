"""Hook methods and additional validation of fields."""

from abc import ABCMeta


class ExtraMixin(metaclass=ABCMeta):
    """Hook methods and additional validation of fields."""

    async def add_validation(self) -> dict[str, str]:
        """It is supposed to be use to additional validation of fields.
        Format: <"field_name", "Error message">
        """
        error_map: dict[str, str] = {}
        return error_map

    @classmethod
    async def indexing(cls) -> None:
        """For set up and start indexing."""

    async def pre_create(self) -> None:
        """Called before a new document is created in the database."""

    async def post_create(self) -> None:
        """Called after a new document has been created in the database."""

    async def pre_update(self) -> None:
        """Called before updating an existing document in the database."""

    async def post_update(self) -> None:
        """Called after an existing document in the database is updated."""

    async def pre_delete(self) -> None:
        """Called before deleting an existing document in the database."""

    async def post_delete(self) -> None:
        """Called after an existing document in the database has been deleted."""
