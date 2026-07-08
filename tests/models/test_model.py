"""Testing the module `ramifice.models.model`."""

from __future__ import annotations

import unittest

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
from ramifice.models.model import Model


@model(service_name="Accounts")
class User:
    """Model for testing."""

    def fields(self) -> None:
        """Adding fields."""
        self.url = URLField()
        self.txt = TextField()
        self.txt2 = TextField()
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


class TestModel(unittest.TestCase):
    """Testing the module `ramifice.models.model`."""

    def test_class_model(self):
        """Testing a class `Model`."""
        self.assertFalse(bool(Model.META))
        self.assertEqual(Model.__name__, "Model")
        self.assertEqual(Model.__module__, "ramifice.models.model")
        self.assertIsNotNone(Model.__dict__.get("model_name"))
        self.assertIsNotNone(Model.__dict__.get("full_model_name"))

    def test_instance_model(self):
        """Testing a instance `Model`."""
        m = User()
        #
        self.assertEqual(m.model_name(), "User")
        self.assertEqual(m.full_model_name(), "test_model.User")
        #
        self.assertIsNone(m.id)
        self.assertIsNone(m.created_at)
        self.assertIsNone(m.updated_at)
        self.assertIsNone(m.username)


if __name__ == "__main__":
    unittest.main()
