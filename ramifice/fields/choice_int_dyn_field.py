"""Field of Model.
Type of selective integer field with dynamic addition of elements.
"""

import json
from typing import Any

from .general.choice_group import ChoiceGroup
from .general.field import Field


class ChoiceIntDynField(Field, ChoiceGroup):
    """Field of Model.
    Type of selective integer field with dynamic addition of elements.
    For simulate relationship Many-to-One.
    Element are (add|delete) via `ModelName.unit_manager(unit)` method.
    How to use, see <a href="https://github.com/kebasyaty/ramifice/tree/main/examples/dynamic_choices" target="_blank">example</a>.
    """

    def __init__(
        self,
        label: str = "",
        disabled: bool = False,
        hide: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        required: bool = False,
        readonly: bool = False,
    ):
        Field.__init__(
            self,
            label=label,
            disabled=disabled,
            hide=hide,
            ignored=ignored,
            hint=hint,
            warning=warning,
            field_type="ChoiceIntDynField",
            group="choice",
        )
        ChoiceGroup.__init__(
            self,
            required=required,
            readonly=readonly,
        )
        self.__value: int | None = None
        self.__choices: list[tuple[int, str]] | None = None

    @property
    def value(self) -> int | None:
        """Sets value of field."""
        return self.__value

    @value.setter
    def value(self, value: int | None) -> None:
        self.__value = value

    # --------------------------------------------------------------------------
    @property
    def choices(self) -> list[tuple[int, str]] | None:
        """Html tag: select.
        Example: [(1, 'Title'), (2, 'Title 2')]
        """
        return self.__choices

    # ---------------------------------------------------------------------------
    def has_value(self) -> bool:
        """Does the field value match the possible options in choices."""
        flag = True
        value = self.__value or None
        choices = self.__choices or None
        if value is not None and choices is not None:
            value_list = [
                item[0] for item in choices  # pylint: disable=not-an-iterable
            ]  # pylint: disable=not-an-iterable
            if value not in value_list:
                flag = False
        return flag

    # --------------------------------------------------------------------------
    def to_dict(
        self,
    ) -> dict[str, str | int | bool | list[str | int] | None]:
        """Convert fields to a dictionary."""
        json_dict: dict[str, str | int | bool | list[str | int] | None] = {}
        for f_name, f_type in self.__dict__.items():
            f_name = f_name.rsplit("__", maxsplit=1)[-1]
            if not callable(f_type):
                json_dict[f_name] = f_type
        return json_dict

    def to_json(self):
        """Convert a dictionary of fields to a JSON string."""
        return json.dumps(self.to_dict())
