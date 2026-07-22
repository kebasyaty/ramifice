"""Testing date|datetime fields."""

from __future__ import annotations

import unittest

from dateparser import parse

from ramifice.config import Config
from ramifice.fields import DateField, DateTimeField


class TestDateFields(unittest.TestCase):
    """Testing date|datetime fields."""

    def test_date_field(self):
        """Testing `DateField`."""
        DATEPARSER_SETTINGS = Config.DATEPARSER_SETTINGS

        # Parameters by default:
        f = DateField()
        self.assertEqual(f.html_attrs.id, "")
        self.assertEqual(f.html_attrs.label, "")
        self.assertEqual(f.html_attrs.name, "")
        self.assertEqual(f.html_attrs.field_type, "DateField")
        self.assertFalse(f.html_attrs.disabled)
        self.assertFalse(f.html_attrs.hide)
        self.assertFalse(f.html_attrs.ignored)
        self.assertEqual(len(f.html_attrs.warning), 0)
        self.assertEqual(f.html_attrs.errors, [])
        self.assertEqual(f.html_attrs.group, "date")
        self.assertEqual(f.html_attrs.input_type, "date")
        self.assertIsNone(f.html_attrs.value)
        self.assertIsNone(f.html_attrs.default)
        self.assertEqual(f.html_attrs.placeholder, "")
        self.assertEqual(f.html_attrs.hint, "")
        self.assertFalse(f.html_attrs.required)
        self.assertFalse(f.html_attrs.readonly)
        self.assertIsNone(f.html_attrs.max_date)
        self.assertIsNone(f.html_attrs.min_date)

        DateField(default="", max_date="", min_date="")
        self.assertIsNone(f.html_attrs.default)
        self.assertIsNone(f.html_attrs.max_date)
        self.assertIsNone(f.html_attrs.min_date)

        DateField(default="???", max_date="???", min_date="???")
        self.assertIsNone(f.html_attrs.default)
        self.assertIsNone(f.html_attrs.max_date)
        self.assertIsNone(f.html_attrs.min_date)

        # Exception checking:
        with self.assertRaises(AssertionError):
            DateField(max_date=12)
        with self.assertRaises(AssertionError):
            DateField(min_date=12)
        with self.assertRaises(AssertionError):
            DateField(default=12)
        with self.assertRaises(AssertionError):
            DateField(
                default=parse("20-12-2024", settings=DATEPARSER_SETTINGS),
                max_date=parse("19-12-2024", settings=DATEPARSER_SETTINGS),
            )
        with self.assertRaises(AssertionError):
            DateField(
                default=parse("20-12-2024", settings=DATEPARSER_SETTINGS),
                min_date=parse("21-12-2024", settings=DATEPARSER_SETTINGS),
            )
        with self.assertRaises(AssertionError):
            DateField(
                max_date=parse("20-12-2024", settings=DATEPARSER_SETTINGS),
                min_date=parse("20-12-2024", settings=DATEPARSER_SETTINGS),
            )
        with self.assertRaises(AssertionError):
            DateField(
                max_date=parse("20-12-2024", settings=DATEPARSER_SETTINGS),
                min_date=parse("21-12-2024", settings=DATEPARSER_SETTINGS),
            )
        DateField(max_date=parse("20-12-2024", settings=DATEPARSER_SETTINGS))
        DateField(min_date=parse("20-12-2024", settings=DATEPARSER_SETTINGS))
        DateField(default=parse("20-12-2024", settings=DATEPARSER_SETTINGS))
        DateField(
            default=parse("20-12-2024", settings=DATEPARSER_SETTINGS),
            max_date=parse("21-12-2024", settings=DATEPARSER_SETTINGS),
            min_date=parse("19-12-2024", settings=DATEPARSER_SETTINGS),
        )

    def test_date_time_field(self):
        """Testing `DateTimeField`."""
        DATEPARSER_SETTINGS = Config.DATEPARSER_SETTINGS

        # Parameters by default:
        f = DateTimeField()
        self.assertEqual(f.html_attrs.id, "")
        self.assertEqual(f.html_attrs.label, "")
        self.assertEqual(f.html_attrs.name, "")
        self.assertEqual(f.html_attrs.field_type, "DateTimeField")
        self.assertFalse(f.html_attrs.disabled)
        self.assertFalse(f.html_attrs.hide)
        self.assertFalse(f.html_attrs.ignored)
        self.assertEqual(len(f.html_attrs.warning), 0)
        self.assertEqual(f.html_attrs.errors, [])
        self.assertEqual(f.html_attrs.group, "date")
        self.assertEqual(f.html_attrs.input_type, "datetime")
        self.assertIsNone(f.html_attrs.value)
        self.assertIsNone(f.html_attrs.default)
        self.assertEqual(f.html_attrs.placeholder, "")
        self.assertEqual(f.html_attrs.hint, "")
        self.assertFalse(f.html_attrs.required)
        self.assertFalse(f.html_attrs.readonly)
        self.assertIsNone(f.html_attrs.max_date)
        self.assertIsNone(f.html_attrs.min_date)

        DateTimeField(default="", max_date="", min_date="")
        self.assertIsNone(f.html_attrs.default)
        self.assertIsNone(f.html_attrs.max_date)
        self.assertIsNone(f.html_attrs.min_date)

        DateTimeField(default="???", max_date="???", min_date="???")
        self.assertIsNone(f.html_attrs.default)
        self.assertIsNone(f.html_attrs.max_date)
        self.assertIsNone(f.html_attrs.min_date)

        # Exception checking:
        with self.assertRaises(AssertionError):
            DateTimeField(max_date=12)
        with self.assertRaises(AssertionError):
            DateTimeField(min_date=12)
        with self.assertRaises(AssertionError):
            DateTimeField(default=12)
        with self.assertRaises(AssertionError):
            DateTimeField(
                default=parse("20-12-2024 00:00:00", settings=DATEPARSER_SETTINGS),
                max_date=parse("19-12-2024 00:00:00", settings=DATEPARSER_SETTINGS),
            )
        with self.assertRaises(AssertionError):
            DateTimeField(
                default=parse("20-12-2024 00:00:00", settings=DATEPARSER_SETTINGS),
                min_date=parse("21-12-2024 00:00:00", settings=DATEPARSER_SETTINGS),
            )
        DateTimeField(max_date=parse("20-12-2024 00:00:00", settings=DATEPARSER_SETTINGS))
        DateTimeField(min_date=parse("20-12-2024 00:00:00", settings=DATEPARSER_SETTINGS))
        DateTimeField(default=parse("20-12-2024 00:00:00", settings=DATEPARSER_SETTINGS))
        DateTimeField(
            default=parse("20-12-2024 00:00:00", settings=DATEPARSER_SETTINGS),
            max_date=parse("21-12-2024 00:00:00", settings=DATEPARSER_SETTINGS),
            min_date=parse("19-12-2024 00:00:00", settings=DATEPARSER_SETTINGS),
        )


if __name__ == "__main__":
    unittest.main()
