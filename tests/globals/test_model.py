"""Testing the module `Model`."""

import unittest

from ramifice import Model


class TestModel(unittest.TestCase):
    """Testing the module `Model`."""

    def test_class_model(self):
        """Testing a class `OutputData`."""
        fields = Model.__dict__
        self.assertEqual(fields, {})
