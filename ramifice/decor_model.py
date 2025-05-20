"""Decorator for converting into a Model."""

import os
from typing import Any

from .errors import DoesNotMatchRegexError, PanicError
from .fake_model import FakeModel
from .model import Model
from .store import REGEX


# Decorator for converting into a Model.
def model(
    service_name: str,
    fixture_name: str | None = None,
    db_query_docs_limit: int = 1000,
    is_migrat_model: bool = True,
    is_create_doc: bool = True,
    is_update_doc: bool = True,
    is_delete_doc: bool = True,
):
    """Decorator for converting into a Model."""

    def decorator(cls):
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
        #
        attrs = {key: val for key, val in cls.__dict__.items()}
        attrs["META"] = {
            "service_name": service_name,
            "fixture_name": fixture_name,
            "db_query_docs_limit": db_query_docs_limit,
            "is_migrat_model": is_migrat_model,
            "is_create_doc": is_create_doc,
            "is_update_doc": is_update_doc,
            "is_delete_doc": is_delete_doc,
        }.update(caching(cls, service_name))
        #
        new_cls = None
        if is_migrat_model:
            attrs["__dict__"] = Model.__dict__["__dict__"]
            new_cls = type(cls.__name__, (Model,), attrs)
        else:
            attrs["__dict__"] = FakeModel.__dict__["__dict__"]
            new_cls = type(cls.__name__, (FakeModel,), attrs)
        #
        return new_cls

    return decorator


def caching(cls, service_name) -> dict[str, Any]:
    """Add metadata to Model.META."""
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
    #
    old_model = cls()
    old_model.fields()
    for f_name, f_type in old_model.__dict__.items():
        if not callable(f_type):
            f_type_str = f_type.__class__.__name__
            # Count all fields.
            count_all_fields += 1
            # Get attributes value for fields of Model: id, name.
            field_attrs[f_name] = {
                "id": f"{model_name}--{f_name.replace("_", "-") if f_name != '_id' else 'id'}",
                "name": f_name,
            }
            #
            if not f_type.ignored:
                # Count fields for migrating.
                count_fields_for_migrating += 1
                # Get a dictionary of field names and types.
                field_name_and_type[f_name] = f_type_str
                # Build data migration storage for dynamic fields.
                if "Dyn" in f_name:
                    data_dynamic_fields[f_name] = None
    #
    metadata["field_name_and_type"] = field_name_and_type
    metadata["field_attrs"] = field_attrs
    metadata["data_dynamic_fields"] = data_dynamic_fields
    metadata["count_all_fields"] = count_all_fields
    metadata["count_fields_for_migrating"] = count_fields_for_migrating
    #
    return metadata
