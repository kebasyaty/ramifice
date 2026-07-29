"""Testing `Ramifice > QPaladinsMixin > PsswordMixin` module."""

from __future__ import annotations

import unittest

from pymongo import AsyncMongoClient

from ramifice import Migration, Model, meta
from ramifice.config import Config
from ramifice.fields import PasswordField


@meta(service_name="Accounts")
class User(Model):
    """Model for testing."""

    password = PasswordField()
    password_2 = PasswordField()


class TestPaladinPasswordMixin(unittest.IsolatedAsyncioTestCase):
    """Testing `Ramifice > QPaladinsMixin > PsswordMixin` module."""

    async def test_pssword_methods(self):
        """Testing PsswordMixin module."""
        # Maximum number of characters 60.
        database_name = "test_pssword_methods"

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

        m = User()
        password = "12345678"  # ruff:ignore[hardcoded-password-string]
        new_password = "new_12345678"  # ruff:ignore[hardcoded-password-string]
        password_2 = "123456789"  # ruff:ignore[hardcoded-password-string]
        new_password_2 = "new_123456789"  # ruff:ignore[hardcoded-password-string]
        m.password = password
        m.password_2 = password_2
        if not await m.save():
            m.print_err()
        self.assertEqual(await User.estimated_document_count(), 1)
        self.assertTrue(await m.verify_password(password))
        self.assertFalse(await m.verify_password("123"))
        self.assertTrue(await m.verify_password(password_2, "password_2"))
        self.assertFalse(await m.verify_password("123", "password_2"))
        await m.update_password(password, new_password)
        self.assertTrue(await m.verify_password(new_password))
        await m.update_password(password_2, new_password_2, "password_2")
        self.assertTrue(await m.verify_password(new_password_2, "password_2"))
        # ----------------------------------------------------------------------
        #
        # Delete database after test.
        await client.drop_database(database_name)
        await client.close()


if __name__ == "__main__":
    unittest.main()
