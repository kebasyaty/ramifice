"""Caching metadata in Model.META"""

from .errors import DoesNotMatchRegexError
from .store import REGEX


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
        if cls.__dict__.get("META") is None:
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
            caching(cls)
        return cls

    return decorator


def caching(cls) -> None:
    """Add metadata to Model.META."""
    model = cls()
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
    # ???
    count_all_fields = 0
    #
    for f_name, f_type in model.__dict__.items():
        if not callable(f_type):
            count_all_fields += 1
            f_name = f_name.split("__")[-1]
            f_type_str = f_type.__class__.__name__
            field_attrs[f_name] = {
                "id": f"{model_name}--{f_name.replace("_", "-")}",
                "name": f_name,
            }
            if not f_type.ignored:
                field_name_and_type_list[f_name] = f_type_str
                field_name_params_list[f_name] = {
                    "type": f_type_str,
                    "group": f_type.group,
                }
                if "Dyn" in f_name:
                    data_dynamic_fields[f_name] = None
    #
    cls.META["field_name_and_type_list"] = field_name_and_type_list
    cls.META["field_name_params_list"] = field_name_params_list
    cls.META["field_attrs"] = field_attrs
    cls.META["data_dynamic_fields"] = data_dynamic_fields
    cls.META["count_all_fields"] = count_all_fields
