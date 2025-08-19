"""Decorator for converting Python classes into Ramifice models."""

from __future__ import annotations

__all__ = ("model",)

import logging
import re
from pathlib import Path
from typing import Any

from ramifice.commons import QCommonsMixin
from ramifice.fields import DateTimeField, IDField
from ramifice.models.model import Model
from ramifice.paladins import QPaladinsMixin
from ramifice.utils.constants import REGEX
from ramifice.utils.errors import DoesNotMatchRegexError, PanicError

logger = logging.getLogger(__name__)


def model(
    service_name: str,
    fixture_name: str | None = None,
    db_query_docs_limit: int = 1000,
    is_create_doc: bool = True,
    is_update_doc: bool = True,
    is_delete_doc: bool = True,
) -> Any:
    """Decorator for converting Python Classe into Ramifice Model."""
    try:
        if not isinstance(service_name, str):
            msg = "Parameter `service_name` - Must be `str` type!"
            raise AssertionError(msg)
        if not isinstance(fixture_name, (str, type(None))):
            msg = "Parameter `fixture_name` - Must be `str | None` type!"
            raise AssertionError(msg)
        if not isinstance(db_query_docs_limit, int):
            msg = "Parameter `db_query_docs_limit` - Must be `int` type!"
            raise AssertionError(msg)
        if not isinstance(is_create_doc, bool):
            msg = "Parameter `is_create_doc` - Must be `bool` type!"
            raise AssertionError(msg)
        if not isinstance(is_update_doc, bool):
            msg = "Parameter `is_update_doc` - Must be `bool` type!"
            raise AssertionError(msg)
        if not isinstance(is_delete_doc, bool):
            msg = "Parameter `is_delete_doc` - Must be `bool` type!"
            raise AssertionError(msg)
    except AssertionError as err:
        logger.critical(str(err))
        raise err

    def decorator(cls: Any) -> Any:
        if REGEX["service_name"].match(service_name) is None:
            regex_str: str = "^[A-Z][a-zA-Z0-9]{0,24}$"
            msg = f"Does not match the regular expression: {regex_str}"
            logger.critical(msg)
            raise DoesNotMatchRegexError(regex_str)
        if fixture_name is not None:
            fixture_path = f"config/fixtures/{fixture_name}.yml"

            if not Path(fixture_path).exists():
                msg = (
                    f"Model: `{cls.__module__}.{cls.__name__}` > "
                    + "META param: `fixture_name` => "
                    + f"Fixture the `{fixture_path}` not exists!"
                )
                logger.critical(msg)
                raise PanicError(msg)

        attrs = dict(cls.__dict__)
        attrs["__dict__"] = Model.__dict__["__dict__"]
        metadata = {
            "service_name": service_name,
            "fixture_name": fixture_name,
            "db_query_docs_limit": db_query_docs_limit,
            "is_create_doc": is_create_doc,
            "is_update_doc": is_update_doc,
            "is_delete_doc": is_delete_doc,
        }
        attrs["META"] = {
            **metadata,
            **caching(cls, service_name),
        }

        return type(
            cls.__name__,
            (
                Model,
                QPaladinsMixin,
                QCommonsMixin,
            ),
            attrs,
        )

    return decorator


def caching(cls: Any, service_name: str) -> dict[str, Any]:
    """Add additional metadata to `Model.META`."""
    metadata: dict[str, Any] = {}
    model_name: str = cls.__name__
    if REGEX["model_name"].match(model_name) is None:
        regex_str: str = "^[A-Z][a-zA-Z0-9]{0,24}$"
        msg = f"Does not match the regular expression: {regex_str}"
        logger.critical(msg)
        raise DoesNotMatchRegexError(regex_str)
    #
    metadata["model_name"] = model_name
    metadata["full_model_name"] = f"{cls.__module__}.{model_name}"
    metadata["collection_name"] = f"{service_name}_{model_name}"
    # Get a dictionary of field names and types.
    # Format: <field_name, field_type>
    field_name_and_type: dict[str, str] = {}
    # Get attributes value for fields of Model: id, name.
    field_attrs: dict[str, dict[str, str]] = {}
    # Build data migration storage for dynamic fields.
    data_dynamic_fields: dict[str, dict[str, str | int | float] | None] = {}
    # Count all fields.
    count_all_fields: int = 0
    # Count fields for migrating.
    count_fields_no_ignored: int = 0
    # List of fields that support localization of translates.
    # Hint: `TextField`
    supported_lang_fields: list[str] = []

    raw_model = cls()
    raw_model.fields()
    default_fields: dict[str, Any] = {
        "_id": IDField(),
        "created_at": DateTimeField(),
        "updated_at": DateTimeField(),
    }
    fields = {**raw_model.__dict__, **default_fields}
    for f_name, f_data in fields.items():
        if not callable(f_data):
            f_type_str = f_data.__class__.__name__
            # Count all fields.
            count_all_fields += 1
            # Get attributes value for fields of Model: id, name.
            field_attrs[f_name] = {
                "id": f"{model_name}--{f_name.replace('_', '-') if f_name != '_id' else 'id'}",
                "name": f_name,
            }
            #
            if not f_data.ignored:
                # Count fields for migrating.
                count_fields_no_ignored += 1
                # Get a dictionary of field names and types.
                field_name_and_type[f_name] = f_type_str
                # Build data migration storage for dynamic fields.
                if "Dyn" in f_data.field_type:
                    data_dynamic_fields[f_name] = None
                if f_data.field_type == "TextField" and f_data.multi_language:
                    supported_lang_fields.append(f_name)

    metadata["field_name_and_type"] = field_name_and_type
    metadata["field_attrs"] = field_attrs
    metadata["data_dynamic_fields"] = data_dynamic_fields
    metadata["count_all_fields"] = count_all_fields
    metadata["count_fields_no_ignored"] = count_fields_no_ignored
    metadata["regex_mongo_filter"] = re.compile(rf'(?P<field>"(?:{"|".join(supported_lang_fields)})":)')

    return metadata
