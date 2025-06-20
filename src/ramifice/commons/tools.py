"""Tool of Commons - A set of auxiliary methods."""

from typing import Any

from babel.dates import format_date, format_datetime

from ..utils import translations


def password_to_none(
    field_name_and_type: dict[str, str],
    mongo_doc: dict[str, Any],
) -> dict[str, Any]:
    """Create object instance from Mongo document."""
    for f_name, t_name in field_name_and_type.items():
        if "Pass" in t_name:
            mongo_doc[f_name] = None
    return mongo_doc


def from_mongo_doc(
    cls_model: Any,
    mongo_doc: dict[str, Any],
) -> Any:
    """Create object instance from Mongo document."""
    obj = cls_model()
    for name, data in mongo_doc.items():
        field = obj.__dict__[name]
        field.value = data if field.group != "pass" else None
    return obj


def mongo_doc_to_raw_doc(
    field_name_and_type: dict[str, str],
    mongo_doc: dict[str, Any],
) -> dict[str, Any]:
    """Convert the Mongo document to the raw document.

    Special changes:
        _id to str
        password to None
        date to str
        datetime to str
    """
    doc: dict[str, Any] = {}
    current_locale = translations.CURRENT_LOCALE
    for f_name, t_name in field_name_and_type.items():
        value = mongo_doc[f_name]
        if value is not None:
            if "Date" in t_name:
                if "Time" in t_name:
                    value = format_datetime(
                        datetime=value,
                        format="short",
                        locale=current_locale,
                    )
                else:
                    value = format_date(
                        date=value.date(),
                        format="short",
                        locale=current_locale,
                    )
            elif "ID" in t_name:
                value = str(value)
            elif "Pass" in t_name:
                value = None
        doc[f_name] = value
    return doc
