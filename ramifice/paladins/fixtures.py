"""Fixtures - To populate the database with pre-created data."""

from pymongo.asynchronous.collection import AsyncCollection


class FixtureMixin:
    """Mixin for Model."""

    async def apply_fixture(self, fixture_name: str, collection: AsyncCollection):
        """Apply fixture for current Model."""
