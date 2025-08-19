"""Tool of Commons - A set of auxiliary methods."""

from __future__ import annotations

__all__ = (
    "correct_mongo_filter",
    "password_to_none",
    "mongo_doc_to_raw_doc",
)

from typing import Any

from babel.dates import format_date, format_datetime
from bson import json_util

from ramifice.utils import translations


def correct_mongo_filter(cls_model: Any, filter: Any) -> Any:
    """Correcting filter of request.

    Corrects `TextField` fields that require localization of translation.
    """
    lang: str = translations.CURRENT_LOCALE
    filter_json: str = json_util.dumps(filter)
    filter_json = cls_model.META["regex_mongo_filter"].sub(rf'\g<field>.{lang}":', filter_json).replace('":.', ".")
    return json_util.loads(filter_json)


def password_to_none(
    field_name_and_type: dict[str, str],
    mongo_doc: dict[str, Any],
) -> dict[str, Any]:
    """Create object instance from Mongo document."""
    for f_name, t_name in field_name_and_type.items():
        if t_name == "PasswordField":
            mongo_doc[f_name] = None
    return mongo_doc


def mongo_doc_to_raw_doc(
    inst_model_dict: dict[str, Any],
    mongo_doc: dict[str, Any],
    lang: str,
) -> dict[str, Any]:
    """Convert the Mongo document to the raw document.

    Special changes:
        - `_id to str`
        - `password to None`
        - `date to str`
        - `datetime to str`
    """
    doc: dict[str, Any] = {}
    for f_name, f_data in inst_model_dict.items():
        field_type = f_data.field_type
        value = mongo_doc[f_name]
        if value is not None:
            if field_type == "TextField" and f_data.multi_language:
                value = value.get(lang, "- -") if value is not None else None
            elif "Date" in field_type:
                if "Time" in field_type:
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
            elif field_type == "IDField":
                value = str(value)
            elif field_type == "PasswordField":
                value = None
        doc[f_name] = value
    return doc
