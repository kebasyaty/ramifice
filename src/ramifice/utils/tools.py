"""Global collection of auxiliary methods."""

from __future__ import annotations

__all__ = (
    "is_password",
    "get_file_size",
    "normal_email",
    "is_email",
    "is_url",
    "is_ip",
    "is_color",
    "is_phone",
    "is_mongo_id",
    "hash_to_obj_id",
)

import ipaddress
from asyncio import to_thread
from os.path import getsize
from typing import Any
from urllib.parse import urlparse

import phonenumbers
from bson.objectid import ObjectId
from email_validator import EmailNotValidError, validate_email

from ramifice.utils.constants import REGEX


def is_password(password: str | None) -> bool:
    """Validate Password."""
    return REGEX["password"].match(str(password)) is not None


async def get_file_size(path: str) -> int:
    """Get file size in bytes."""
    size: int = await to_thread(getsize, path)
    return size


def normal_email(email: str | None) -> str | None:
    """Normalizing email address.

    Use this before requeste to a database.
    For example, on the login page.
    """
    normal: str | None = None
    try:
        emailinfo = validate_email(
            str(email),
            check_deliverability=False,
        )
        normal = emailinfo.normalized
    except EmailNotValidError:
        pass
    return normal


async def is_email(email: str | None) -> bool:
    """Validate Email address."""
    try:
        await to_thread(
            validate_email,
            str(email),
            check_deliverability=True,
        )
    except EmailNotValidError:
        return False
    return True


def is_url(url: str | None) -> bool:
    """Validate URL address."""
    result = urlparse(str(url))
    return not (not result.scheme or not result.netloc)


def is_ip(address: str | int | None) -> bool:
    """Validate IP address."""
    try:
        ipaddress.ip_address(str(address))
    except ValueError:
        return False
    return True


def is_color(color_code: str | None) -> bool:
    """Validate Color code."""
    return REGEX["color_code"].match(str(color_code)) is not None


def is_phone(number: str | None) -> bool:
    """Validate Phone number."""
    try:
        phone = phonenumbers.parse(str(number))
        if not phonenumbers.is_valid_number(phone):
            return False
    except phonenumbers.phonenumberutil.NumberParseException:
        return False
    return True


def is_mongo_id(oid: Any) -> bool:
    """Validation of the Mongodb identifier."""
    return ObjectId.is_valid(oid)


def hash_to_obj_id(hash: str | None) -> ObjectId | None:
    """Get ObjectId from hash string."""
    return ObjectId(hash) if bool(hash) else None
