"""Tool of Paladins - A set of auxiliary methods."""

from typing import Any

from ..errors import PanicError


def ignored_fields_to_none(inst_model: Any) -> None:
    """Reset the values of ignored fields to None."""
    for _, field_data in inst_model.__dict__.items():
        if not callable(field_data) and field_data.ignored and field_data.name != "_id":
            field_data.value = None


def refresh_from_mongo_doc(inst_model: Any, mongo_doc: dict[str, Any]) -> None:
    """Update object instance from Mongo document."""
    for name, data in mongo_doc.items():
        field = inst_model.__dict__[name]
        field.value = data if field.group != "pass" else None


def panic_type_error(value_type: str, params: dict[str, Any]) -> None:
    """Unacceptable type of value."""
    msg = (
        f"Model: `{params['full_model_name']}` > "
        + f"Field: `{params['field_data'].name}` > "
        + f"Parameter: `value` => Must be `{value_type}` type!"
    )
    raise PanicError(msg)


def accumulate_error(err_msg: str, params: dict[str, Any]) -> None:
    """For accumulating errors to ModelName.field_name.errors ."""
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
        raise PanicError(msg)


async def check_uniqueness(
    value: str | int | float,
    params: dict[str, Any],
) -> bool:
    """Check the uniqueness of the value in the collection."""
    if not params["is_migrate_model"]:
        return True
    q_filter = {
        "$and": [
            {"_id": {"$ne": params["doc_id"]}},
            {params["field_data"].name: value},
        ],
    }
    return await params["collection"].find_one(q_filter) is None
