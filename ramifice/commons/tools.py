"""Tools - A set of additional auxiliary methods for Commons."""

from typing import Any

from dateutil.parser import parse


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

    @classmethod
    def mongo_doc_to_model_doc(cls, mongo_doc: dict[str, Any]) -> dict[str, Any]:
        """Convert the Mongo document to the Model document."""
        doc: dict[str, Any] = {"_id": str(mongo_doc["_id"])}
        for f_name, t_name in cls.META["field_name_and_type"].items():  # type: ignore[index, attr-defined]
            value = mongo_doc[f_name]
            if value is not None:
                if "Date" in t_name:
                    if "Time" in t_name:
                        value = value.strftime("%Y-%m-%d %H:%M:%S")
                    else:
                        value = value.strftime("%Y-%m-%d")
                elif "Hash" in t_name:
                    value = str(value)
                elif "Pass" in t_name:
                    value = None
            doc[f_name] = value
        return doc
