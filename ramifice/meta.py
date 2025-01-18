"""Model parameters."""

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
    """Model parameters."""

    def decorator(cls):
        if cls.__dict__.get("META") is None:
            cls.META = {
                "service_name": service_name,
                "fixture_name": fixture_name,
                "db_query_docs_limit": db_query_docs_limit,
                "is_migrat_model": is_migrat_model,
                "is_create_doc": is_create_doc,
                "is_update_doc": is_update_doc,
                "is_delete_doc": is_delete_doc,
            }
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
