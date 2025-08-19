"""Tool of Paladins - A set of auxiliary methods."""

from __future__ import annotations

__all__ = (
    "ignored_fields_to_none",
    "refresh_from_mongo_doc",
    "panic_type_error",
    "accumulate_error",
    "check_uniqueness",
)

import logging
from typing import Any

from ramifice.utils import errors, translations

logger = logging.getLogger(__name__)


def ignored_fields_to_none(inst_model: Any) -> None:
    """Reset the values of ignored fields to None."""
    for _, field_data in inst_model.__dict__.items():
        if not callable(field_data) and field_data.ignored:
            field_data.value = None


def refresh_from_mongo_doc(inst_model: Any, mongo_doc: dict[str, Any]) -> None:
    """Update object instance from Mongo document."""
    lang: str = translations.CURRENT_LOCALE
    model_dict = inst_model.__dict__
    for name, data in mongo_doc.items():
        field = model_dict[name]
        if field.field_type == "TextField" and field.multi_language:
            field.value = data.get(lang, "- -") if data is not None else None
        elif field.group == "pass":
            field.value = None
        else:
            field.value = data


def panic_type_error(value_type: str, params: dict[str, Any]) -> None:
    """Unacceptable type of value."""
    msg = (
        f"Model: `{params['full_model_name']}` > "
        + f"Field: `{params['field_data'].name}` > "
        + f"Parameter: `value` => Must be `{value_type}` type!"
    )
    logger.critical(msg)
    raise errors.PanicError(msg)


def accumulate_error(err_msg: str, params: dict[str, Any]) -> None:
    """Accumulating errors to ModelName.field_name.errors ."""
    if not params["field_data"].hide:
        params["field_data"].errors.append(err_msg)
        if not params["is_error_symptom"]:
            params["is_error_symptom"] = True
    else:
        msg = (
            f">>hidden field<< -> Model: `{params['full_model_name']}` > "
            + f"Field: `{params['field_data'].name}`"
            + f" => {err_msg}"
        )
        logger.critical(msg)
        raise errors.PanicError(msg)


async def check_uniqueness(
    value: str | int | float,
    params: dict[str, Any],
    field_name: str | None = None,
    is_multi_language: bool = False,
) -> bool:
    """Checking the uniqueness of the value in the collection."""
    q_filter = None
    if is_multi_language:
        lang_filter = [{f"{field_name}.{lang}": value} for lang in translations.LANGUAGES]
        q_filter = {
            "$and": [
                {"_id": {"$ne": params["doc_id"]}},
                {"$or": lang_filter},
            ],
        }
    else:
        q_filter = {
            "$and": [
                {"_id": {"$ne": params["doc_id"]}},
                {field_name: value},
            ],
        }
    return await params["collection"].find_one(q_filter) is None
