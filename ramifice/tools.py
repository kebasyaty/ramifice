"""A collection of auxiliary tools."""

import ipaddress
from datetime import datetime
from urllib.parse import urlparse

import phonenumbers
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


def is_email(value: str) -> bool:
    """Validate Email address."""
    flag = True
    try:
        validate_email(value, check_deliverability=True)
    except EmailNotValidError:
        flag = False
    return flag


def is_url(value: str) -> bool:
    """Validate URL address."""
    flag = True
    result = urlparse(value)
    if not result.scheme or not result.netloc:
        flag = False
    return flag


def is_ip(value: str) -> bool:
    """Validate IP address."""
    flag = True
    try:
        ipaddress.ip_address(value)
    except ValueError:
        flag = False
    return flag


def is_color(value: str) -> bool:
    """Validate color code."""
    flag = True
    if REGEX["color_code"].match(value) is None:
        flag = False
    return flag


def is_phone(value: str) -> bool:
    """Validate Phone number."""
    flag = True
    phone = phonenumbers.parse(value)
    if not phonenumbers.is_valid_number(phone):
        flag = False
    return flag
