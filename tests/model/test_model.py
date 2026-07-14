"""Testing the module `ramifice.models.model`."""

from __future__ import annotations

import unittest

from ramifice import Translations, model
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


Translations.init_params()


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
        Translations.change_locale("ru")
        m = User()

        self.assertEqual(m.model_name(), "User")
        self.assertEqual(m.full_model_name(), "test_model.User")

        self.assertEqual(m.id_html_attrs["label"], "Идентификатор документа")
        self.assertEqual(m.id_html_attrs["placeholder"], "Он добавляется автоматически")
        self.assertEqual(m.id_html_attrs["hint"], "Он добавляется автоматически")
        self.assertEqual(len(m.id_html_attrs["warning"]), 0)
        self.assertTrue(m.id_html_attrs["hide"])
        self.assertTrue(m.id_html_attrs["disabled"])

        self.assertEqual(m.created_at_html_attrs["label"], "Создан")
        self.assertEqual(m.created_at_html_attrs["placeholder"], "Он добавляется автоматически")
        self.assertEqual(m.created_at_html_attrs["hint"], "Он добавляется автоматически")
        self.assertEqual(m.created_at_html_attrs["warning"][0], "Когда был создан документ.")
        self.assertTrue(m.created_at_html_attrs["hide"])
        self.assertTrue(m.created_at_html_attrs["disabled"])

        self.assertEqual(m.updated_at_html_attrs["label"], "Обновлен")
        self.assertEqual(m.updated_at_html_attrs["placeholder"], "Он добавляется автоматически")
        self.assertEqual(m.updated_at_html_attrs["hint"], "Он добавляется автоматически")
        self.assertEqual(m.updated_at_html_attrs["warning"][0], "Когда был обновлен документ.")
        self.assertTrue(m.updated_at_html_attrs["hide"])
        self.assertTrue(m.updated_at_html_attrs["disabled"])

        self.assertIsNone(m.id)
        self.assertIsNone(m.created_at)
        self.assertIsNone(m.updated_at)
        self.assertIsNone(m.url)
        self.assertIsNone(m.txt)
        self.assertIsNone(m.slug)
        self.assertIsNone(m.phone)
        self.assertIsNone(m.password)
        self.assertIsNone(m.ip)
        self.assertIsNone(m.num_int)
        self.assertIsNone(m.num_float)
        self.assertIsNone(m.img)
        self.assertIsNone(m.hash2)
        self.assertIsNone(m.file)
        self.assertIsNone(m.email)
        self.assertIsNone(m.date_time)
        self.assertIsNone(m.date)
        self.assertIsNone(m.color)
        self.assertIsNone(m.bool)
        self.assertIsNone(m.choice_float_dyn)
        self.assertIsNone(m.choice_float)
        self.assertIsNone(m.choice_float_mult_dyn)
        self.assertIsNone(m.choice_float_mult)
        self.assertIsNone(m.choice_int_dyn)
        self.assertIsNone(m.choice_int_mult_dyn)
        self.assertIsNone(m.choice_int_mult)
        self.assertIsNone(m.choice_txt_dyn)
        self.assertIsNone(m.choice_txt)
        self.assertIsNone(m.choice_txt_mult_dyn)
        self.assertIsNone(m.choice_txt_mult)
        self.assertIsNone(m.choice_int)

        m.id = None
        m.created_at = None
        m.updated_at = None
        m.url = None
        m.txt = None
        m.slug = None
        m.phone = None
        m.password = None
        m.ip = None
        m.num_int = None
        m.num_float = None
        m.img = None
        m.hash2 = None
        m.file = None
        m.email = None
        m.date_time = None
        m.date = None
        m.color = None
        m.bool = None
        m.choice_float_dyn = None
        m.choice_float = None
        m.choice_float_mult_dyn = None
        m.choice_float_mult = None
        m.choice_int_dyn = None
        m.choice_int_mult_dyn = None
        m.choice_int_mult = None
        m.choice_txt_dyn = None
        m.choice_txt = None
        m.choice_txt_mult_dyn = None
        m.choice_txt_mult = None
        m.choice_int = None

        self.assertIsNone(m.id)
        self.assertIsNone(m.created_at)
        self.assertIsNone(m.updated_at)
        self.assertIsNone(m.url)
        self.assertIsNone(m.txt)
        self.assertIsNone(m.slug)
        self.assertIsNone(m.phone)
        self.assertIsNone(m.password)
        self.assertIsNone(m.ip)
        self.assertIsNone(m.num_int)
        self.assertIsNone(m.num_float)
        self.assertIsNone(m.img)
        self.assertIsNone(m.hash2)
        self.assertIsNone(m.file)
        self.assertIsNone(m.email)
        self.assertIsNone(m.date_time)
        self.assertIsNone(m.date)
        self.assertIsNone(m.color)
        self.assertIsNone(m.bool)
        self.assertIsNone(m.choice_float_dyn)
        self.assertIsNone(m.choice_float)
        self.assertIsNone(m.choice_float_mult_dyn)
        self.assertIsNone(m.choice_float_mult)
        self.assertIsNone(m.choice_int_dyn)
        self.assertIsNone(m.choice_int_mult_dyn)
        self.assertIsNone(m.choice_int_mult)
        self.assertIsNone(m.choice_txt_dyn)
        self.assertIsNone(m.choice_txt)
        self.assertIsNone(m.choice_txt_mult_dyn)
        self.assertIsNone(m.choice_txt_mult)
        self.assertIsNone(m.choice_int)

        # Exception checking:
        with self.assertRaises(TypeError):
            m.id = "???"
        with self.assertRaises(TypeError):
            m.created_at = 12
        with self.assertRaises(TypeError):
            m.updated_at = "???"
        with self.assertRaises(TypeError):
            m.url = 12
        with self.assertRaises(TypeError):
            m.txt = 5.2
        with self.assertRaises(TypeError):
            m.slug = 12
        with self.assertRaises(TypeError):
            m.phone = 5.2
        with self.assertRaises(TypeError):
            m.password = 12
        with self.assertRaises(TypeError):
            m.ip = 5.2
        with self.assertRaises(TypeError):
            m.num_int = "???"
        with self.assertRaises(TypeError):
            m.num_float = 12
        with self.assertRaises(TypeError):
            m.img = "???"
        with self.assertRaises(TypeError):
            m.hash2 = 12
        with self.assertRaises(TypeError):
            m.file = 5.2
        with self.assertRaises(TypeError):
            m.email = 12
        with self.assertRaises(TypeError):
            m.date_time = "???"
        with self.assertRaises(TypeError):
            m.date = 5.2
        with self.assertRaises(TypeError):
            m.color = 12
        with self.assertRaises(TypeError):
            m.bool = "???"
        with self.assertRaises(TypeError):
            m.choice_float_dyn = 12
        with self.assertRaises(TypeError):
            m.choice_float = "???"
        with self.assertRaises(TypeError):
            m.choice_float_mult_dyn = 5.2
        with self.assertRaises(TypeError):
            m.choice_float_mult = 5.2
        with self.assertRaises(TypeError):
            m.choice_int_dyn = 5.2
        with self.assertRaises(TypeError):
            m.choice_int_mult_dyn = 12
        with self.assertRaises(TypeError):
            m.choice_int_mult = 12
        with self.assertRaises(TypeError):
            m.choice_txt_dyn = 5.2
        with self.assertRaises(TypeError):
            m.choice_txt = 12
        with self.assertRaises(TypeError):
            m.choice_txt_mult_dyn = "???"
        with self.assertRaises(TypeError):
            m.choice_txt_mult = "???"
        with self.assertRaises(TypeError):
            m.choice_int = 5.2


if __name__ == "__main__":
    unittest.main()
