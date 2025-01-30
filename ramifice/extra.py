"""Hook methods and additional validation of fields."""

from abc import ABCMeta


class Extra(metaclass=ABCMeta):
    """Hook methods and additional validation of fields."""

    def add_validation(self) -> dict[str, str]:
        """It is supposed to be use to additional validation of fields.
        Format: <"field_name", "Error message">
        """
        error_map: dict[str, str] = {}
        return error_map

    @classmethod
    def indexing(cls) -> None:
        """For set up and start indexing."""

    def pre_create(self) -> None:
        """Called before a new document is created in the database."""

    def post_create(self) -> None:
        """Called after a new document has been created in the database."""

    def pre_update(self) -> None:
        """Called before updating an existing document in the database."""

    def post_update(self) -> None:
        """Called after an existing document in the database is updated."""

    def pre_delete(self) -> None:
        """Called before deleting an existing document in the database."""

    def post_delete(self) -> None:
        """Called after an existing document in the database has been deleted."""
