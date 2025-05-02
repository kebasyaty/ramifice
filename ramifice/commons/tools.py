"""Tools - A set of additional auxiliary methods for Commons."""

from datetime import datetime
from typing import Any

from ..types import FileData, ImageData


class ToolsMixin:
    """A set of additional auxiliary methods for Commons."""

    @classmethod
    def from_doc(cls, mongo_doc: dict[str, Any]) -> Any:
        """Convert Mongo document to a object instance."""
        obj = cls()
        for name, data in mongo_doc.items():
            if data is None:
                continue
            field = obj.__dict__[name]
            if field.group != "pass":
                if name != "_id":
                    if field.group == "date":
                        if field.input_type == "date":
                            data = data.strftime("%Y-%m-%d")
                        else:
                            data = data.strftime("%Y-%m-%dT%H:%M:%S")
                    elif field.group == "file":
                        data = FileData.from_doc(data)
                    elif field.group == "img":
                        data = ImageData.from_doc(data)
                else:
                    data = str(data)
                field.value = data
        return obj
