"""Tools - A set of additional auxiliary methods for Commons."""

from typing import Any


class ToolsMixin:
    """A set of additional auxiliary methods for Commons."""

    @classmethod
    def from_doc(cls, mongo_doc: dict[str, Any]) -> Any:
        """Convert Mongo document to a object instance."""
        obj = cls()
        for name, data in mongo_doc.items():
            obj.__dict__[name] = data
        return obj
