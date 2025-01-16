"""Testing the module `ramifice.model`."""

import unittest

from ramifice import Model


class ModelName(Model):
    """For testing a instance `Model`."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_property()


class TestModel(unittest.TestCase):
    """Testing the module `ramifice.model`."""

    def test_class_model(self):
        """Testing a class `Model`."""
        self.assertEqual(Model.__name__, "Model")
        self.assertEqual(Model.__module__, "ramifice.model")
        self.assertIsNotNone(Model.__dict__.get("model_name"))
        self.assertIsNotNone(Model.__dict__.get("full_model_name"))

    def test_instance_model(self):
        """Testing a instance `Model`."""
        m = ModelName()
        #
        self.assertEqual(m.model_name(), "ModelName")
        self.assertEqual(m.full_model_name(), "test_model.ModelName")
        self.assertEqual(Model.__subclasses__(), [ModelName])
        #
        self.assertIsNone(m.hash.value)
        self.assertIsNone(m.created_at.value)
        self.assertIsNone(m.updated_at.value)
