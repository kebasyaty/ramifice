"""General purpose instrument set."""

from datetime import datetime
from .store import REGEX
from ..errors import InvalidDate


def date_parse(date: str) -> datetime:
    """Converting string Date to object `datetime`.
    Formats: dd-mm-yyyy | dd/mm/yyyy | dd.mm.yyyy |
             yyyy-mm-dd | yyyy/mm/dd | yyyy.mm.dd
    """
    md = REGEX['date_parse'].match(
        date) or REGEX['date_parse_reverse'].match(date)
    if md is None:
        raise InvalidDate()
    dt = datetime.strptime(
        f'{md.group('y')}-{md.group('m')}-{md.group('d')}', '%Y-%m-%d')
    return dt
