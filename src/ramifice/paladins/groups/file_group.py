"""Group for checking file fields.

Supported fields: FileField
"""

from __future__ import annotations

__all__ = ("FileGroupMixin",)

from typing import Any

from xloft.converters import to_human_size

from ramifice.paladins.tools import (
    accumulate_error,
    panic_type_error,
)
from ramifice.utils import translations


class FileGroupMixin:
    """Group for checking file fields.

    Supported fields: FileField
    """

    async def file_group(self, params: dict[str, Any]) -> None:
        """Checking file fields."""
        field = params["field_data"]
        value = field.value or None

        if not isinstance(value, (dict, type(None))):
            panic_type_error("dict | None", params)

        if not params["is_update"] and value is None:
            default = field.default or None
            # If necessary, use the default value.
            if default is not None:
                params["field_data"].from_path(default)
                value = params["field_data"].value
            # Validation, if the field is required and empty, accumulate the error.
            # ( the default value is used whenever possible )
            if value is None:
                if field.required:
                    err_msg = translations._("Required field !")
                    accumulate_error(err_msg, params)
                if params["is_save"]:
                    params["result_map"][field.name] = None
                return
        # Return if the current value is missing
        if value is None:
            return
        if not value["save_as_is"]:
            # If the file needs to be delete.
            if value["is_delete"] and len(value["path"]) == 0:
                default = field.default or None
                # If necessary, use the default value.
                if default is not None:
                    params["field_data"].from_path(default)
                    value = params["field_data"].value
                else:
                    if not field.required:
                        if params["is_save"]:
                            params["result_map"][field.name] = None
                    else:
                        err_msg = translations._("Required field !")
                        accumulate_error(err_msg, params)
                    return
            # Accumulate an error if the file size exceeds the maximum value.
            if value["size"] > field.max_size:
                human_size = to_human_size(field.max_size)
                err_msg = translations._(
                    "File size exceeds the maximum value {} !",
                ).format(human_size)
                accumulate_error(err_msg, params)
                return
        # Insert result.
        if params["is_save"] and (value["is_new_file"] or value["save_as_is"]):
            value["is_delete"] = False
            value["save_as_is"] = True
            params["result_map"][field.name] = value
