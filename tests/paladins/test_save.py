"""Testing `Ramifice > QPaladinsMixin > SaveMixin` module."""

import unittest

from bson.objectid import ObjectId
from pymongo import AsyncMongoClient

from ramifice import model
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
from ramifice.utils.migration import Monitor


@model(service_name="Accounts")
class User:
    """Model for testing."""

    def fields(self):
        """For adding fields."""
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
    is_migrate_model=False,
)
class PseudoUser:
    """Model for testing."""

    def fields(self):
        """For adding fields."""
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
        self.choice_float = ChoiceFloatField()
        self.choice_float_mult = ChoiceFloatMultField()
        self.choice_int_mult = ChoiceIntMultField()
        self.choice_txt = ChoiceTextField()
        self.choice_txt_mult = ChoiceTextMultField()
        self.choice_int = ChoiceIntField()


@model(service_name="Accounts")
class UniqueUser:
    """For test the uniqueness of values."""

    def fields(self):
        """For adding fields."""
        self.username = TextField(
            unique=True,
        )
        self.email = EmailField(
            unique=True,
        )
        self.age = IntegerField(
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
        await Monitor(
            database_name=database_name,
            mongo_client=client,
        ).migrat()
        #
        # HELLISH BURN
        # ----------------------------------------------------------------------
        user = User()
        # Create doc.
        if not await user.save():
            user.print_err()
        self.assertTrue(isinstance(user.id.value, ObjectId))
        doc_id = str(user.id.value)
        # Update doc.
        if not await user.save():
            user.print_err()
        self.assertEqual(str(user.id.value), doc_id)
        # Update doc.
        if not await user.save():
            user.print_err()
        #
        self.assertEqual(str(user.id.value), doc_id)
        self.assertEqual(await User.estimated_document_count(), 1)
        result = await user.delete()
        self.assertTrue(isinstance(result, dict))
        self.assertEqual(len(result), 31)
        self.assertEqual(await User.estimated_document_count(), 0)

        pseudo_user = PseudoUser()
        with self.assertRaises(AttributeError):
            await pseudo_user.save()

        # Check Unique.
        # positive
        unique_user = UniqueUser()
        unique_user.username.value = "pythondev"
        unique_user.email.value = "John_Smith@gmail.com"
        unique_user.age.value = 32
        self.assertTrue(await unique_user.save())
        unique_user = UniqueUser()
        self.assertTrue(await unique_user.save())
        # negative
        unique_user = UniqueUser()
        unique_user.username.value = "pythondev"
        self.assertFalse(await unique_user.save())
        unique_user = UniqueUser()
        unique_user.email.value = "John_Smith@gmail.com"
        self.assertFalse(await unique_user.save())
        unique_user = UniqueUser()
        unique_user.age.value = 32
        self.assertFalse(await unique_user.save())
        # ----------------------------------------------------------------------
        #
        # Delete database after test.
        await client.drop_database(database_name)
        await client.close()


if __name__ == "__main__":
    unittest.main()
