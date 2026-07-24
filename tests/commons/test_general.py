"""Testing `Ramifice > QCommonsMixin > GeneraMixin` module."""

from __future__ import annotations

import unittest

from pymongo import AsyncMongoClient

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
    txt2 = TextField(multi_language=True)
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


class TestCommonGeneralMixin(unittest.IsolatedAsyncioTestCase):
    """Testing `Ramifice > QCommonsMixin > GeneraMixin` module."""

    async def test_general_mixin_methods(self):
        """Testing GeneralMixin methods."""
        # Maximum number of characters 60.
        database_name = "test_general_mixin_methods"

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

        self.assertEqual(await User.estimated_document_count(), 0)
        self.assertEqual(await User.count_documents({}), 0)
        m = User()
        if not await m.save():
            m.print_err()
        self.assertEqual(await User.estimated_document_count(), 1)
        self.assertEqual(await User.count_documents({}), 1)
        self.assertEqual(await User.count_documents({"_id": m.id}), 1)
        self.assertEqual(User.collection_name(), "Accounts_User")
        self.assertEqual(User.collection_full_name(), "test_general_mixin_methods.Accounts_User")
        self.assertEqual(User.database(), Config.MONGO_DATABASE)
        self.assertEqual(User.collection(), Config.MONGO_DATABASE[User.META["collection_name"]])
        # ----------------------------------------------------------------------
        #
        # Delete database after test.
        await client.drop_database(database_name)
        await client.close()


if __name__ == "__main__":
    unittest.main()
