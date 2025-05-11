"""Testing `Ramifice > Commons > OneMixin` module."""

import unittest

from pymongo import AsyncMongoClient

from ramifice import Model, meta, store
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
    HashField,
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


@meta(service_name="Accounts")
class User(Model):
    """Class for testing."""

    def __init__(self):
        self.url = URLField()
        self.txt = TextField()
        self.slug = SlugField()
        self.phone = PhoneField()
        self.password = PasswordField()
        self.ip = IPField()
        self.num_int = IntegerField()
        self.num_float = FloatField()
        self.img = ImageField()
        self.hash2 = HashField()
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
        #
        super().__init__()


class TestCommonOneMixin(unittest.IsolatedAsyncioTestCase):
    """Testing `Ramifice > Commons > OneMixin` module."""

    async def test_one_mixin_methods(self):
        """Testing OneMixin methods."""
        # Maximum number of characters 60.
        database_name = "test_one_mixin_methods"

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
        # self.assertTrue(await m.save())
        if not await m.save():
            m.print_err()
        #
        doc = await User.find_one({"_id": m.to_obj_id()})
        self.assertTrue(isinstance(doc, dict))
        #
        model = await User.find_one_to_instance({"_id": m.to_obj_id()})
        self.assertEqual(model.hash.value, m.hash.value)
        #
        json_str = await User.find_one_to_json({"_id": m.to_obj_id()})
        self.assertEqual(json_str, m.to_json())
        #
        await User.delete_one({"_id": m.to_obj_id()})
        self.assertEqual(await User.estimated_document_count(), 0)
        #
        m = User()
        if not await m.save():
            m.print_err()
        doc = await User.find_one_and_delete({"_id": m.to_obj_id()})
        self.assertEqual(str(doc["_id"]), m.hash.value)
        self.assertEqual(await User.estimated_document_count(), 0)
        # ----------------------------------------------------------------------
        #
        # Delete database after test.
        await client.drop_database(database_name)
        await client.close()


if __name__ == "__main__":
    unittest.main()
