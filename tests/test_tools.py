"""Testing the module `ramifice.tools`."""

import unittest

from ramifice.errors import InvalidDateError, InvalidDateTimeError
from ramifice.tools import (
    date_parse,
    datetime_parse,
    is_color,
    is_email,
    is_ip,
    is_mongo_id,
    is_phone,
    is_url,
    normal_email,
)


class TestTools(unittest.TestCase):
    """Testing the module `ramifice.tools`."""

    def test_tools_date_parse(self):
        """Testing a method `date_parse()`."""
        # Negative:
        self.assertRaises(InvalidDateError, date_parse, "1/1/2024")
        self.assertRaises(InvalidDateError, date_parse, "2024/1/1")
        self.assertRaises(InvalidDateError, date_parse, "1.1.2024")
        self.assertRaises(InvalidDateError, date_parse, "1/1/2024")
        # Positive:
        self.assertEqual(date_parse("16-12-2024").strftime("%Y-%m-%d"), "2024-12-16")
        self.assertEqual(date_parse("16/12/2024").strftime("%Y-%m-%d"), "2024-12-16")
        self.assertEqual(date_parse("16.12.2024").strftime("%Y-%m-%d"), "2024-12-16")
        self.assertEqual(date_parse("2024-12-16").strftime("%Y-%m-%d"), "2024-12-16")
        self.assertEqual(date_parse("2024/12/16").strftime("%Y-%m-%d"), "2024-12-16")
        self.assertEqual(date_parse("2024.12.16").strftime("%Y-%m-%d"), "2024-12-16")

    def test_tools_datetime_parse(self):
        """Testing a method `datetime_parse()`."""
        # Negative:
        self.assertRaises(InvalidDateTimeError, datetime_parse, "1/1/2024")
        self.assertRaises(InvalidDateTimeError, datetime_parse, "2024/1/1")
        self.assertRaises(InvalidDateTimeError, datetime_parse, "1.1.2024")
        self.assertRaises(InvalidDateTimeError, datetime_parse, "1/1/2024")
        self.assertRaises(InvalidDateTimeError, datetime_parse, "1/1/2024 09:33:15")
        self.assertRaises(InvalidDateTimeError, datetime_parse, "2024/1/1 09:33:15")
        self.assertRaises(InvalidDateTimeError, datetime_parse, "1.1.2024 09:33:15")
        self.assertRaises(InvalidDateTimeError, datetime_parse, "1/1/2024 09:33:15")
        self.assertRaises(InvalidDateTimeError, datetime_parse, "1/1/2024T09:33:15")
        self.assertRaises(InvalidDateTimeError, datetime_parse, "2024/1/1T09:33:15")
        self.assertRaises(InvalidDateTimeError, datetime_parse, "1.1.2024T09:33:15")
        self.assertRaises(InvalidDateTimeError, datetime_parse, "1/1/2024T09:33:15")
        # Positive:
        self.assertEqual(
            datetime_parse("16-12-2024 09:33:15").strftime("%Y-%m-%dT%H:%M:%S"),
            "2024-12-16T09:33:15",
        )
        self.assertEqual(
            datetime_parse("16/12/2024 09:33:15").strftime("%Y-%m-%dT%H:%M:%S"),
            "2024-12-16T09:33:15",
        )
        self.assertEqual(
            datetime_parse("16.12.2024 09:33:15").strftime("%Y-%m-%dT%H:%M:%S"),
            "2024-12-16T09:33:15",
        )
        self.assertEqual(
            datetime_parse("16-12-2024T09:33:15").strftime("%Y-%m-%dT%H:%M:%S"),
            "2024-12-16T09:33:15",
        )
        self.assertEqual(
            datetime_parse("16/12/2024T09:33:15").strftime("%Y-%m-%dT%H:%M:%S"),
            "2024-12-16T09:33:15",
        )
        self.assertEqual(
            datetime_parse("16.12.2024T09:33:15").strftime("%Y-%m-%dT%H:%M:%S"),
            "2024-12-16T09:33:15",
        )
        self.assertEqual(
            datetime_parse("2024-12-16T09:33:15").strftime("%Y-%m-%dT%H:%M:%S"),
            "2024-12-16T09:33:15",
        )
        self.assertEqual(
            datetime_parse("2024/12/16T09:33:15").strftime("%Y-%m-%dT%H:%M:%S"),
            "2024-12-16T09:33:15",
        )
        self.assertEqual(
            datetime_parse("2024.12.16T09:33:15").strftime("%Y-%m-%dT%H:%M:%S"),
            "2024-12-16T09:33:15",
        )

    def test_normal_email(self):
        """Testing a method `normal_email()`."""
        self.assertIsNone(normal_email(None))
        self.assertIsNone(normal_email("???"))
        self.assertIsNone(normal_email(""))
        self.assertEqual(
            normal_email("my+address@example.net"), "my+address@example.net"
        )
        self.assertEqual(normal_email("kebasyaty@gmail.com"), "kebasyaty@gmail.com")

    def test_is_emale(self):
        """Testing a method `is_email()`."""
        self.assertFalse(is_email(None))
        self.assertFalse(is_email(""))
        self.assertFalse(is_email("my+address@example.net"))
        self.assertTrue(is_email("kebasyaty@gmail.com"))

    def test_is_url(self):
        """Testing a method `is_url()`."""
        self.assertFalse(is_url(None))
        self.assertFalse(is_url(""))
        self.assertFalse(is_url("http://???"))
        self.assertTrue(is_url("https://www.google.com"))

    def test_is_ip(self):
        """Testing a method `is_ip()`."""
        self.assertFalse(is_ip(None))
        self.assertFalse(is_ip(""))
        self.assertFalse(is_ip("127.0."))
        self.assertTrue(is_ip("127.0.0.1"))

    def test_is_color(self):
        """Testing a method `is_color()`."""
        self.assertFalse(is_color(None))
        self.assertFalse(is_color(""))
        self.assertFalse(is_color("color"))
        self.assertTrue(is_color("#000"))

    def test_is_phone(self):
        """Testing a method `is_phone()`."""
        self.assertFalse(is_phone(None))
        self.assertFalse(is_phone(""))
        self.assertFalse(is_phone("+4002123456"))
        self.assertTrue(is_phone("+447986123456"))

    def test_is_mongo_id(self):
        """Testing a method `is_phone()`."""
        self.assertFalse(is_mongo_id(None))
        self.assertFalse(is_mongo_id(""))
        self.assertFalse(is_mongo_id("nviy349ghugh"))
        self.assertTrue(is_mongo_id("666f6f2d6261722d71757578"))


if __name__ == "__main__":
    unittest.main()
