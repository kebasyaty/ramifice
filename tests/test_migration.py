"""Testing the module `ramifice.migration`."""

import unittest

from pymongo import AsyncMongoClient
from pymongo.asynchronous.collection import AsyncCollection

from ramifice import model, store
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
from ramifice.migration import Monitor


@model(service_name="Accounts")
class User:
    """Model for testing."""

    def fields(self):
        self.url = URLField()
        self.txt = TextField()
        self.slug = SlugField()
        self.phone = PhoneField()
        self.password = PasswordField()
        self.ip = IPField()
        self.num_int = IntegerField()
        self.num_float = FloatField()
        self.img = ImageField()
        self.hash2 = IDField()
        self.file = FileField()
        self.email = EmailField()
        self.date_time = DateTimeField()
        self.date = DateField()
        self.color = ColorField()
        self.bool = BooleanField()
        self.choice_float_dyn = ChoiceFloatDynField()
        self.choice_float = ChoiceFloatField()
        self.choice_float_mult_dyn = ChoiceFloatMultDynField()
        self.choice_float_mult = ChoiceFloatMultField()
        self.choice_int_dyn = ChoiceIntDynField()
        self.choice_int_mult_dyn = ChoiceIntMultDynField()
        self.choice_int_mult = ChoiceIntMultField()
        self.choice_txt_dyn = ChoiceTextDynField()
        self.choice_txt = ChoiceTextField()
        self.choice_txt_mult_dyn = ChoiceTextMultDynField()
        self.choice_txt_mult = ChoiceTextMultField()
        self.choice_int = ChoiceIntField()


@model(
    service_name="Accounts",
    is_migrat_model=False,
)
class PseudoUser:
    """Model for testing."""

    def fields(self):
        self.url = URLField()
        self.txt = TextField()
        self.slug = SlugField()
        self.phone = PhoneField()
        self.password = PasswordField()
        self.ip = IPField()
        self.num_int = IntegerField()
        self.num_float = FloatField()
        self.img = ImageField()
        self.hash2 = IDField()
        self.file = FileField()
        self.email = EmailField()
        self.date_time = DateTimeField()
        self.date = DateField()
        self.color = ColorField()
        self.bool = BooleanField()
        self.choice_float_dyn = ChoiceFloatDynField()
        self.choice_float = ChoiceFloatField()
        self.choice_float_mult_dyn = ChoiceFloatMultDynField()
        self.choice_float_mult = ChoiceFloatMultField()
        self.choice_int_dyn = ChoiceIntDynField()
        self.choice_int_mult_dyn = ChoiceIntMultDynField()
        self.choice_int_mult = ChoiceIntMultField()
        self.choice_txt_dyn = ChoiceTextDynField()
        self.choice_txt = ChoiceTextField()
        self.choice_txt_mult_dyn = ChoiceTextMultDynField()
        self.choice_txt_mult = ChoiceTextMultField()
        self.choice_int = ChoiceIntField()


class TestMigration(unittest.IsolatedAsyncioTestCase):
    """Testing the module `ramifice.migration`."""

    async def test_monitor(self):
        """Testing a `Monitor`."""
        # Maximum number of characters 60.
        database_name = "test_monitor_migration"

        # Delete database before test.
        # (if the test fails)
        client = AsyncMongoClient()
        await client.drop_database(database_name)
        await client.close()

        self.assertTrue(store.DEBUG)

        client = AsyncMongoClient()
        await Monitor(
            database_name=database_name,
            mongo_client=client,
        ).migrat()

        self.assertFalse(store.DEBUG)
        super_collection: AsyncCollection = store.MONGO_DATABASE[  # type: ignore[annotation-unchecked]
            store.SUPER_COLLECTION_NAME
        ]
        self.assertEqual(await super_collection.estimated_document_count(), 1)

        # Delete database after test.
        await client.drop_database(database_name)
        await client.close()


if __name__ == "__main__":
    unittest.main()
