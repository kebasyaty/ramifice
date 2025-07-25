"""Testing `Ramifice > QCommonsMixin > ManyMixin` module."""

import unittest

from pymongo import AsyncMongoClient

from ramifice import Migration, model
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


class TestCommonManyMixin(unittest.IsolatedAsyncioTestCase):
    """Testing `Ramifice > QCommonsMixin > ManyMixin` module."""

    async def test_many_mixin_methods(self):
        """Testing OneMixin methods."""
        # Maximum number of characters 60.
        database_name = "test_many_mixin_methods"

        client: AsyncMongoClient = AsyncMongoClient()

        # Delete database before test.
        # (if the test fails)
        await client.drop_database(database_name)
        await client.close()

        client = AsyncMongoClient()
        await Migration(
            database_name=database_name,
            mongo_client=client,
        ).migrate()
        #
        # HELLISH BURN
        # ----------------------------------------------------------------------
        m = User()
        # self.assertTrue(await m.save())
        if not await m.save():
            m.print_err()
        #
        doc_list = await User.find_many()
        self.assertTrue(isinstance(doc_list, list))
        self.assertEqual(len(doc_list), 1)
        self.assertEqual(len(doc_list[0]), 32)
        doc_list = await User.find_many_to_raw_docs()
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
