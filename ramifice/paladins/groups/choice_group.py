"""Group for checking choice fields.
Supported fields:
ChoiceTextMultField | ChoiceTextMultDynField | ChoiceTextField
| ChoiceTextDynField | ChoiceIntMultField | ChoiceIntMultDynField
| ChoiceIntField | ChoiceIntDynField | ChoiceFloatMultField
| ChoiceFloatMultDynField | ChoiceFloatField | ChoiceFloatDynField
"""

from typing import Any


class ChoiceGroupMixin:
    """Group for checking choice fields.
    Supported fields:
    ChoiceTextMultField | ChoiceTextMultDynField | ChoiceTextField
    | ChoiceTextDynField | ChoiceIntMultField | ChoiceIntMultDynField
    | ChoiceIntField | ChoiceIntDynField | ChoiceFloatMultField
    | ChoiceFloatMultDynField | ChoiceFloatField | ChoiceFloatDynField
    """

    def choice_group(self, params: dict[str, Any]) -> None:
        """Checking choice fields."""
