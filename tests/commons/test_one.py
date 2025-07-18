"""Testing `Ramifice > QCommonsMixin > OneMixin` module."""

import datetime
import unittest

from pymongo import AsyncMongoClient
from pymongo.results import DeleteResult

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


class TestCommonOneMixin(unittest.IsolatedAsyncioTestCase):
    """Testing `Ramifice > QCommonsMixin > OneMixin` module."""

    async def test_one_mixin_methods(self):
        """Testing OneMixin methods."""
        # Maximum number of characters 60.
        database_name = "test_one_mixin_methods"

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
        m.date.value = datetime.datetime(2000, 1, 25)
        m.date_time.value = datetime.datetime(2000, 1, 25)
        # self.assertTrue(await m.save())
        if not await m.save():
            m.print_err()
        #
        doc = await User.find_one({"_id": m.id.value})
        self.assertTrue(isinstance(doc, dict))
        #
        raw_doc = await User.find_one_to_raw_doc({"_id": m.id.value})
        self.assertTrue(isinstance(raw_doc, dict))
        #
        model = await User.find_one_to_instance({"_id": m.id.value})
        self.assertEqual(model.id.value, m.id.value)
        #
        json_str = await User.find_one_to_json({"_id": m.id.value})
        self.assertEqual(json_str, m.to_json())
        #
        await User.delete_one({"_id": m.id.value})
        self.assertEqual(await User.estimated_document_count(), 0)
        #
        m = User()
        if not await m.save():
            m.print_err()
        doc = await User.find_one_and_delete({"_id": m.id.value})
        self.assertEqual(doc["_id"], m.id.value)
        self.assertEqual(await User.estimated_document_count(), 0)
        #
        m = User()
        if not await m.save():
            m.print_err()
        result = await User.delete_one({"_id": m.id.value})
        self.assertTrue(isinstance(result, DeleteResult))
        self.assertEqual(await User.estimated_document_count(), 0)
        # ----------------------------------------------------------------------
        #
        # Delete database after test.
        await client.drop_database(database_name)
        await client.close()


if __name__ == "__main__":
    unittest.main()
