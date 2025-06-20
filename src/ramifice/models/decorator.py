"""Decorator for converting Python classes into Ramifice models."""

import os
from typing import Any

from .. import translations
from ..add_valid import AddValidMixin
from ..commons import QCommonsMixin
from ..errors import DoesNotMatchRegexError, PanicError
from ..fields import DateTimeField, IDField  # type: ignore[attr-defined]
from ..hooks import HooksMixin
from ..indexing import IndexMixin
from ..paladins import CheckMixin, QPaladinsMixin, ValidationMixin  # type: ignore[attr-defined]
from ..store import REGEX
from .model import Model
from .pseudo import PseudoModel


def model(
    service_name: str,
    fixture_name: str | None = None,
    db_query_docs_limit: int = 1000,
    is_migrate_model: bool = True,
    is_create_doc: bool = True,
    is_update_doc: bool = True,
    is_delete_doc: bool = True,
) -> Any:
    """Decorator for converting Python Classe into Ramifice Model."""
    if not isinstance(service_name, str):
        raise AssertionError("Parameter `service_name` - Must be `str` type!")
    if not isinstance(fixture_name, (str, type(None))):
        raise AssertionError("Parameter `fixture_name` - Must be `str | None` type!")
    if not isinstance(db_query_docs_limit, int):
        raise AssertionError("Parameter `db_query_docs_limit` - Must be `int` type!")
    if not isinstance(is_migrate_model, bool):
        raise AssertionError("Parameter `is_migrate_model` - Must be `bool` type!")
    if not isinstance(is_create_doc, bool):
        raise AssertionError("Parameter `is_create_doc` - Must be `bool` type!")
    if not isinstance(is_update_doc, bool):
        raise AssertionError("Parameter `is_update_doc` - Must be `bool` type!")
    if not isinstance(is_delete_doc, bool):
        raise AssertionError("Parameter `is_delete_doc` - Must be `bool` type!")

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
        if is_migrate_model:
            attrs["__dict__"] = Model.__dict__["__dict__"]
        else:
            attrs["__dict__"] = PseudoModel.__dict__["__dict__"]
        metadata = {
            "service_name": service_name,
            "fixture_name": fixture_name,
            "db_query_docs_limit": db_query_docs_limit,
            "is_migrate_model": is_migrate_model,
            "is_create_doc": is_create_doc if is_migrate_model else False,
            "is_update_doc": is_update_doc if is_migrate_model else False,
            "is_delete_doc": is_delete_doc if is_migrate_model else False,
        }
        attrs["META"] = {
            **metadata,
            **caching(cls, service_name, is_migrate_model),
        }

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
            return type(
                cls.__name__,
                (
                    PseudoModel,
                    ValidationMixin,
                    CheckMixin,
                    AddValidMixin,
                ),
                attrs,
            )

    return decorator


def caching(cls: Any, service_name: str, is_migrate_model: bool) -> dict[str, Any]:
    """Add additional metadata to `Model.META`."""
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
    count_fields_no_ignored = 0

    raw_model = cls()
    raw_model.fields()
    default_fields: dict[str, Any] = {}
    if is_migrate_model:
        default_fields["_id"] = IDField()
        default_fields["created_at"] = DateTimeField()
        default_fields["updated_at"] = DateTimeField()
    fields = {**raw_model.__dict__, **default_fields}
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
                if is_migrate_model:
                    count_fields_no_ignored += 1
                # Get a dictionary of field names and types.
                field_name_and_type[f_name] = f_type_str
                # Build data migration storage for dynamic fields.
                if "Dyn" in f_type.field_type:
                    if not is_migrate_model:
                        msg = (
                            f"Model: `{cls.__module__}.{model_name}` > "
                            + f"Field: `{f_name}` => "
                            + "Dynamic field only for a migrated Model."
                        )
                        raise PanicError(msg)
                    data_dynamic_fields[f_name] = None

    metadata["field_name_and_type"] = field_name_and_type
    metadata["field_attrs"] = field_attrs
    metadata["data_dynamic_fields"] = data_dynamic_fields
    metadata["count_all_fields"] = count_all_fields
    metadata["count_fields_no_ignored"] = count_fields_no_ignored

    return metadata
