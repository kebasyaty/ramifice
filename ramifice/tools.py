"""A collection of auxiliary tools."""

import json
from datetime import datetime
from typing import Any

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


class MixinJSON:
    """Complect of methods for converting custom object to JSON and back to an object."""

    def to_dict(self) -> dict[str, Any]:
        """Convert object instance to a dictionary."""
        json_dict: dict[str, Any] = {}
        for f_name, f_type in self.__dict__.items():
            f_name = f_name.rsplit("__", maxsplit=1)[-1]
            if not callable(f_type):
                if f_type.__dict__.get("to_dict") is None:
                    json_dict[f_name] = f_type
                else:
                    json_dict[f_name] = f_type.to_dict()
        return json_dict

    @classmethod
    def from_dict(cls, json_dict: dict[str, Any]) -> Any:
        """Convert JSON string to a object instance."""
        obj = cls()
        for f_name, f_type in json_dict.items():
            if not isinstance(f_type, dict):
                obj.__dict__[f_name] = f_type
            else:
                obj.__dict__[f_name] = cls.from_dict(f_type)
        return obj

    def to_json(self):
        """Convert object instance to a JSON string."""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Any:
        """Convert JSON string to a object instance."""
        json_dict = json.loads(json_str)
        return cls.from_dict(json_dict)
