"""Testing date|datetime fields."""

import unittest

from dateutil.parser import parse

from ramifice.fields import DateField, DateTimeField
from ramifice.store import CURRENT_LOCALE


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
        self.assertEqual(f.errors, [])
        self.assertEqual(f.group, "date")
        self.assertEqual(f.input_type, "date")
        self.assertIsNone(f.value)
        self.assertIsNone(f.default)
        self.assertEqual(f.placeholder, "")
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertIsNone(f.max_date)
        self.assertIsNone(f.min_date)
        # Exception checking:
        with self.assertRaises(AssertionError):
            DateField(max_date=12)
        with self.assertRaises(AssertionError):
            DateField(max_date="")
        with self.assertRaises(AssertionError):
            DateField(min_date=12)
        with self.assertRaises(AssertionError):
            DateField(min_date="")
        with self.assertRaises(AssertionError):
            DateField(default=12)
        with self.assertRaises(AssertionError):
            DateField(default="")
        with self.assertRaises(AssertionError):
            DateField(default=parse("20-12-2024"), max_date=parse("19-12-2024"))
        with self.assertRaises(AssertionError):
            DateField(default=parse("20-12-2024"), min_date=parse("21-12-2024"))
        with self.assertRaises(AssertionError):
            DateField(max_date=parse("20-12-2024"), min_date=parse("20-12-2024"))
        with self.assertRaises(AssertionError):
            DateField(max_date=parse("20-12-2024"), min_date=parse("21-12-2024"))
        DateField(max_date=parse("20-12-2024"))
        DateField(min_date=parse("20-12-2024"))
        DateField(default=parse("20-12-2024"))
        DateField(
            default=parse("20-12-2024"),
            max_date=parse("21-12-2024"),
            min_date=parse("19-12-2024"),
        )

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
        self.assertEqual(f.errors, [])
        self.assertEqual(f.group, "date")
        self.assertEqual(f.input_type, "datetime")
        self.assertIsNone(f.value)
        self.assertIsNone(f.default)
        self.assertEqual(f.placeholder, "")
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertIsNone(f.max_date)
        self.assertIsNone(f.min_date)
        # Exception checking:
        with self.assertRaises(AssertionError):
            DateTimeField(max_date=12)
        with self.assertRaises(AssertionError):
            DateTimeField(max_date="")
        with self.assertRaises(AssertionError):
            DateTimeField(min_date=12)
        with self.assertRaises(AssertionError):
            DateTimeField(min_date="")
        with self.assertRaises(AssertionError):
            DateTimeField(default=12)
        with self.assertRaises(AssertionError):
            DateTimeField(default="")
        with self.assertRaises(AssertionError):
            DateTimeField(
                default=parse("20-12-2024 00:00:00"),
                max_date=parse("19-12-2024 00:00:00"),
            )
        with self.assertRaises(AssertionError):
            DateTimeField(
                default=parse("20-12-2024 00:00:00"),
                min_date=parse("21-12-2024 00:00:00"),
            )
        DateTimeField(max_date=parse("20-12-2024 00:00:00"))
        DateTimeField(min_date=parse("20-12-2024 00:00:00"))
        DateTimeField(default=parse("20-12-2024 00:00:00"))
        DateTimeField(
            default=parse("20-12-2024 00:00:00"),
            max_date=parse("21-12-2024 00:00:00"),
            min_date=parse("19-12-2024 00:00:00"),
        )


if __name__ == "__main__":
    unittest.main()
