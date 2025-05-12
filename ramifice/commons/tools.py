"""Tools - A set of additional auxiliary methods for Commons."""

from typing import Any


class ToolMixin:
    """A set of additional auxiliary methods for Commons."""

    @classmethod
    def from_doc(cls, mongo_doc: dict[str, Any]) -> Any:
        """Create object instance from Mongo document."""
        obj = cls()
        for name, data in mongo_doc.items():
            field = obj.__dict__[name]
            field.value = data if field.group != "pass" else None

        return obj
