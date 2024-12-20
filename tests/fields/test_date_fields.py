"""Testing date|datetime fields."""

import unittest

from ramifice.fields import (DateField, DateTimeField)


class TestDateFields(unittest.TestCase):
    """Testing date|datetime fields."""

    def test_date_field(self):
        """Testing `DateField`."""
        # Parameters by default:
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
        # Additional check:
        with self.assertRaises(AssertionError):
            DateField(default=12)
        with self.assertRaises(AssertionError):
            DateField(default="")
        with self.assertRaises(AssertionError):
            DateField(default='1/1/2024')
        DateField(default='20-12-2024')

    def test_date_time_field(self):
        """Testing `DateTimeField`."""
        # Parameters by default:
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
        # Additional check:
        with self.assertRaises(AssertionError):
            DateTimeField(default=12)
        with self.assertRaises(AssertionError):
            DateTimeField(default="")
        with self.assertRaises(AssertionError):
            DateTimeField(default='1/1/2024 00:00:00')
        DateTimeField(default='20-12-2024 15:27:26')


if __name__ == '__main__':
    unittest.main()
