"""Group for checking id fields.
Supported fields: IDField
"""

from typing import Any

from bson.objectid import ObjectId

from ... import translations


class IDGroupMixin:
    """Group for checking id fields.
    Supported fields: IDField
    """

    def id_group(self, params: dict[str, Any]) -> None:
        """Checking id fields."""
        field = params["field_data"]
        gettext = translations.gettext
        # Get current value.
        value = field.value or None
        if value is None:
            if field.required:
                err_msg = gettext("Required field !")
                self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
            if params["is_save"]:
                params["result_map"][field.name] = None
            return
        # Validation of the MongoDB identifier in a string form.
        if not ObjectId.is_valid(value):
            err_msg = gettext("Invalid document ID !")
            self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
        # Insert result.
        if params["is_save"]:
            params["result_map"][field.name] = value
