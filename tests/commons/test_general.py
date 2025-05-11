"""Testing `Ramifice > Commons > GeneraMixin` methods."""

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


class TestCommonGeneral(unittest.IsolatedAsyncioTestCase):
    """Testing `Ramifice > Commons > GeneralMixin` methods."""

    async def test_general_methods(self):
        """Testing General methods."""
        # To generate a key (this is not an advertisement):
        # https://randompasswordgen.com/
        unique_key = "3H38935riZ53ML5u"
        # Maximum number of characters 60
        database_name = f"test_{unique_key}"

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
        self.assertEqual(await User.estimated_document_count(), 0)
        self.assertEqual(await User.count_documents({}), 0)
        m = User()
        # self.assertTrue(await m.save())
        if not await m.save():
            m.print_err()
        self.assertEqual(await User.estimated_document_count(), 1)
        self.assertEqual(await User.count_documents({}), 1)
        self.assertEqual(await User.count_documents({"_id": m.hash.to_obj_id()}), 1)
        self.assertEqual(User.collection_name(), "Accounts_User")
        self.assertEqual(
            User.collection_full_name(), "test_3H38935riZ53ML5u.Accounts_User"
        )
        self.assertEqual(User.database(), store.MONGO_DATABASE)
        self.assertEqual(
            User.collection(), store.MONGO_DATABASE[User.META["collection_name"]]
        )
        # ----------------------------------------------------------------------
        #
        # Delete database after test.
        await client.drop_database(database_name)
        await client.close()


if __name__ == "__main__":
    unittest.main()
