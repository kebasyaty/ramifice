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
        m = UserProfile()
        json_str = m.to_json()
        print(json_str)


if __name__ == "__main__":
    unittest.main()
