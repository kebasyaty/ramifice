"""A collection of auxiliary tools."""

import ipaddress
from datetime import datetime
from typing import Any
from urllib.parse import urlparse

import phonenumbers
from bson.objectid import ObjectId
from email_validator import EmailNotValidError, validate_email

from .errors import InvalidDateError, InvalidDateTimeError
from .store import REGEX


def date_parse(date: str) -> datetime:
    """Converting a string with Date to object `datetime`.
    Formats: dd-mm-yyyy | dd/mm/yyyy | dd.mm.yyyy |
             yyyy-mm-dd | yyyy/mm/dd | yyyy.mm.dd
    """
    md = REGEX["date_parse"].match(date) or REGEX["date_parse_reverse"].match(date)
    if md is None:
        raise InvalidDateError()
    dt = datetime.strptime(
        f"{md.group('y')}-{md.group('m')}-{md.group('d')}", "%Y-%m-%d"
    )
    return dt


def datetime_parse(date_time: str) -> datetime:
    """Converting a string with Date and Time to the object `datetime`.
    Formats: dd-mm-yyyy hh:mm:ss | dd/mm/yyyy hh:mm:ss | dd.mm.yyyy hh:mm:ss |
             dd-mm-yyyyThh:mm:ss | dd/mm/yyyyThh:mm:ss | dd.mm.yyyyThh:mm:ss |
             yyyy-mm-dd hh:mm:ss | yyyy/mm/dd hh:mm:ss | yyyy.mm.dd hh:mm:ss |
             yyyy-mm-ddThh:mm:ss | yyyy/mm/ddThh:mm:ss | yyyy.mm.ddThh:mm:ss
    """
    md = REGEX["datetime_parse"].match(date_time) or REGEX[
        "datetime_parse_reverse"
    ].match(date_time)
    if md is None:
        raise InvalidDateTimeError()
    dt = datetime.strptime(
        f"{md.group('y')}-{md.group('m')}-{md.group('d')}T{md.group('t')}",
        "%Y-%m-%dT%H:%M:%S",
    )
    return dt


def normal_email(email: str | bytes) -> str | None:
    """Normalizing email address."""
    normal: str | None = None
    try:
        emailinfo = validate_email(email, check_deliverability=False)
        normal = emailinfo.normalized
    except EmailNotValidError:
        pass
    return normal


def is_email(email: str | bytes) -> bool:
    """Validate Email address."""
    flag = True
    try:
        validate_email(email, check_deliverability=True)
    except EmailNotValidError:
        flag = False
    return flag


def is_url(url: str) -> bool:
    """Validate URL address."""
    flag = True
    result = urlparse(url)
    if not result.scheme or not result.netloc:
        flag = False
    return flag


def is_ip(address: str | int) -> bool:
    """Validate IP address."""
    flag = True
    try:
        ipaddress.ip_address(address)
    except ValueError:
        flag = False
    return flag


def is_color(color_code: str) -> bool:
    """Validate Color code."""
    flag = True
    if REGEX["color_code"].match(color_code) is None:
        flag = False
    return flag


def is_phone(number: str) -> bool:
    """Validate Phone number."""
    flag = True
    try:
        phone = phonenumbers.parse(number)
        if not phonenumbers.is_valid_number(phone):
            flag = False
    except phonenumbers.phonenumberutil.NumberParseException:
        flag = False
    return flag


def is_mongo_id(oid: Any) -> bool:
    """Validation of the Mongodb identifier."""
    return ObjectId.is_valid(oid)
