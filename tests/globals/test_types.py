"""Testing the global module `Types`."""

import unittest

from ramifice.globals.types import OutputData


class TestGlobalType(unittest.TestCase):
    """Testing the global module `Types`."""

    def test_output_data(self):
        """Testing a class `OutputData`."""
        d = OutputData(data={'field_name': 'value'}, valid=True, update=False)
        self.assertEqual(d.data, {'field_name': 'value'})
        self.assertTrue(d.valid)
        self.assertFalse(d.update)
