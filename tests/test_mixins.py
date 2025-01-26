"""Testing the class `ramifice.mixins.JsonMixin`."""

import unittest

from ramifice import Model, meta
from ramifice.fields import ChoiceIntField
from ramifice.mixins import JsonMixin


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


@meta(service_name="Profiles")
class User(Model):
    """For testing the Ramifice fields."""

    def __init__(self):
        self.profession = ChoiceIntField(choices=[(1, "Musician"), (2, "Artist")])
        #
        super().__init__()

    def __str__(self):
        return str(self.profession.value)


class TestJsonMixin(unittest.TestCase):
    """Testing the class `JsonMixin`."""

    def test_standard_types(self):
        """Testing standard types."""
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

    def test_ramifice_fields(self):
        """Testing the Ramifice fields."""
        m = User()
        json_str = m.to_json()
        m2 = User.from_json(json_str)
        self.assertEqual(m.profession.choices, [(1, "Musician"), (2, "Artist")])
        self.assertEqual(m2.profession.choices, [[1, "Musician"], [2, "Artist"]])


if __name__ == "__main__":
    unittest.main()
