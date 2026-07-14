"""Testing date|datetime fields."""

from __future__ import annotations

import unittest

from dateparser import parse

from ramifice.fields import DateField, DateTimeField


class TestDateFields(unittest.TestCase):
    """Testing date|datetime fields."""

    def test_date_field(self):
        """Testing `DateField`."""
        # Parameters by default:
        f = DateField()
        self.assertEqual(f.html_attrs["id"], "")
        self.assertEqual(f.html_attrs["label"], "")
        self.assertEqual(f.html_attrs["name"], "")
        self.assertEqual(f.html_attrs["field_type"], "DateField")
        self.assertFalse(f.html_attrs["disabled"])
        self.assertFalse(f.html_attrs["hide"])
        self.assertFalse(f.html_attrs["ignored"])
        self.assertEqual(len(f.html_attrs["warning"]), 0)
        self.assertEqual(f.html_attrs["errors"], [])
        self.assertEqual(f.html_attrs["group"], "date")
        self.assertEqual(f.html_attrs["input_type"], "date")
        self.assertIsNone(f.html_attrs["value"])
        self.assertIsNone(f.html_attrs["default"])
        self.assertEqual(f.html_attrs["placeholder"], "")
        self.assertEqual(f.html_attrs["hint"], "")
        self.assertFalse(f.html_attrs["required"])
        self.assertFalse(f.html_attrs["readonly"])
        self.assertIsNone(f.html_attrs["max_date"])
        self.assertIsNone(f.html_attrs["min_date"])
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
        self.assertEqual(f.html_attrs["id"], "")
        self.assertEqual(f.html_attrs["label"], "")
        self.assertEqual(f.html_attrs["name"], "")
        self.assertEqual(f.html_attrs["field_type"], "DateTimeField")
        self.assertFalse(f.html_attrs["disabled"])
        self.assertFalse(f.html_attrs["hide"])
        self.assertFalse(f.html_attrs["ignored"])
        self.assertEqual(len(f.html_attrs["warning"]), 0)
        self.assertEqual(f.html_attrs["errors"], [])
        self.assertEqual(f.html_attrs["group"], "date")
        self.assertEqual(f.html_attrs["input_type"], "datetime")
        self.assertIsNone(f.html_attrs["value"])
        self.assertIsNone(f.html_attrs["default"])
        self.assertEqual(f.html_attrs["placeholder"], "")
        self.assertEqual(f.html_attrs["hint"], "")
        self.assertFalse(f.html_attrs["required"])
        self.assertFalse(f.html_attrs["readonly"])
        self.assertIsNone(f.html_attrs["max_date"])
        self.assertIsNone(f.html_attrs["min_date"])
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
