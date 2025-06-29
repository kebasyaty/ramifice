"""Tool of Commons - A set of auxiliary methods."""

import json
from typing import Any

from babel.dates import format_date, format_datetime

from ..utils import translations


def correct_mongo_filter(cls_model: Any, filter: Any) -> Any:
    """Correcting filter of request.

    Corrects `TextField` fields that require localization of translation.
    """
    lang: str = translations.CURRENT_LOCALE
    filter_json: str = json.dumps(filter)
    filter_json = (
        cls_model.META["regex_mongo_filter"]
        .sub(rf'\g<field>.{lang}":', filter_json)
        .replace('":.', ".")
    )
    return json.loads(filter_json)


def password_to_none(
    field_name_and_type: dict[str, str],
    mongo_doc: dict[str, Any],
) -> dict[str, Any]:
    """Create object instance from Mongo document."""
    for f_name, t_name in field_name_and_type.items():
        if "PasswordField" == t_name:
            mongo_doc[f_name] = None
    return mongo_doc


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
    lang: str = translations.CURRENT_LOCALE
    for f_name, t_name in field_name_and_type.items():
        value = mongo_doc[f_name]
        if value is not None:
            if t_name == "TextField":
                value = value.get(lang, "") if value is not None else None
            elif "Date" in t_name:
                if "Time" in t_name:
                    value = format_datetime(
                        datetime=value,
                        format="short",
                        locale=lang,
                    )
                else:
                    value = format_date(
                        date=value.date(),
                        format="short",
                        locale=lang,
                    )
            elif t_name == "IDField":
                value = str(value)
            elif t_name == "PasswordField":
                value = None
        doc[f_name] = value
    return doc
