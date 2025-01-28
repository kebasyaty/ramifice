"""Testing the module `ramifice.migration`."""

import unittest

from pymongo import AsyncMongoClient

from ramifice import Model, meta
from ramifice.fields import ChoiceTextDynField, TextField
from ramifice.migration import Monitor


@meta(service_name="Accounts")
class User(Model):
    """Class for testing."""

    def __init__(self):
        self.username = TextField()
        self.favorite_color = ChoiceTextDynField()
        #
        super().__init__()

    def __str__(self):
        return str(self.username.value)


class TestMigration(unittest.IsolatedAsyncioTestCase):
    """Testing the module `ramifice.migration`."""

    async def test_monitor(self):
        """Testing a `Monitor`."""
        # To generate a key (This is not an advertisement):
        # https://randompasswordgen.com/
        unique_key = "alo0V9Q76Yr4r15z"
        # max 60
        database_name = f"test_{unique_key}"

        # Delete database before test.
        # (if the test fails)
        client = AsyncMongoClient()
        await client.drop_database(database_name)
        await client.close()

        client = AsyncMongoClient()
        await Monitor(
            database_name=database_name,
            mongo_client=client,
        ).migrat()

        # Delete database after test.
        await client.drop_database(database_name)
        await client.close()
