"""Global storage for data cache."""

import re
from pymongo import MongoClient
from pymongo.database import Database

# Mongo client caching.
MONGO_CLIENT: MongoClient | None = None
# Mongo database caching.
MONGO_DATABASE: Database | None = None
# Database name.
DATABASE_NAME: str = ''
# Super collection name.
# Store technical data for Models migration into a database.
# Store dynamic field data for simulate relationship Many-to-One and Many-to-Manyю.
SUPER_COLLECTION_NAME: str = 'SUPER_COLLECTION'
# Caching a patterns of regular expression.
REGEX: dict[str, re.Pattern] = {
    'database_name': re.compile(r'^[a-zA-Z][-_a-zA-Z0-9]{0,59}$'),
    'service_name': re.compile(r'^[A-Z][a-zA-Z0-9]{0,24}$'),
    'model_name': re.compile(r'^[A-Z][a-zA-Z0-9]{0,24}$'),
    'get_type_marker': re.compile(r'(Text|Integer|Float)'),
    'date_parse': re.compile(r'^(?P<d>[0-9]{2})[-\/\.](?P<m>[0-9]{2})[-\/\.](?P<y>[0-9]{4})$'),
    'date_parse_reverse': re.compile(r'^(?P<y>[0-9]{4})[-\/\.](?P<m>[0-9]{2})[-\/\.](?P<d>[0-9]{2})$'),
    'datetime_parse': re.compile(r'^(?P<d>[0-9]{2})[-\/\.](?P<m>[0-9]{2})[-\/\.](?P<y>[0-9]{4})(?:T|\s)(?<t>[0-9]{2}:[0-9]{2}:[0-9]{2})'),
    'datetime_parse_reverse': re.compile(r'^(?P<y>[0-9]{4})[-\/\.](?P<m>[0-9]{2})[-\/\.](?P<d>[0-9]{2})(?:T|\s)(?<t>[0-9]{2}:[0-9]{2}:[0-9]{2})'),
    'color_code': re.compile(r'^(?:#|0x)(?:[a-f0-9]{3}|[a-f0-9]{6}|[a-f0-9]{8})\b|(?:rgb|hsl)a?\([^\)]*\)$', re.I),
    'password': re.compile(r'^[-._!"`\'  # %&,:;<>=@{}~\$\(\)\*\+\/\\\?\[\]\^\|a-zA-Z0-9]+$'),
    'phone_number': re.compile(r'^\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$'),
}