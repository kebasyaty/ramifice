"""Ramifice - Global collection of auxiliary methods."""

__all__ = (
    "is_password",
    "to_human_size",
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
import math
from asyncio import to_thread
from os.path import getsize
from typing import Any
from urllib.parse import urlparse

import phonenumbers
from bson.objectid import ObjectId
from email_validator import EmailNotValidError, validate_email

from ramifice.utils.constants import REGEX


def is_password(password: str | None) -> bool:
    """Ramifice - Validate Password."""
    if not REGEX["password"].match(str(password)):
        return False
    return True


def to_human_size(size: int) -> str:
    """Ramifice - Convert number of bytes to readable format."""
    idx = int(math.floor(math.log(size) / math.log(1024)))
    size = size if size < 1024 else abs(round(size / pow(1024, idx), 2))
    order = ["bytes", "KB", "MB", "GB", "TB"][idx]
    return f"{size} {order}"


async def get_file_size(path: str) -> int:
    """Ramifice - Get file size in bytes."""
    size: int = await to_thread(getsize, path)
    return size


def normal_email(email: str | None) -> str | None:
    """Ramifice - Normalizing email address.

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
    """Ramifice - Validate Email address."""
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
    """Ramifice - Validate URL address."""
    result = urlparse(str(url))
    if not result.scheme or not result.netloc:
        return False
    return True


def is_ip(address: str | int | None) -> bool:
    """Ramifice - Validate IP address."""
    try:
        ipaddress.ip_address(str(address))
    except ValueError:
        return False
    return True


def is_color(color_code: str | None) -> bool:
    """Ramifice - Validate Color code."""
    if REGEX["color_code"].match(str(color_code)) is None:
        return False
    return True


def is_phone(number: str | None) -> bool:
    """Ramifice - Validate Phone number."""
    try:
        phone = phonenumbers.parse(str(number))
        if not phonenumbers.is_valid_number(phone):
            return False
    except phonenumbers.phonenumberutil.NumberParseException:
        return False
    return True


def is_mongo_id(oid: Any) -> bool:
    """Ramifice - Validation of the Mongodb identifier."""
    return ObjectId.is_valid(oid)


def hash_to_obj_id(hash: str | None) -> ObjectId | None:
    """Ramifice - Get ObjectId from hash string."""
    return ObjectId(hash) if bool(hash) else None
