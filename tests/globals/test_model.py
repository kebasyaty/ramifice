"""Testing the module `ramifice.model`."""

import unittest

from ramifice import Model


class TestModel(unittest.TestCase):
    """Testing the module `ramifice.model`."""

    def test_class_model(self):
        """Testing a class `Model`."""
        self.assertEqual(Model.__name__, "Model")
        self.assertEqual(Model.__module__, "ramifice.model")
        self.assertIsNotNone(Model.__dict__.get("hash"))
        self.assertIsNotNone(Model.__dict__.get("created_at"))
        self.assertIsNotNone(Model.__dict__.get("updated_at"))
        self.assertIsNotNone(Model.__dict__.get("model_name"))
        self.assertIsNotNone(Model.__dict__.get("full_model_name"))
