"""Testing the global module `Tools`."""

import unittest

from ramifice.errors import InvalidDateError, InvalidDateTimeError
from ramifice.tools import date_parse, datetime_parse


class TestGlobalTools(unittest.TestCase):
    """Testing the global module `Tools`."""

    def test_tools_date_parse(self):
        """Testing a method `date_parse()`."""
        # Negative:
        self.assertRaises(InvalidDateError, date_parse, '1/1/2024')
        self.assertRaises(InvalidDateError, date_parse, '2024/1/1')
        self.assertRaises(InvalidDateError, date_parse, '1.1.2024')
        self.assertRaises(InvalidDateError, date_parse, '1/1/2024')
        # Positive:
        self.assertEqual(date_parse(
            '16-12-2024').strftime('%Y-%m-%d'), '2024-12-16')
        self.assertEqual(date_parse(
            '16/12/2024').strftime('%Y-%m-%d'), '2024-12-16')
        self.assertEqual(date_parse(
            '16.12.2024').strftime('%Y-%m-%d'), '2024-12-16')
        self.assertEqual(date_parse(
            '2024-12-16').strftime('%Y-%m-%d'), '2024-12-16')
        self.assertEqual(date_parse(
            '2024/12/16').strftime('%Y-%m-%d'), '2024-12-16')
        self.assertEqual(date_parse(
            '2024.12.16').strftime('%Y-%m-%d'), '2024-12-16')

    def test_tools_datetime_parse(self):
        """Testing a method `datetime_parse()`."""
        # Negative:
        self.assertRaises(InvalidDateTimeError, datetime_parse, '1/1/2024')
        self.assertRaises(InvalidDateTimeError, datetime_parse, '2024/1/1')
        self.assertRaises(InvalidDateTimeError, datetime_parse, '1.1.2024')
        self.assertRaises(InvalidDateTimeError, datetime_parse, '1/1/2024')
        self.assertRaises(InvalidDateTimeError,
                          datetime_parse, '1/1/2024 09:33:15')
        self.assertRaises(InvalidDateTimeError,
                          datetime_parse, '2024/1/1 09:33:15')
        self.assertRaises(InvalidDateTimeError,
                          datetime_parse, '1.1.2024 09:33:15')
        self.assertRaises(InvalidDateTimeError,
                          datetime_parse, '1/1/2024 09:33:15')
        self.assertRaises(InvalidDateTimeError,
                          datetime_parse, '1/1/2024T09:33:15')
        self.assertRaises(InvalidDateTimeError,
                          datetime_parse, '2024/1/1T09:33:15')
        self.assertRaises(InvalidDateTimeError,
                          datetime_parse, '1.1.2024T09:33:15')
        self.assertRaises(InvalidDateTimeError,
                          datetime_parse, '1/1/2024T09:33:15')
        # Positive:
        self.assertEqual(datetime_parse(
            '16-12-2024 09:33:15').strftime('%Y-%m-%dT%H:%M:%S'), '2024-12-16T09:33:15')
        self.assertEqual(datetime_parse(
            '16/12/2024 09:33:15').strftime('%Y-%m-%dT%H:%M:%S'), '2024-12-16T09:33:15')
        self.assertEqual(datetime_parse(
            '16.12.2024 09:33:15').strftime('%Y-%m-%dT%H:%M:%S'), '2024-12-16T09:33:15')
        self.assertEqual(datetime_parse(
            '16-12-2024T09:33:15').strftime('%Y-%m-%dT%H:%M:%S'), '2024-12-16T09:33:15')
        self.assertEqual(datetime_parse(
            '16/12/2024T09:33:15').strftime('%Y-%m-%dT%H:%M:%S'), '2024-12-16T09:33:15')
        self.assertEqual(datetime_parse(
            '16.12.2024T09:33:15').strftime('%Y-%m-%dT%H:%M:%S'), '2024-12-16T09:33:15')
        self.assertEqual(datetime_parse(
            '2024-12-16T09:33:15').strftime('%Y-%m-%dT%H:%M:%S'), '2024-12-16T09:33:15')
        self.assertEqual(datetime_parse(
            '2024/12/16T09:33:15').strftime('%Y-%m-%dT%H:%M:%S'), '2024-12-16T09:33:15')
        self.assertEqual(datetime_parse(
            '2024.12.16T09:33:15').strftime('%Y-%m-%dT%H:%M:%S'), '2024-12-16T09:33:15')


if __name__ == '__main__':
    unittest.main()
