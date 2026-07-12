"""Testing `Ramifice > QPaladinsMixin > SaveMixin` module."""

from __future__ import annotations

import unittest

from bson.objectid import ObjectId
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


@model(service_name="Accounts")
class UniqueUser:
    """For test the uniqueness of values."""

    username = TextField(
        unique=True,
    )
    email = EmailField(
        unique=True,
    )
    age = IntegerField(
        unique=True,
    )


class TestPaladinSaveMixin(unittest.IsolatedAsyncioTestCase):
    """Testing `Ramifice > QPaladinsMixin > SaveMixin` module."""

    async def test_save_method(self):
        """Testing `save` method."""
        # Maximum number of characters 60.
        database_name = "test_save_method"

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
        user = User()
        # Create doc.
        if not await user.save():
            user.print_err()
        self.assertTrue(isinstance(user.id, ObjectId))
        doc_id = str(user.id)
        # Update doc.
        if not await user.save():
            user.print_err()
        self.assertEqual(str(user.id), doc_id)
        # Update doc.
        if not await user.save():
            user.print_err()

        self.assertEqual(str(user.id), doc_id)
        self.assertEqual(await User.estimated_document_count(), 1)
        result = await user.delete()
        self.assertTrue(isinstance(result, dict))
        self.assertEqual(len(result), 31)
        self.assertEqual(await User.estimated_document_count(), 0)

        # Check Unique.
        # positive
        unique_user = UniqueUser()
        unique_user.username = "pythondev"
        unique_user.email = "John_Smith@gmail.com"
        unique_user.age = 32
        self.assertTrue(await unique_user.save())
        unique_user = UniqueUser()
        self.assertTrue(await unique_user.save())
        # negative
        unique_user = UniqueUser()
        unique_user.username = "pythondev"
        self.assertFalse(await unique_user.save())
        unique_user = UniqueUser()
        unique_user.email = "John_Smith@gmail.com"
        self.assertFalse(await unique_user.save())
        unique_user = UniqueUser()
        unique_user.age = 32
        self.assertFalse(await unique_user.save())
        # ----------------------------------------------------------------------
        #
        # Delete database after test.
        await client.drop_database(database_name)
        await client.close()


if __name__ == "__main__":
    unittest.main()
