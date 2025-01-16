"""Testing the module `Model`."""

import unittest

from ramifice import Model


class TestModel(unittest.TestCase):
    """Testing the module `Model`."""

    def test_class_model(self):
        """Testing a class `OutputData`."""
        # fields = Model.__dict__.keys()
        self.assertEqual(Model.__name__, "Model")
        self.assertEqual(Model.__module__, "ramifice.model")
