"""Testing `ramifice > commons > tools` module."""

import unittest

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

    def fields(self):
        """For adding fields."""
        self.url = URLField()
        self.txt = TextField(multi_language=True)
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


class TestCommonGeneralMixin(unittest.IsolatedAsyncioTestCase):
    """Testing `ramifice > commons > tools` module."""

    async def test_correct_mongo_filter(self):
        """Testing `correct_mongo_filter` methods."""
        translations.change_locale("en")
        filter = {
            "txt": "John",
            "num_int": 30,
            "url": "https://www.google.com",
        }
        correct_fielter = {
            "txt.en": "John",
            "num_int": 30,
            "url": "https://www.google.com",
        }
        filter = correct_mongo_filter(User, filter)
        self.assertEqual(filter, correct_fielter)

        filter = {
            "$or": [{"txt": "John"}, {"txt": "Julia"}],
            "num_int": 30,
            "url": "https://www.google.com",
        }
        correct_fielter = {
            "$or": [{"txt.en": "John"}, {"txt.en": "Julia"}],
            "num_int": 30,
            "url": "https://www.google.com",
        }
        filter = correct_mongo_filter(User, filter)
        self.assertEqual(filter, correct_fielter)


if __name__ == "__main__":
    unittest.main()
