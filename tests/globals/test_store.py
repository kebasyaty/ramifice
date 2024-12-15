"""Testing variables in global store."""

import unittest
import re
from ramifice.globals.store import (
    MONGO_CLIENT, MONGO_DATABASE, DATABASE_NAME, SUPER_COLLECTION_NAME, REGEX)


class TestGlobalStore(unittest.TestCase):
    """Testing variables in global store."""

    def test_values_by_default(self):
        """Testing a values by default."""
        global DATABASE_NAME  # pylint: disable=global-statement

        self.assertIsNone(MONGO_CLIENT)
        self.assertIsNone(MONGO_DATABASE)
        self.assertIsNone(DATABASE_NAME)
        DATABASE_NAME = 'test'
        self.assertEqual(DATABASE_NAME, 'test')
        self.assertEqual(SUPER_COLLECTION_NAME, 'SUPER_COLLECTION')
        regex = {
            'database_name': re.compile(r'^[a-zA-Z][-_a-zA-Z0-9]{0,59}$'),
            'service_name': re.compile(r'^[A-Z][a-zA-Z0-9]{0,24}$'),
            'model_name': re.compile(r'^[A-Z][a-zA-Z0-9]{0,24}$'),
            'get_type_marker': re.compile(r'(Text|Integer|Float)'),
            'date_parse': re.compile(r'^(?P<d>[0-9]{2})[-\/\.](?P<m>[0-9]{2})[-\/\.](?P<y>[0-9]{4})$'),
            'date_parse_reverse': re.compile(r'^(?P<y>[0-9]{4})[-\/\.](?P<m>[0-9]{2})[-\/\.](?P<d>[0-9]{2})$'),
            'datetime_parse': re.compile(r'^(?P<d>[0-9]{2})[-\/\.](?P<m>[0-9]{2})[-\/\.](?P<y>[0-9]{4})(?:T|\s)(?P<t>[0-9]{2}:[0-9]{2}:[0-9]{2})'),
            'datetime_parse_reverse': re.compile(r'^(?P<y>[0-9]{4})[-\/\.](?P<m>[0-9]{2})[-\/\.](?P<d>[0-9]{2})(?:T|\s)(?P<t>[0-9]{2}:[0-9]{2}:[0-9]{2})'),
            'color_code': re.compile(r'^(?:#|0x)(?:[a-f0-9]{3}|[a-f0-9]{6}|[a-f0-9]{8})\b|(?:rgb|hsl)a?\([^\)]*\)$', re.I),
            'password': re.compile(r'^[-._!"`\'#%&,:;<>=@{}~\$\(\)\*\+\/\\\?\[\]\^\|a-zA-Z0-9]+$'),
            'phone_number': re.compile(r'^\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$'),
        }
        self.assertEqual(REGEX, regex)


if __name__ == '__main__':
    unittest.main()
