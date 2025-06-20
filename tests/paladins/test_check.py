"""Testing `Ramifice > QPaladinsMixin > CheckMixin` module."""

import unittest

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


class TestPaladinCheckMixin(unittest.IsolatedAsyncioTestCase):
    """Testing `Ramifice > QPaladinsMixin > CheckMixin` module."""

    async def test_check_method(self) -> None:
        """Testing `check` method."""
        # Maximum number of characters 60.
        database_name = "test_check_method"

        # Delete database before test.
        # (if the test fails)
        client: AsyncMongoClient = AsyncMongoClient()
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
        # self.assertTrue(await user.is_valid())
        if not await user.is_valid():
            user.print_err()
        #
        pseudo_user = PseudoUser()
        # self.assertTrue(await pseudo_user.is_valid())
        if not await pseudo_user.is_valid():
            pseudo_user.print_err()
        # ----------------------------------------------------------------------
        #
        # Delete database after test.
        await client.drop_database(database_name)
        await client.close()


if __name__ == "__main__":
    unittest.main()
