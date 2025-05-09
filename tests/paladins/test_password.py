"""Testing `Ramifice > Paladins > PsswordMixin module."""

import unittest

from pymongo import AsyncMongoClient

from ramifice import Model, meta
from ramifice.fields import PasswordField
from ramifice.migration import Monitor


@meta(service_name="Accounts")
class User(Model):
    """Class for testing."""

    def __init__(self):
        self.password = PasswordField()
        self.password_2 = PasswordField()
        #
        super().__init__()


class TestPaladinPassword(unittest.IsolatedAsyncioTestCase):
    """Testing `Ramifice > Paladins > PsswordMixin module."""

    async def test_pssword_mixin(self):
        """Testing PsswordMixin module."""
        # Maximum number of characters 60.
        database_name = "test_pssword_mixin"

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
        #
        # HELLISH BURN
        # ----------------------------------------------------------------------
        m = User()
        password = "12345678"
        password_2 = "123456789"
        m.password.value = password
        m.password_2.value = password_2
        # self.assertTrue(await m.save())
        if not await m.save():
            m.print_err()
        self.assertEqual(await User.estimated_document_count(), 1)
        self.assertTrue(await m.verify_password(password))
        self.assertFalse(await m.verify_password("123"))
        self.assertTrue(await m.verify_password(password_2, "password_2"))
        self.assertFalse(await m.verify_password("123", "password_2"))

        # ----------------------------------------------------------------------
        #
        # Delete database after test.
        await client.drop_database(database_name)
        await client.close()


if __name__ == "__main__":
    unittest.main()
