"""Caching metadata in Model.META"""

from datetime import datetime

from .errors import DoesNotMatchRegexError
from .store import REGEX
from .tools import date_parse, datetime_parse


def meta(
    service_name: str,
    fixture_name: str | None = None,
    db_query_docs_limit: int = 1000,
    is_migrat_model: bool = True,
    is_create_doc: bool = True,
    is_update_doc: bool = True,
    is_delete_doc: bool = True,
):
    """Caching metadata in Model.META"""

    def decorator(cls):
        if not bool(cls.META):
            model = cls()
            if REGEX["service_name"].match(service_name) is None:
                raise DoesNotMatchRegexError("^[A-Z][a-zA-Z0-9]{0,24}$")
            #
            cls.META = {
                "service_name": service_name,
                "fixture_name": fixture_name,
                "db_query_docs_limit": db_query_docs_limit,
                "is_migrat_model": is_migrat_model,
                "is_create_doc": is_create_doc,
                "is_update_doc": is_update_doc,
                "is_delete_doc": is_delete_doc,
            }
            caching(cls, model)
        return cls

    return decorator


def caching(cls, model) -> None:
    """Add metadata to Model.META."""
    model_name = model.model_name()
    if REGEX["model_name"].match(model_name) is None:
        raise DoesNotMatchRegexError("^[A-Z][a-zA-Z0-9]{0,24}$")
    #
    cls.META["model_name"] = model_name
    cls.META["full_model_name"] = model.full_model_name()
    cls.META["collection_name"] = f"{cls.META["service_name"]}_{model_name}"
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
    for f_name, f_type in model.__dict__.items():
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
    cls.META["field_name_and_type"] = field_name_and_type
    cls.META["field_attrs"] = field_attrs
    cls.META["data_dynamic_fields"] = data_dynamic_fields
    cls.META["count_all_fields"] = count_all_fields
    cls.META["count_fields_for_migrating"] = count_fields_for_migrating
