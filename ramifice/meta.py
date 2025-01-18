"""Model parameters."""


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
