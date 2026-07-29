"""Testing the `password` example."""

from __future__ import annotations

import re
import unittest

from pymongo import AsyncMongoClient

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
    """Model of User."""

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
    password = fields.PasswordField(
        label=_("Password"),
        placeholder=_("Enter your password"),
        warning=[
            _("Maximum length: {}").format(256),  # this is an immutable size
            _("Minimum length: {}").format(8),  # this is an immutable size
        ],
    )
    confirm_password = fields.PasswordField(
        label=_("Confirm password"),
        placeholder=_("Repeat your password"),
        # If true, the value of this field is not saved in the database.
        is_ignore=True,
    )

    # Optional method
    async def add_validation(self) -> NamedTuple:
        """Additional validation of fields."""
        _ = self._CUSTOM_TRANSLATOR.gettext
        err_map = self.get_error_map()

        username = self.username
        id = self.id
        password = self.password
        confirm_password = self.confirm_password

        # Check username
        if username is not None and re.match(r"^[a-zA-Z0-9_]+$", username) is None:
            err_map.update("username", _("Allowed characters: {}").format("a-z A-Z 0-9 _"))

        # Check password
        if id is None and password != confirm_password:
            err_map.update("password", _("Passwords do not match!"))

        return err_map


class TestPasswordExample(unittest.IsolatedAsyncioTestCase):
    """Testing the `password` example."""

    async def test_password_example(self):
        """Testing the `password` example."""
        # Maximum number of characters 60.
        database_name = "password_example"

        client = AsyncMongoClient(host=Config.MONGO_HOST)

        # Delete database before test.
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

        # Save User
        is_saved = await user.save()
        if not is_saved:
            user.print_err()
        # ----------------------------------------------------------------------
        #
        # Delete database after test.
        await client.drop_database(database_name)
        await Config.MONGO_CLIENT.close()
        await client.close()


if __name__ == "__main__":
    unittest.main()
