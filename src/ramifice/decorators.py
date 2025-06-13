"""Decorators."""

import os
from typing import Any

from . import translations
from .add_valid import AddValidMixin
from .commons import QCommonsMixin
from .errors import DoesNotMatchRegexError, PanicError
from .fields import DateTimeField, IDField  # type: ignore[attr-defined]
from .hooks import HooksMixin
from .indexing import IndexMixin
from .model import Model
from .paladins import CheckMixin, QPaladinsMixin, ToolMixin  # type: ignore[attr-defined]
from .store import REGEX


# Decorator for converting into a Model.
def model(
    service_name: str,
    fixture_name: str | None = None,
    db_query_docs_limit: int = 1000,
    is_migrate_model: bool = True,
    is_create_doc: bool = True,
    is_update_doc: bool = True,
    is_delete_doc: bool = True,
) -> Any:
    """Decorator for converting into a Model."""

    def decorator(cls: Any) -> Any:
        if REGEX["service_name"].match(service_name) is None:
            raise DoesNotMatchRegexError("^[A-Z][a-zA-Z0-9]{0,24}$")
        if fixture_name is not None:
            fixture_path = f"config/fixtures/{fixture_name}.yml"
            if not os.path.exists(fixture_path):
                msg = (
                    f"Model: `{cls.__module__}.{cls.__name__}` > "
                    + f"META param: `fixture_name` => "
                    + f"Fixture the `{fixture_path}` not exists!"
                )
                raise PanicError(msg)

        attrs = {key: val for key, val in cls.__dict__.items()}
        attrs["__dict__"] = Model.__dict__["__dict__"]
        metadata = {
            "service_name": service_name,
            "fixture_name": fixture_name,
            "db_query_docs_limit": db_query_docs_limit,
            "is_migrate_model": is_migrate_model,
            "is_create_doc": is_create_doc if is_migrate_model else False,
            "is_update_doc": is_update_doc if is_migrate_model else False,
            "is_delete_doc": is_delete_doc if is_migrate_model else False,
        }
        attrs["META"] = {**metadata, **caching(cls, service_name)}

        if is_migrate_model:
            return type(
                cls.__name__,
                (
                    Model,
                    QPaladinsMixin,
                    QCommonsMixin,
                    AddValidMixin,
                    IndexMixin,
                    HooksMixin,
                ),
                attrs,
            )
        else:
            return type(cls.__name__, (Model, ToolMixin, CheckMixin, AddValidMixin), attrs)

    return decorator


def caching(cls: Any, service_name: str) -> dict[str, Any]:
    """Get additional metadata for `Model.META`."""
    metadata: dict[str, Any] = {}
    model_name = cls.__name__
    if REGEX["model_name"].match(model_name) is None:
        raise DoesNotMatchRegexError("^[A-Z][a-zA-Z0-9]{0,24}$")
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
    count_all_fields = 0
    # Count fields for migrating.
    count_fields_for_migrating = 0

    old_model = cls()
    old_model.fields()
    default_fields: dict[str, Any] = {
        "_id": IDField(),
        "created_at": DateTimeField(),
        "updated_at": DateTimeField(),
    }
    fields = {**old_model.__dict__, **default_fields}
    for f_name, f_type in fields.items():
        if not callable(f_type):
            f_type_str = f_type.__class__.__name__
            # Count all fields.
            count_all_fields += 1
            # Get attributes value for fields of Model: id, name.
            field_attrs[f_name] = {
                "id": f"{model_name}--{f_name.replace('_', '-') if f_name != '_id' else 'id'}",
                "name": f_name,
            }
            #
            if not f_type.ignored:
                # Count fields for migrating.
                count_fields_for_migrating += 1
                # Get a dictionary of field names and types.
                field_name_and_type[f_name] = f_type_str
                # Build data migration storage for dynamic fields.
                if "Dyn" in f_type.field_type:
                    data_dynamic_fields[f_name] = None

    metadata["field_name_and_type"] = field_name_and_type
    metadata["field_attrs"] = field_attrs
    metadata["data_dynamic_fields"] = data_dynamic_fields
    metadata["count_all_fields"] = count_all_fields
    metadata["count_fields_for_migrating"] = count_fields_for_migrating

    return metadata
