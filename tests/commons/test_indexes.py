"""Testing `Ramifice > QCommonsMixi > IndexMixin` module."""

from __future__ import annotations

import unittest

from pymongo import ASCENDING, DESCENDING, AsyncMongoClient, IndexModel

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

    @classmethod
    async def indexing(cls) -> None:
        """For set up and start indexing."""
        await cls.create_index(["email"], name="idx_email")
        #
        index_1 = IndexModel([("color", DESCENDING), ("url", ASCENDING)], name="idx_color_url")
        index_2 = IndexModel([("text", DESCENDING)], name="idx_text")
        await cls.create_indexes([index_1, index_2])


class TestCommonIndexMixin(unittest.IsolatedAsyncioTestCase):
    """Testing `Ramifice > QCommonsMixin > IndexMixin` module."""

    async def test_index_mixin_methods(self):
        """Testing OneMixin methods."""
        # Maximum number of characters 60.
        database_name = "test_index_mixin_methods"

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

        m = User()
        m.email = "kebasyaty@gmail.com"
        if not await m.save():
            m.print_err()
        #
        mongo_doc = await User.find_one({"email": "kebasyaty@gmail.com"})
        self.assertEqual(mongo_doc["email"], "kebasyaty@gmail.com")
        await User.drop_index("idx_email")
        await User.drop_indexes()
        # ----------------------------------------------------------------------
        #
        # Delete database after test.
        await client.drop_database(database_name)
        await client.close()


if __name__ == "__main__":
    unittest.main()
