"""Testing the class `ramifice.mixins.JsonMixin`."""

import unittest

from ramifice import Model, meta
from ramifice.fields import ChoiceIntField


@meta(service_name="Profiles")
class UserProfile(Model):
    """Class for testing."""

    def __init__(self):
        self.profession = ChoiceIntField(choices=[(1, "Musician"), (2, "Artist")])
        #
        super().__init__()

    def __str__(self):
        return str(self.profession.value)


class TestJsonMixin(unittest.TestCase):
    """Testing the class `JsonMixin`."""

    def test_to_json(self):
        """Testing a method `to_json`."""
        x = 3
        print(x.__class__)
        m = UserProfile()
        json_str = m.to_json()
        m2 = UserProfile.from_json(json_str)
        self.assertEqual(m.profession.choices, [(1, "Musician"), (2, "Artist")])
        self.assertEqual(m2.profession.choices, [[1, "Musician"], [2, "Artist"]])


if __name__ == "__main__":
    unittest.main()
