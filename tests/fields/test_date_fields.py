"""Testing a parameters with default values for date|datetime fields."""

import unittest
from ramifice.fields import (DateField, DateTimeField)


class TestDateFields(unittest.TestCase):
    """Testing parameters with default values."""

    def test_date_field(self):
        """Testing a parameters by default for DateField."""
        f = DateField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, 'DateField')
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, 'date')
        self.assertEqual(f.input_type, 'date')
        self.assertIsNone(f.value)
        self.assertIsNone(f.default)
        self.assertEqual(f.placeholder, "")
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertFalse(f.unique)
        self.assertIsNone(f.max_date)
        self.assertIsNone(f.min_date)

    def test_date_time_field(self):
        """Testing a parameters by default for DateTimeField."""
        f = DateTimeField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, 'DateTimeField')
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, 'date')
        self.assertEqual(f.input_type, 'datetime')
        self.assertIsNone(f.value)
        self.assertIsNone(f.default)
        self.assertEqual(f.placeholder, "")
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertFalse(f.unique)
        self.assertIsNone(f.max_date)
        self.assertIsNone(f.min_date)


if __name__ == '__main__':
    unittest.main()
