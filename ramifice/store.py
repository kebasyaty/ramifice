"""Global storage for caching objects.
The purpose of caching is production optimization.
"""

import re

from pymongo import AsyncMongoClient
from pymongo.asynchronous.database import AsyncDatabase

# For block the verification code, at the end of the migration to the database.
DEBUG: bool = True
# Mongo client caching.
MONGO_CLIENT: AsyncMongoClient | None = None
# Mongo database caching.
MONGO_DATABASE: AsyncDatabase | None = None
# Database name.
DATABASE_NAME: str | None = None
# Super collection name.
# Store technical data for Models migration into a database.
# Store dynamic field data for simulate relationship Many-to-One and Many-to-Manyю.
SUPER_COLLECTION_NAME: str = "SUPER_COLLECTION"
# Caching a patterns of regular expression.
REGEX: dict[str, re.Pattern] = {
    "database_name": re.compile(r"^[a-zA-Z][-_a-zA-Z0-9]{0,59}$"),
    "service_name": re.compile(r"^[A-Z][a-zA-Z0-9]{0,24}$"),
    "model_name": re.compile(r"^[A-Z][a-zA-Z0-9]{0,24}$"),
    "color_code": re.compile(
        r"^(?:#|0x)(?:[a-f0-9]{3}|[a-f0-9]{6}|[a-f0-9]{8})\b|(?:rgb|hsl)a?\([^\)]*\)$",
        re.I,
    ),
    "password": re.compile(
        r'^[-._!"`\'#%&,:;<>=@{}~\$\(\)\*\+\/\\\?\[\]\^\|a-zA-Z0-9]{8,256}$'
    ),
}
