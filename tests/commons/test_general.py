"""Testing `Ramifice > QCommonsMixin > GeneraMixin` module."""

import unittest

from pymongo import AsyncMongoClient

from ramifice import MigrationManager, model
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
from ramifice.utils import globals


@model(service_name="Accounts")
class User:
    """Model for testing."""

    def fields(self):
        """For adding fields."""
        self.url = URLField()
        self.txt = TextField()
        self.txt2 = TextField(multi_language=True)
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


class TestCommonGeneralMixin(unittest.IsolatedAsyncioTestCase):
    """Testing `Ramifice > QCommonsMixin > GeneraMixin` module."""

    async def test_general_mixin_methods(self):
        """Testing GeneralMixin methods."""
        # Maximum number of characters 60.
        database_name = "test_general_mixin_methods"

        client: AsyncMongoClient = AsyncMongoClient()

        # Delete database before test.
        # (if the test fails)
        await client.drop_database(database_name)
        await client.close()

        client = AsyncMongoClient()
        await MigrationManager(
            database_name=database_name,
            mongo_client=client,
        ).migrate()
        #
        # HELLISH BURN
        # ----------------------------------------------------------------------
        self.assertEqual(await User.estimated_document_count(), 0)
        self.assertEqual(await User.count_documents({}), 0)
        m = User()
        # self.assertTrue(await m.save())
        if not await m.save():
            m.print_err()
        self.assertEqual(await User.estimated_document_count(), 1)
        self.assertEqual(await User.count_documents({}), 1)
        self.assertEqual(await User.count_documents({"_id": m.id.value}), 1)
        self.assertEqual(User.collection_name(), "Accounts_User")
        self.assertEqual(User.collection_full_name(), "test_general_mixin_methods.Accounts_User")
        self.assertEqual(User.database(), globals.MONGO_DATABASE)
        self.assertEqual(User.collection(), globals.MONGO_DATABASE[User.META["collection_name"]])
        # ----------------------------------------------------------------------
        #
        # Delete database after test.
        await client.drop_database(database_name)
        await client.close()


if __name__ == "__main__":
    unittest.main()
