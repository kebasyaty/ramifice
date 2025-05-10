"""Tools - A set of additional auxiliary methods for Commons."""

from typing import Any

from ..types import FileData, ImageData


class ToolMixin:
    """A set of additional auxiliary methods for Commons."""

    @classmethod
    def from_doc(cls, mongo_doc: dict[str, Any]) -> Any:
        """Create object instance from Mongo document."""
        obj = cls()
        for name, data in mongo_doc.items():
            if data is None:
                continue
            if name == "_id":
                obj.__dict__["hash"].value = str(data)
                continue
            field = obj.__dict__[name]
            if field.group != "pass":
                if field.group == "date":
                    if field.input_type == "date":
                        data = data.strftime("%Y-%m-%d")
                    else:
                        data = data.strftime("%Y-%m-%dT%H:%M:%S")
                elif field.group == "file":
                    data = FileData.from_doc(data)
                elif field.group == "img":
                    data = ImageData.from_doc(data)
                field.value = data
            else:
                field.value = None
        return obj
