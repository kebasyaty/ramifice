# Ramifice - ORM-pseudo-like API MongoDB for Python language.
# Copyright (c) 2024 Gennady Kostyunin
# SPDX-License-Identifier: MIT
#
# Copyright 2024-present MongoDB, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Ramifice settings.

The settings class contains the following parameters:

- `DEBUG` - Condition for the verification code.
- `MONGO_CLIENT` - Mongo client.
- `MONGO_DATABASE` - Mongo database.
- `DATABASE_NAME` - Batabase name.
- `SUPER_COLLECTION_NAME` - Super collection name.
- `MEDIA_ROOT` - Absolute filesystem path to the directory that will hold user-uploaded files.
- `MEDIA_URL` - URL that handles the media served from MEDIA_ROOT, used for managing stored files.
- `STATIC_ROOT` - The absolute path to the directory where static files are located.
- `STATIC_URL` - URL to use when referring to static files located in STATIC_ROOT.
- `UTC_TIMEZONE` - UTC timezone object.
- `REGEX` - Patterns of regular expression.
"""

from __future__ import annotations

__all__ = ("Config",)


import re
from datetime import tzinfo
from typing import ClassVar, final

from babel.dates import get_timezone
from pymongo import AsyncMongoClient
from pymongo.asynchronous.database import AsyncDatabase


@final
class Config:
    """Ramifice settings."""

    # Condition for the verification code.
    # For block the verification code, at the end of the migration to the database.
    DEBUG: ClassVar[bool] = True
    # Mongo client.
    MONGO_CLIENT: ClassVar[AsyncMongoClient | None] = None
    # Mongo database.
    MONGO_DATABASE: ClassVar[AsyncDatabase | None] = None
    # Database name.
    DATABASE_NAME: ClassVar[str | None] = None
    # Super collection name.
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
    # UTC timezone object.
    UTC_TIMEZONE: ClassVar[tzinfo] = get_timezone("UTC")
    # Patterns of regular expression.
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
