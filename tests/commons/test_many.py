"""Testing `Ramifice > QCommonsMixin > ManyMixin` module."""

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


class TestCommonManyMixin(unittest.IsolatedAsyncioTestCase):
    """Testing `Ramifice > QCommonsMixin > ManyMixin` module."""

    async def test_many_mixin_methods(self):
        """Testing OneMixin methods."""
        # Maximum number of characters 60.
        database_name = "test_many_mixin_methods"

        client = AsyncMongoClient(host=Config.MONGO_HOST)

        # Delete database before test.
        # (if the test fails)
        await client.drop_database(database_name)
        await client.close()

        client = AsyncMongoClient(host=Config.MONGO_HOST)
        await Migration(
            database_name=database_name,
            mongo_client=client,
        ).migrate()
        #
        # HELLISH BURN
        # ----------------------------------------------------------------------
        m = User()
        if not await m.save():
            m.print_err()
        #
        doc_list = await User.find_many()
        self.assertTrue(isinstance(doc_list, list))
        self.assertEqual(len(doc_list), 1)
        self.assertEqual(len(doc_list[0]), 32)
        doc_list = await User.find_many_to_model_dict_list()
        self.assertTrue(isinstance(doc_list, list))
        self.assertEqual(len(doc_list), 1)
        self.assertEqual(len(doc_list[0]), 32)
        docs_json = await User.find_many_to_json()
        self.assertTrue(isinstance(docs_json, str))
        self.assertTrue(len(docs_json) > 0)
        self.assertEqual(await User.estimated_document_count(), 1)
        await User.delete_many({})
        self.assertEqual(await User.estimated_document_count(), 0)
        m = User()
        await m.save()
        m = User()
        await m.save()
        m = User()
        await m.save()
        self.assertEqual(await User.estimated_document_count(), 3)
        await User.delete_many({})
        self.assertEqual(await User.estimated_document_count(), 0)
        # ----------------------------------------------------------------------
        #
        # Delete database after test.
        await client.drop_database(database_name)
        await client.close()


if __name__ == "__main__":
    unittest.main()
