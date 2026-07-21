"""Testing the module `ramifice.migration`."""

from __future__ import annotations

import unittest

from pymongo import AsyncMongoClient
from pymongo.asynchronous.collection import AsyncCollection

from ramifice import Migration, Model, meta
from ramifice.config import Config
from ramifice.fields import (
    BooleanField,
    ChoiceFloatDynField,
    ChoiceFloatField,
    ChoiceFloatMultDynField,
    ChoiceFloatMultField,
    ChoiceIntDynField,
    ChoiceIntField,
    ChoiceIntMultDynField,
    ChoiceIntMultField,
    ChoiceTextDynField,
    ChoiceTextField,
    ChoiceTextMultDynField,
    ChoiceTextMultField,
    ColorField,
    DateField,
    DateTimeField,
    EmailField,
    FileField,
    FloatField,
    IDField,
    ImageField,
    IntegerField,
    IPField,
    PasswordField,
    PhoneField,
    SlugField,
    TextField,
    URLField,
)


@meta(service_name="Accounts")
class User(Model):
    """Model for testing."""

    url = URLField()
    txt = TextField()
    slug = SlugField()
    phone = PhoneField()
    password = PasswordField()
    ip = IPField()
    num_int = IntegerField()
    num_float = FloatField()
    img = ImageField()
    hash2 = IDField()
    file = FileField()
    email = EmailField()
    date_time = DateTimeField()
    date = DateField()
    color = ColorField()
    bool = BooleanField()
    choice_float_dyn = ChoiceFloatDynField()
    choice_float = ChoiceFloatField()
    choice_float_mult_dyn = ChoiceFloatMultDynField()
    choice_float_mult = ChoiceFloatMultField()
    choice_int_dyn = ChoiceIntDynField()
    choice_int_mult_dyn = ChoiceIntMultDynField()
    choice_int_mult = ChoiceIntMultField()
    choice_txt_dyn = ChoiceTextDynField()
    choice_txt = ChoiceTextField()
    choice_txt_mult_dyn = ChoiceTextMultDynField()
    choice_txt_mult = ChoiceTextMultField()
    choice_int = ChoiceIntField()


class TestMigration(unittest.IsolatedAsyncioTestCase):
    """Testing the module `ramifice.migration`."""

    async def test_migration_manager(self):
        """Testing a `Migration`."""
        # Maximum number of characters 60.
        database_name = "test_migration_manager"

        client: AsyncMongoClient = AsyncMongoClient(host=Config.MONGO_HOST)

        # Delete database before test.
        # (if the test fails)
        await client.drop_database(database_name)
        await client.close()

        self.assertTrue(Config.DEBUG)

        client = AsyncMongoClient(host=Config.MONGO_HOST)
        await Migration(
            database_name=database_name,
            mongo_client=client,
        ).migrate()

        self.assertFalse(Config.DEBUG)
        super_collection: AsyncCollection = Config.MONGO_DATABASE[Config.SUPER_COLLECTION_NAME]
        self.assertEqual(await super_collection.estimated_document_count(), 1)

        # Delete database after test.
        await client.drop_database(database_name)
        await client.close()


if __name__ == "__main__":
    unittest.main()
