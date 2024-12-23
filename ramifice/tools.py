"""A collection of auxiliary tools."""

from datetime import datetime

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
