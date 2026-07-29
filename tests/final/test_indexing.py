"""Testing the `indexing` example."""

from __future__ import annotations

import logging
import re
import unittest
from typing import Any

from pymongo import ASCENDING, AsyncMongoClient

from ramifice import (
    Migration,
    Model,
    NamedTuple,
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
        placeholder=_("Enter your username"),
        max_length=150,
        is_require=True,
        is_unique=True,
        warning=[
            _("Allowed characters: {}").format("a-z A-Z 0-9 _"),
            _("Maximum length: {}").format(150),
        ],
    )
    first_name = fields.TextField(
        label=_("First name"),
        placeholder=_("Enter your First name"),
        is_multilingual=True,  # Support for several language.
        max_length=150,
        is_require=True,
        warning=[
            _("Maximum length: {}").format(150),
        ],
    )
    last_name = fields.TextField(
        label=_("Last name"),
        placeholder=_("Enter your Last name"),
        is_multilingual=True,  # Support for several language.
        max_length=150,
        is_require=True,
        warning=[
            _("Maximum length: {}").format(150),
        ],
    )
    email = fields.EmailField(
        label=_("Email"),
        placeholder=_("Enter your email"),
        is_require=True,
        is_unique=True,
    )

    # Optional method
    async def add_validation(self) -> NamedTuple:
        """Additional validation of fields."""
        _ = self._CUSTOM_TRANSLATOR.gettext
        err_map = self.get_error_map()
        username = self.username
        # Check username
        if username is not None and re.match(r"^[a-zA-Z0-9_]+$", username) is None:
            err_map.update("username", _("Allowed characters: {}").format("a-z A-Z 0-9 _"))

        return err_map

    # Optional method
    @classmethod
    async def indexing(cls) -> None:
        """To set up and start indexing."""
        await cls.create_index(
            [("username", ASCENDING)],
            name="username_Idx",
        )
        await cls.create_index(
            [("email", ASCENDING)],
            name="email_Idx",
        )


class TestIndexingExample(unittest.IsolatedAsyncioTestCase):
    """Testing the `indexing` example."""

    async def test_indexing_example(self):
        """Testing the `indexing` example."""
        # Maximum number of characters 60
        database_name = "indexing_example"

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

        # Create User
        user = User()
        user.username = "pythondev"
        user.first_name = "John"
        user.last_name = "Smith"
        user.email = "John_Smith@gmail.com"

        # Save User
        is_saved = await user.save()
        if not is_saved:
            user.print_err()

        # Delete User
        deleted_user: dict[str, Any] = await user.delete()
        self.assertTrue(isinstance(deleted_user, dict))

        # Remove indexes
        await User.drop_index("username_Idx")
        await User.drop_index("email_Idx")

        # Index information
        index_info = await User.index_information()
        logging.critical(index_info)
        # ----------------------------------------------------------------------
        #
        # Delete database after test.
        await client.drop_database(database_name)
        await client.close()


if __name__ == "__main__":
    unittest.main()
