"""HooksMixin - Contains abstract methods for creating hooks."""

from __future__ import annotations

__all__ = ("HooksMixin",)

from abc import abstractmethod


class HooksMixin:
    """A set of abstract methods for creating hooks."""

    @abstractmethod
    async def pre_create(self) -> None:
        """Called before a new document is created in the database."""

    @abstractmethod
    async def post_create(self) -> None:
        """Called after a new document has been created in the database."""

    @abstractmethod
    async def pre_update(self) -> None:
        """Called before updating an existing document in the database."""

    @abstractmethod
    async def post_update(self) -> None:
        """Called after an existing document in the database is updated."""

    @abstractmethod
    async def pre_delete(self) -> None:
        """Called before deleting an existing document in the database."""

    @abstractmethod
    async def post_delete(self) -> None:
        """Called after an existing document in the database has been deleted."""
