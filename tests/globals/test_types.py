"""Testing the global module `Types`."""

import unittest

from ramifice.globals.types import OutputData, Unit


class TestGlobalType(unittest.TestCase):
    """Testing the global module `Types`."""

    def test_output_data(self):
        """Testing a class `OutputData`."""
        d = OutputData(data={'field_name': 'value'}, valid=True, update=False)
        self.assertEqual(d.data, {'field_name': 'value'})
        self.assertTrue(d.valid)
        self.assertFalse(d.update)
        d.valid = False
        self.assertFalse(d.valid)

    def test_unit(self):
        """Testing a class `Unit`."""
        u = Unit(field='field_name', title='Title', value='value')
        self.assertEqual(u.field, 'field_name')
        self.assertEqual(u.title, 'Title')
        self.assertEqual(u.value, 'value')
        self.assertFalse(u.delete)
        u = Unit(field='field_name', title='Title', value='value', delete=True)
        self.assertEqual(u.field, 'field_name')
        self.assertEqual(u.title, 'Title')
        self.assertEqual(u.value, 'value')
        self.assertTrue(u.delete)
