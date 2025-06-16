"""Testing the destructor of the Model.

The method `ramifice.model.Model.__del__ `.
If the model is not migrated,
it must delete files and images in the destructor.
"""

import unittest

from pymongo import AsyncMongoClient

from ramifice import model
from ramifice.fields import FileField, ImageField, TextField
from ramifice.migration import Monitor


@model(
    service_name="Accounts",
    is_migrate_model=False,
)
class User:
    """Model for testing."""

    def fields(self):
        """For adding fields."""
        self.avatar = ImageField()
        self.resume = FileField()


@model(service_name="Accounts")
class UserProfile:
    """Stub Model to circumvent migration restrictions."""

    def fields(self):
        """For adding fields."""
        self.profession = TextField()


class TestDestructorModel(unittest.IsolatedAsyncioTestCase):
    """Testing the destructor of the Model.

    The method `ramifice.model.Model.__del__`.
    If the model is not migrated,
    it must delete files and images in the destructor.
    """

    async def test_del_method(self):
        """Testing the destructor of the Model."""
        # Maximum number of characters 60.
        database_name = "test_del_method"

        # Delete database before test.
        # (if the test fails)
        client: AsyncMongoClient = AsyncMongoClient()
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
        user = User()
        user.avatar.from_path(
            src_path="public/media/default/no-photo.png",
        )
        user.resume.from_path(
            src_path="public/media/default/no_doc.odt",
        )

        if not await user.is_valid():
            user.print_err()
            self.assertTrue(False)
        del user
        # ----------------------------------------------------------------------
        #
        # Delete database after test.
        await client.drop_database(database_name)
        await client.close()


if __name__ == "__main__":
    unittest.main()
