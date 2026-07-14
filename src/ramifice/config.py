# Ramifice - ORM-pseudo-like API MongoDB for Python language.
# Copyright (c) 2024 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""Ramifice settings.

The settings class contains the following parameters:

- `DEBUG` - Caching a condition for the verification code.
- `MONGO_CLIENT` - Caching a Mongo client.
- `MONGO_DATABASE` - Caching a Mongo database.
- `DATABASE_NAME` - Caching a database name.
- `SUPER_COLLECTION_NAME` - Caching a super collection name.
- `MEDIA_ROOT` - Absolute filesystem path to the directory that will hold user-uploaded files.
- `MEDIA_URL` - URL that handles the media served from MEDIA_ROOT, used for managing stored files.
- `STATIC_ROOT` - The absolute path to the directory where static files are located.
- `STATIC_URL` - URL to use when referring to static files located in STATIC_ROOT.
- `UTC_TIMEZONE` - Caching a patterns of regular expression.
- `REGEX` - Caching a patterns of regular expression.
"""

from __future__ import annotations

__all__ = ("Config",)


import re
from typing import ClassVar, final
from zoneinfo import ZoneInfo

from pymongo import AsyncMongoClient
from pymongo.asynchronous.database import AsyncDatabase


@final
class Config:
    """Ramifice settings."""

    # Caching a condition for the verification code.
    # For block the verification code, at the end of the migration to the database.
    DEBUG: ClassVar[bool] = True
    # Caching a Mongo client.
    MONGO_CLIENT: ClassVar[AsyncMongoClient | None] = None
    # Caching a Mongo database.
    MONGO_DATABASE: ClassVar[AsyncDatabase | None] = None
    # Caching a database name.
    DATABASE_NAME: ClassVar[str | None] = None
    # Caching a super collection name.
    # Store technical data for Models migration into a database.
    # Store dynamic field data for simulate relationship Many-to-One and Many-to-Manyю.
    SUPER_COLLECTION_NAME: ClassVar[str] = "SUPER_COLLECTION"
    # Absolute filesystem path to the
    # directory that will hold user-uploaded files.
    MEDIA_ROOT: ClassVar[str] = "public/media"
    # URL that handles the media served from MEDIA_ROOT,
    # used for managing stored files.
    MEDIA_URL: ClassVar[str] = "/media"
    # The absolute path to the
    # directory where static files are located.
    STATIC_ROOT: ClassVar[str] = "public/static"
    # URL to use when referring to
    # static files located in STATIC_ROOT.
    STATIC_URL: ClassVar[str] = "/static"
    # Caching a UTC timezone object.
    UTC_TIMEZONE: ClassVar[ZoneInfo] = ZoneInfo("UTC")
    # Caching a patterns of regular expression.
    REGEX: ClassVar[dict[str, re.Pattern]] = {
        "database_name": re.compile(r"^[a-zA-Z][-_a-zA-Z0-9]{0,59}$"),
        "service_name": re.compile(r"^[A-Z][a-zA-Z0-9]{0,24}$"),
        "model_name": re.compile(r"^[A-Z][a-zA-Z0-9]{0,24}$"),
        "color_code": re.compile(
            r"^(?:#|0x)(?:[a-f0-9]{3}|[a-f0-9]{6}|[a-f0-9]{8})\b|(?:rgb|hsl)a?\([^\)]*\)$",
            re.I,  # noqa: FURB167
        ),
        "password": re.compile(r'^[-._!"`\'#%&,:;<>=@{}~\$\(\)\*\+\/\\\?\[\]\^\|a-zA-Z0-9]{8,256}$'),
    }
