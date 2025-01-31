"""Testing the module `ramifice.model`."""

import unittest

from ramifice import Model
from ramifice.fields import TextField


class User(Model):
    """For testing a instance `Model`."""

    def __init__(self):
        self.username = TextField()
        #
        super().__init__()


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
        self.assertIsNone(m.hash.value)
        self.assertIsNone(m.created_at.value)
        self.assertIsNone(m.updated_at.value)
        self.assertIsNone(m.username.value)
        self.assertIsNone(m.to_obj_id())
