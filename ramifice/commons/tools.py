"""Tools - A set of additional auxiliary methods for Commons."""

from typing import Any

from babel.dates import format_date, format_datetime
from dateutil.parser import parse

from ..translations import CURRENT_LOCALE


class ToolMixin:
    """A set of additional auxiliary methods for Commons."""

    @classmethod
    def password_to_none(cls, mongo_doc: dict[str, Any]) -> dict[str, Any]:
        """Create object instance from Mongo document."""
        for f_name, t_name in cls.META["field_name_and_type"].items():  # type: ignore[index, attr-defined]
            if "Pass" in t_name:
                mongo_doc[f_name] = None
        return mongo_doc

    @classmethod
    def from_mongo_doc(cls, mongo_doc: dict[str, Any]) -> Any:
        """Create object instance from Mongo document."""
        obj = cls()
        for name, data in mongo_doc.items():
            field = obj.__dict__[name]
            field.value = data if field.group != "pass" else None
        return obj

    @classmethod
    def mongo_doc_to_raw_doc(cls, mongo_doc: dict[str, Any]) -> dict[str, Any]:
        """Convert the Mongo document to the raw document.
        Special changes:
        _id to str
        password to None
        date to str
        datetime to str
        """
        doc: dict[str, Any] = {}
        for f_name, t_name in cls.META["field_name_and_type"].items():  # type: ignore[index, attr-defined]
            value = mongo_doc[f_name]
            if value is not None:
                if "Date" in t_name:
                    if "Time" in t_name:
                        value = format_datetime(
                            value, format="short", locale=CURRENT_LOCALE
                        )
                    else:
                        value = format_date(
                            value, format="short", locale=CURRENT_LOCALE
                        )
                elif "ID" in t_name:
                    value = str(value)
                elif "Pass" in t_name:
                    value = None
            doc[f_name] = value
        return doc
