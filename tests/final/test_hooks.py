"""Testing the `hooks` example."""

from __future__ import annotations

import logging
import unittest
from typing import Any

from pymongo import AsyncMongoClient

from ramifice import (
    Migration,
    Model,
    Translator,
    fields,
    meta,
)
from ramifice.config import Config

_ = Translator.STUB_TRANSLATOR_FOR_ATTRIBUTES_OF_FIELD


@meta(service_name="Accounts")
class User(Model):
    """User Model."""

    username = fields.TextField(
        label=_("Username"),
        is_require=True,
        is_unique=True,
    )
    email = fields.EmailField(
        label=_("Email"),
        is_require=True,
        is_unique=True,
    )

    # Optional method
    async def pre_create(self) -> None:
        """Called before a new document is created in the database."""
        logging.info("!!!-pre_create-!!!")

    # Optional method
    async def post_create(self) -> None:
        """Called after a new document has been created in the database."""
        logging.info("!!!-post_create-!!!")

    # Optional method
    async def pre_update(self) -> None:
        """Called before updating an existing document in the database."""
        logging.info("!!!-pre_update-!!!")

    # Optional method
    async def post_update(self) -> None:
        """Called after an existing document in the database is updated."""
        logging.info("!!!-post_update-!!!")

    # Optional method
    async def pre_delete(self) -> None:
        """Called before deleting an existing document in the database."""
        logging.info("!!!-pre_delete-!!!")

    # Optional method
    async def post_delete(self) -> None:
        """Called after an existing document in the database has been deleted."""
        logging.info("!!!-post_delete-!!!")


class TestHooksExample(unittest.IsolatedAsyncioTestCase):
    """Testing the `hooks` example."""

    async def test_hooks_example(self):
        """Testing the `hooks` example."""
        # Maximum number of characters 60
        database_name = "hooks_example"

        client = AsyncMongoClient(host=Config.MONGO_HOST)

        # Delete database before test
        # (if the test fails)
        await client.drop_database(database_name)
        await client.close()
        #
        # ----------------------------------------------------------------------
        client = AsyncMongoClient(host=Config.MONGO_HOST)
        await Migration(
            database_name=database_name,
            mongo_client=client,
        ).migrate()

        user = User()
        user.username = "pythondev"
        user.email = "John_Smith@gmail.com"

        # Create User
        is_saved = await user.save()
        if not is_saved:
            user.print_err()

        # Update User
        user.username = "pythondev-123"
        is_saved = await user.save()
        if not is_saved:
            user.print_err()

        # Delete User
        user_mongo_doc: dict[str, Any] = await user.delete()
        self.assertTrue(isinstance(user_mongo_doc, dict))
        # ----------------------------------------------------------------------
        #
        # Delete database after test.
        await client.drop_database(database_name)
        await client.close()


if __name__ == "__main__":
    unittest.main()
