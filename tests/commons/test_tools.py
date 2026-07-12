"""Testing `ramifice > commons > tools` module."""

from __future__ import annotations

import unittest

from bson import ObjectId

from ramifice import model, translations
from ramifice.commons.tools import correct_mongo_filter
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


class TestCommonGeneralMixin(unittest.IsolatedAsyncioTestCase):
    """Testing `ramifice > commons > tools` module."""

    async def test_correct_mongo_filter(self):
        """Testing `correct_mongo_filter` methods."""
        translations.change_locale("en")
        id = ObjectId("666f6f2d6261722d71757578")
        filter = {
            "txt": "John",
            "num_int": 30,
            "url": "https://www.google.com",
            "hash": id,
        }
        correct_fielter = {
            "txt.en": "John",
            "num_int": 30,
            "url": "https://www.google.com",
            "hash": id,
        }
        filter = correct_mongo_filter(User, filter)
        self.assertEqual(filter, correct_fielter)

        filter = {
            "$or": [{"txt": "John"}, {"txt": "Julia"}],
            "num_int": 30,
            "url": "https://www.google.com",
            "hash": id,
        }
        correct_fielter = {
            "$or": [{"txt.en": "John"}, {"txt.en": "Julia"}],
            "num_int": 30,
            "url": "https://www.google.com",
            "hash": id,
        }
        filter = correct_mongo_filter(User, filter)
        self.assertEqual(filter, correct_fielter)


if __name__ == "__main__":
    unittest.main()
