"""Group for checking choice fields.

Supported fields:
    ChoiceTextMultField | ChoiceTextMultDynField | ChoiceTextField
    | ChoiceTextDynField | ChoiceIntMultField | ChoiceIntMultDynField
    | ChoiceIntField | ChoiceIntDynField | ChoiceFloatMultField
    | ChoiceFloatMultDynField | ChoiceFloatField | ChoiceFloatDynField
"""

from typing import Any

from ...utils import translations
from ..tools import accumulate_error


class ChoiceGroupMixin:
    """Group for checking choice fields.

    Supported fields:
            ChoiceTextMultField | ChoiceTextMultDynField | ChoiceTextField
            ChoiceTextDynField | ChoiceIntMultField | ChoiceIntMultDynField
            ChoiceIntField | ChoiceIntDynField | ChoiceFloatMultField
            ChoiceFloatMultDynField | ChoiceFloatField | ChoiceFloatDynField
    """

    def choice_group(self, params: dict[str, Any]) -> None:
        """Checking choice fields."""
        field = params["field_data"]
        # Get current value.
        value = field.value or field.__dict__.get("default") or None

        if value is None:
            if field.required:
                err_msg = translations._("Required field !")
                accumulate_error(err_msg, params)
            if params["is_save"]:
                params["result_map"][field.name] = None
            return
        # Does the field value match the possible options in choices.
        if not field.has_value(is_migrat=params["is_migration_process"]):
            err_msg = translations._("Your choice does not match the options offered !")
            accumulate_error(err_msg, params)
        # Insert result.
        if params["is_save"]:
            params["result_map"][field.name] = value
