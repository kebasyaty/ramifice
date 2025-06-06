"""Testing the module `ramifice.model`."""

import unittest

from src.ramifice import model
from src.ramifice.fields import TextField
from src.ramifice.model import Model


@model(service_name="Accounts")
class User:
    """Model for testing."""

    def fields(self, gettext):
        self.username = TextField()


class TestModel(unittest.TestCase):
    """Testing the module `ramifice.model`."""

    def test_class_model(self):
        """Testing a class `Model`."""
        self.assertFalse(bool(Model.META))
        self.assertEqual(Model.__name__, "Model")
        self.assertEqual(Model.__module__, "ramifice.model")
        self.assertIsNotNone(Model.__dict__.get("model_name"))
        self.assertIsNotNone(Model.__dict__.get("full_model_name"))

    def test_instance_model(self):
        """Testing a instance `Model`."""
        m = User()
        #
        self.assertEqual(m.model_name(), "User")
        self.assertEqual(m.full_model_name(), "tests.test_model.User")
        #
        self.assertIsNone(m._id.value)
        self.assertIsNone(m.created_at.value)
        self.assertIsNone(m.updated_at.value)
        self.assertIsNone(m.username.value)


if __name__ == "__main__":
    unittest.main()
