"""Ramifice - HooksMixin - Contains abstract methods for creating hooks."""

__all__ = ("HooksMixin",)

from abc import ABCMeta


class HooksMixin(metaclass=ABCMeta):
    """Ramifice - A set of abstract methods for creating hooks."""

    async def pre_create(self) -> None:
        """Ramifice - Called before a new document is created in the database."""

    async def post_create(self) -> None:
        """Ramifice - Called after a new document has been created in the database."""

    async def pre_update(self) -> None:
        """Ramifice - Called before updating an existing document in the database."""

    async def post_update(self) -> None:
        """Ramifice - Called after an existing document in the database is updated."""

    async def pre_delete(self) -> None:
        """Ramifice - Called before deleting an existing document in the database."""

    async def post_delete(self) -> None:
        """Ramifice - Called after an existing document in the database has been deleted."""
