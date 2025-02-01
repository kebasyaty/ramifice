"""Testing the class `ramifice.mixins.JsonMixin`."""

import unittest

from ramifice import Model, meta
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
from ramifice.mixins import JsonMixin
from ramifice.types import FileData, ImageData


class StandardTypes(JsonMixin):
    """For testing standard types."""

    def __init__(self):
        JsonMixin.__init__(self)
        self.x1 = {"x": 1, "y": 2}
        self.x2 = [1, 2, 3]
        self.x3 = (1, 2, 3)
        self.x4 = "Hello world!"
        self.x5 = 12
        self.x6 = 12.3
        self.x7 = True
        self.x8 = False
        self.x9 = None


@meta(service_name="Accounts")
class User(Model):
    """For testing the Ramifice fields."""

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
        self.choice_int = ChoiceIntField(choices={"Title": 1, "Title 2": 2})
        #
        super().__init__()

    def __str__(self):
        return str(self.txt.value)


class TestJsonMixin(unittest.TestCase):
    """Testing the class `JsonMixin`."""

    def test_standard_types(self):
        """Testing standard types to JSON."""
        x = StandardTypes()
        json_str = x.to_json()
        y = StandardTypes.from_json(json_str)
        self.assertEqual(x.x1, y.x1)
        self.assertEqual(x.x2, y.x2)
        self.assertEqual(x.x3, (1, 2, 3))  # y.x3 == [1, 2, 3]
        self.assertEqual(x.x4, y.x4)
        self.assertEqual(x.x5, y.x5)
        self.assertEqual(x.x6, y.x6)
        self.assertEqual(x.x7, y.x7)
        self.assertEqual(x.x8, y.x8)
        self.assertEqual(x.x9, y.x9)

    def test_fields(self):
        """Testing the Ramifice fields to JSON."""
        m = User()
        #
        json_str = m.to_json()
        m2 = User.from_json(json_str)
        for name, data in m.__dict__.items():
            if not callable(data):
                self.assertEqual(m2.__dict__[name].__dict__, data.__dict__)
        #
        json_str = m.to_json_only_value()
        m3 = User.from_json_only_value(json_str)
        for name, data in m.__dict__.items():
            if not callable(data):
                self.assertEqual(m3.__dict__[name].__dict__, data.__dict__)
        #
        #
        m = User()
        m.img.value = ImageData()
        m.file.value = FileData()
        #
        json_str = m.to_json()
        m2 = User.from_json(json_str)
        for name, data in m.__dict__["img"].__dict__["value"].__dict__.items():
            if not callable(data):
                data2 = m2.__dict__["img"].__dict__["value"].__dict__[name]
                self.assertEqual(data, data2)
        for name, data in m.__dict__["file"].__dict__["value"].__dict__.items():
            if not callable(data):
                data2 = m2.__dict__["file"].__dict__["value"].__dict__[name]
                self.assertEqual(data, data2)


if __name__ == "__main__":
    unittest.main()
