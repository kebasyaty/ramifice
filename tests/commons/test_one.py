"""Testing `Ramifice > QCommonsMixin > OneMixin` module."""

from __future__ import annotations

import datetime
import unittest

from pymongo import AsyncMongoClient
from pymongo.results import DeleteResult

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


class TestCommonOneMixin(unittest.IsolatedAsyncioTestCase):
    """Testing `Ramifice > QCommonsMixin > OneMixin` module."""

    async def test_one_mixin_methods(self):
        """Testing OneMixin methods."""
        # Maximum number of characters 60.
        database_name = "test_one_mixin_methods"

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
        m.date = datetime.datetime(2000, 1, 25, tzinfo=Config.UTC_TIMEZONE)
        m.date_time = datetime.datetime(2000, 1, 25, tzinfo=Config.UTC_TIMEZONE)

        if not await m.save():
            m.print_err()
        #
        doc = await User.find_one({"_id": m.id})
        self.assertTrue(isinstance(doc, dict))
        #
        raw_doc = await User.find_one_to_model_dict({"_id": m.id})
        self.assertTrue(isinstance(raw_doc, dict))
        #
        model = await User.find_one_to_instance_model({"_id": m.id})
        self.assertEqual(model.id, m.id)
        #
        json_str = await User.find_one_to_json({"_id": m.id})
        self.assertEqual(json_str, m.to_json())
        #
        await User.delete_one({"_id": m.id})
        self.assertEqual(await User.estimated_document_count(), 0)
        #
        m = User()
        if not await m.save():
            m.print_err()
        doc = await User.find_one_and_delete({"_id": m.id})
        self.assertEqual(doc["_id"], m.id)
        self.assertEqual(await User.estimated_document_count(), 0)
        #
        m = User()
        if not await m.save():
            m.print_err()
        result = await User.delete_one({"_id": m.id})
        self.assertTrue(isinstance(result, DeleteResult))
        self.assertEqual(await User.estimated_document_count(), 0)
        # ----------------------------------------------------------------------
        #
        # Delete database after test.
        await client.drop_database(database_name)
        await client.close()


if __name__ == "__main__":
    unittest.main()
