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
    field_name_and_type_list: dict[str, str] = {}
    # Format: <field_name, <type: field_type, group: field_group>>
    field_name_params_list: dict[str, dict[str, str]] = {}
    # Get attributes value for fields of Model: id, name.
    field_attrs: dict[str, dict[str, str]] = {}
    # Build data migration storage for dynamic fields.
    data_dynamic_fields: dict[str, list[tuple[str | int | float, str]] | None] = {}
    # Count all fields.
    count_all_fields = 0
    # Count fields for migrating.
    count_fields_for_migrating = 0
    # Caching `datetime` objects for (date|date and time) fields.
    time_object_list: dict[str, dict[str, datetime | None]] = {}
    #
    for f_name, f_type in model.__dict__.items():
        if not callable(f_type):
            f_name = f_name.rsplit("__", maxsplit=1)[-1]
            f_type_str = f_type.__class__.__name__
            # Count all fields.
            count_all_fields += 1
            # Get attributes value for fields of Model: id, name.
            field_attrs[f_name] = {
                "id": f"{model_name}--{f_name.replace("_", "-")}",
                "name": f_name,
            }
            # Caching `datetime` objects for (date|date and time) fields.
            if "Date" in f_type_str:
                if "Time" in f_type_str:
                    dt_default = (
                        datetime_parse(f_type.default) if f_type.default else None
                    )
                    dt_max = (
                        datetime_parse(f_type.max_date) if f_type.max_date else None
                    )
                    dt_min = (
                        datetime_parse(f_type.min_date) if f_type.min_date else None
                    )
                    time_object_list[f_name] = {
                        "default": dt_default,
                        "max_date": dt_max,
                        "min_date": dt_min,
                    }
                else:
                    dt_default = date_parse(f_type.default) if f_type.default else None
                    dt_max = date_parse(f_type.max_date) if f_type.max_date else None
                    dt_min = date_parse(f_type.min_date) if f_type.min_date else None
                    time_object_list[f_name] = {
                        "default": dt_default,
                        "max_date": dt_max,
                        "min_date": dt_min,
                    }
            #
            if not f_type.ignored:
                # Count fields for migrating.
                count_fields_for_migrating += 1
                # Get a dictionary of field names and types.
                field_name_and_type_list[f_name] = f_type_str
                # Format: <field_name, <type: field_type, group: field_group>>
                field_name_params_list[f_name] = {
                    "type": f_type_str,
                    "group": f_type.group,
                }
                # Build data migration storage for dynamic fields.
                if "Dyn" in f_name:
                    data_dynamic_fields[f_name] = None
    #
    cls.META["field_name_and_type_list"] = field_name_and_type_list
    cls.META["field_name_params_list"] = field_name_params_list
    cls.META["field_attrs"] = field_attrs
    cls.META["data_dynamic_fields"] = data_dynamic_fields
    cls.META["count_all_fields"] = count_all_fields
    cls.META["count_fields_for_migrating"] = count_fields_for_migrating
    cls.META["time_object_list"] = time_object_list
