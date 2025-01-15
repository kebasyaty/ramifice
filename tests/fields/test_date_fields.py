"""Testing date|datetime fields."""

import unittest
from datetime import datetime

from ramifice.fields import DateField, DateTimeField


class TestDateFields(unittest.TestCase):
    """Testing date|datetime fields."""

    def test_date_field(self):
        """Testing `DateField`."""
        # Parameters by default:
        f = DateField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, "DateField")
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, "date")
        self.assertEqual(f.input_type, "date")
        self.assertIsNone(f.value)
        self.assertIsNone(f.default)
        self.assertEqual(f.placeholder, "")
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertFalse(f.unique)
        self.assertIsNone(f.max_date)
        self.assertIsNone(f.min_date)
        # Exception checking:
        with self.assertRaises(AssertionError):
            DateField(max_date=12)
        with self.assertRaises(AssertionError):
            DateField(max_date="")
        with self.assertRaises(AssertionError):
            DateField(max_date="1/1/2024")
        with self.assertRaises(AssertionError):
            DateField(min_date=12)
        with self.assertRaises(AssertionError):
            DateField(min_date="")
        with self.assertRaises(AssertionError):
            DateField(min_date="1/1/2024")
        with self.assertRaises(AssertionError):
            DateField(default=12)
        with self.assertRaises(AssertionError):
            DateField(default="")
        with self.assertRaises(AssertionError):
            DateField(default="1/1/2024")
        with self.assertRaises(AssertionError):
            DateField(default="20-12-2024", max_date="19-12-2024")
        with self.assertRaises(AssertionError):
            DateField(default="20-12-2024", min_date="21-12-2024")
        DateField(max_date="20-12-2024")
        DateField(min_date="20-12-2024")
        DateField(default="20-12-2024")
        DateField(default="20-12-2024", max_date="21-12-2024", min_date="19-12-2024")
        # Methods:
        f = DateField()
        self.assertIsNone(f.to_datetime())
        f = DateField(default="20-12-2024")
        self.assertEqual(f.to_datetime(), datetime(2024, 12, 20))
        f = DateField()
        f.value = "20-12-2024"
        self.assertEqual(f.to_datetime(), datetime(2024, 12, 20))

    def test_date_time_field(self):
        """Testing `DateTimeField`."""
        # Parameters by default:
        f = DateTimeField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, "DateTimeField")
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, "date")
        self.assertEqual(f.input_type, "datetime")
        self.assertIsNone(f.value)
        self.assertIsNone(f.default)
        self.assertEqual(f.placeholder, "")
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertFalse(f.unique)
        self.assertIsNone(f.max_date)
        self.assertIsNone(f.min_date)
        # Exception checking:
        with self.assertRaises(AssertionError):
            DateTimeField(max_date=12)
        with self.assertRaises(AssertionError):
            DateTimeField(max_date="")
        with self.assertRaises(AssertionError):
            DateTimeField(max_date="1/1/2024 00:00:00")
        with self.assertRaises(AssertionError):
            DateTimeField(min_date=12)
        with self.assertRaises(AssertionError):
            DateTimeField(min_date="")
        with self.assertRaises(AssertionError):
            DateTimeField(min_date="1/1/2024 00:00:00")
        with self.assertRaises(AssertionError):
            DateTimeField(default=12)
        with self.assertRaises(AssertionError):
            DateTimeField(default="")
        with self.assertRaises(AssertionError):
            DateTimeField(default="1/1/2024 00:00:00")
        with self.assertRaises(AssertionError):
            DateTimeField(default="20-12-2024 00:00:00", max_date="19-12-2024 00:00:00")
        with self.assertRaises(AssertionError):
            DateTimeField(default="20-12-2024 00:00:00", min_date="21-12-2024 00:00:00")
        DateTimeField(max_date="20-12-2024 00:00:00")
        DateTimeField(min_date="20-12-2024 00:00:00")
        DateTimeField(default="20-12-2024 00:00:00")
        DateTimeField(
            default="20-12-2024 00:00:00",
            max_date="21-12-2024 00:00:00",
            min_date="19-12-2024 00:00:00",
        )
        # Methods:
        f = DateTimeField()
        self.assertIsNone(f.to_datetime())
        f = DateTimeField(default="20-12-2024 00:00:00")
        self.assertEqual(f.to_datetime(), datetime(2024, 12, 20))
        f = DateTimeField()
        f.value = "20-12-2024 00:00:00"
        self.assertEqual(f.to_datetime(), datetime(2024, 12, 20))


if __name__ == "__main__":
    unittest.main()
