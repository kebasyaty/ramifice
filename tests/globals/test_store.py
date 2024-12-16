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

    def test_regex_database_name(self):
        """Testing a regular expression for `database_name`."""
        p = REGEX['database_name']
        # Negative:
        self.assertIsNone(p.match(""))
        self.assertIsNone(p.match('Database Name'))
        self.assertIsNone(p.match(' DatabaseName'))
        self.assertIsNone(p.match('5DatabaseName'))
        self.assertIsNone(p.match('_DatabaseName'))
        self.assertIsNone(p.match('-DatabaseName'))
        # > 60 characters
        self.assertIsNone(
            p.match('LoremIpsumDolorSitAmetConsecteturAdipiscingElitIntegerLacinia'))
        # Positive:
        self.assertIsNotNone(p.match('D'))
        self.assertIsNotNone(p.match('d'))
        self.assertIsNotNone(p.match('test'))
        self.assertIsNotNone(p.match('DatabaseName'))
        self.assertIsNotNone(p.match('Database_Name'))
        self.assertIsNotNone(p.match('Database-Name'))
        self.assertIsNotNone(p.match('databaseName'))
        self.assertIsNotNone(p.match('database_name'))
        self.assertIsNotNone(p.match('database-name'))
        self.assertIsNotNone(p.match('x4N83BGV26b3Npg2'))
        self.assertIsNotNone(p.match('X4N83BGV26b3Npg2'))
        self.assertIsNotNone(p.match('test_X4N83BGV26b3Npg2'))

    def test_regex_service_name(self):
        """Testing a regular expression for `service_name`."""
        p = REGEX['service_name']
        # Negative:
        self.assertIsNone(p.match(""))
        self.assertIsNone(p.match('Auto parts'))
        self.assertIsNone(p.match('Auto Parts'))
        self.assertIsNone(p.match('autoparts'))
        self.assertIsNone(p.match('Auto_parts'))
        self.assertIsNone(p.match('Auto-parts'))
        self.assertIsNone(p.match('360AutoParts'))
        # > 25 characters
        self.assertIsNone(p.match('Loremipsumdolorsitametcons'))
        # Positive:
        self.assertIsNotNone(p.match('AutoParts'))
        self.assertIsNotNone(p.match('Autoparts'))
        self.assertIsNotNone(p.match('AutoParts360'))

    def test_regex_model_name(self):
        """Testing a regular expression for `model_name`."""
        p = REGEX['model_name']
        # Negative:
        self.assertIsNone(p.match(""))
        self.assertIsNone(p.match('360'))
        self.assertIsNone(p.match('accounts'))
        self.assertIsNone(p.match('Model Name'))
        self.assertIsNone(p.match('360ModelName'))

        # > 25 characters
        self.assertIsNone(p.match('Loremipsumdolorsitametcons'))
        # Positive:
        self.assertIsNotNone(p.match('Accounts'))
        self.assertIsNotNone(p.match('ACCOUNTS'))
        self.assertIsNotNone(p.match('ModelName'))
        self.assertIsNotNone(p.match('ModelName360'))
        self.assertIsNotNone(p.match('MODELNAME360'))

    def test_regex_get_type_marker(self):
        """Testing a regular expression for `get_type_marker`."""
        p = REGEX['get_type_marker']
        # Negative:
        self.assertIsNone(p.match(""))
        self.assertIsNone(p.match('text'))
        self.assertIsNone(p.match('integer'))
        self.assertIsNone(p.match('float'))
        self.assertIsNone(p.match('Tex'))
        self.assertIsNone(p.match('Int'))
        self.assertIsNone(p.match('Intege'))
        self.assertIsNone(p.match('Floa'))
        # Positive:
        self.assertIsNotNone(p.match('Text'))
        self.assertIsNotNone(p.match('TextField'))
        self.assertIsNotNone(p.match('Integer'))
        self.assertIsNotNone(p.match('IntegerField'))
        self.assertIsNotNone(p.match('Float'))
        self.assertIsNotNone(p.match('FloatField'))

    def test_regex_date_parse(self):
        """Testing a regular expression for `date_parse`."""
        p = REGEX['date_parse']
        # Negative:
        self.assertIsNone(p.match(""))
        self.assertIsNone(p.match('1/1/2024'))
        self.assertIsNone(p.match('2024.16.12'))
        self.assertIsNone(p.match('2024-12-16'))
        self.assertIsNone(p.match('2024-1-1'))
        self.assertIsNone(p.match('2024/12/16'))
        self.assertIsNone(p.match('2024/1/1'))
        self.assertIsNone(p.match('1.1.2024'))
        self.assertIsNone(p.match('1-1-2024'))
        self.assertIsNone(p.match('1/1/2024'))
        # Positive:
        self.assertIsNotNone(p.match('16-12-2024'))
        self.assertIsNotNone(p.match('12/12/2024'))
        self.assertIsNotNone(p.match('16.12.2024'))

    def test_regex_date_parse_reverse(self):
        """Testing a regular expression for `date_parse_reverse`."""
        p = REGEX['date_parse_reverse']
        # Negative:
        self.assertIsNone(p.match('12/16/2024'))
        self.assertIsNone(p.match('16.12.2024'))
        self.assertIsNone(p.match('16-12-2024'))
        self.assertIsNone(p.match('16/12/2024'))
        # Positive:
        self.assertIsNotNone(p.match('2024-12-16'))
        self.assertIsNotNone(p.match('2024/12/16'))
        self.assertIsNotNone(p.match('2024.12.16'))

    def test_regex_datetime_parse(self):
        """Testing a regular expression for `datetime_parse`."""
        p = REGEX['datetime_parse']
        # Negative:
        self.assertIsNone(p.match('1/1/2024'))
        self.assertIsNone(p.match('2024.16.12'))
        self.assertIsNone(p.match('2024-12-16'))
        self.assertIsNone(p.match('2024-1-1'))
        self.assertIsNone(p.match('2024/12/16'))
        self.assertIsNone(p.match('2024/1/1'))
        self.assertIsNone(p.match('1.1.2024'))
        self.assertIsNone(p.match('1-1-2024'))
        self.assertIsNone(p.match('1/1/2024'))
        #
        self.assertIsNone(p.match('1/1/2024 09:33:15'))
        self.assertIsNone(p.match('2024.16.12 09:33:15'))
        self.assertIsNone(p.match('2024-12-16 09:33:15'))
        self.assertIsNone(p.match('2024-1-1 09:33:15'))
        self.assertIsNone(p.match('2024/12/16 09:33:15'))
        self.assertIsNone(p.match('2024/1/1 09:33:15'))
        self.assertIsNone(p.match('1.1.2024 09:33:15'))
        self.assertIsNone(p.match('1-1-2024 09:33:15'))
        self.assertIsNone(p.match('1/1/2024 09:33:15'))
        #
        self.assertIsNone(p.match('1/1/2024T09:33:15'))
        self.assertIsNone(p.match('2024.16.12T09:33:15'))
        self.assertIsNone(p.match('2024-12-16T09:33:15'))
        self.assertIsNone(p.match('2024-1-1T09:33:15'))
        self.assertIsNone(p.match('2024/12/16T09:33:15'))
        self.assertIsNone(p.match('2024/1/1T09:33:15'))
        self.assertIsNone(p.match('1.1.2024T09:33:15'))
        self.assertIsNone(p.match('1-1-2024T09:33:15'))
        self.assertIsNone(p.match('1/1/2024T09:33:15'))
        # Positive:
        self.assertIsNotNone(p.match('16-12-2024 09:33:15'))
        self.assertIsNotNone(p.match('12/12/2024 09:33:15'))
        self.assertIsNotNone(p.match('16.12.2024 09:33:15'))
        self.assertIsNotNone(p.match('16-12-2024T09:33:15'))
        self.assertIsNotNone(p.match('12/12/2024T09:33:15'))
        self.assertIsNotNone(p.match('16.12.2024T09:33:15'))

    def test_regex_datetime_parse_reverse(self):
        """Testing a regular expression for `datetime_parse_reverse`."""
        p = REGEX['datetime_parse_reverse']
        # Negative:
        self.assertIsNone(p.match('12/16/2024'))
        self.assertIsNone(p.match('16.12.2024'))
        self.assertIsNone(p.match('16-12-2024'))
        self.assertIsNone(p.match('16/12/2024'))
        #
        self.assertIsNone(p.match('12/16/2024 09:33:15'))
        self.assertIsNone(p.match('16.12.2024 09:33:15'))
        self.assertIsNone(p.match('16-12-2024 09:33:15'))
        self.assertIsNone(p.match('16/12/2024 09:33:15'))
        #
        self.assertIsNone(p.match('12/16/2024T09:33:15'))
        self.assertIsNone(p.match('16.12.2024T09:33:15'))
        self.assertIsNone(p.match('16-12-2024T09:33:15'))
        self.assertIsNone(p.match('16/12/2024T09:33:15'))
        # Positive:
        self.assertIsNotNone(p.match('2024-12-16 09:33:15'))
        self.assertIsNotNone(p.match('2024/12/16 09:33:15'))
        self.assertIsNotNone(p.match('2024.12.16 09:33:15'))
        #
        self.assertIsNotNone(p.match('2024-12-16T09:33:15'))
        self.assertIsNotNone(p.match('2024/12/16T09:33:15'))
        self.assertIsNotNone(p.match('2024.12.16T09:33:15'))


if __name__ == '__main__':
    unittest.main()
