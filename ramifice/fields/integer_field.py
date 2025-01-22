"""Field of Model for enter (int) number."""

import json
from typing import Any

from ..store import DEBUG
from .general.field import Field
from .general.number_group import NumberGroup


class IntegerField(Field, NumberGroup):
    """Field of Model for enter (int) number."""

    def __init__(
        self,
        label: str = "",
        disabled: bool = False,
        hide: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        default: int | None = None,
        placeholder: str = "",
        required: bool = False,
        readonly: bool = False,
        unique: bool = False,
        max_number: int | None = None,
        min_number: int | None = None,
        step: int = 1,
        input_type: str = "number",  # number | range
    ):
        Field.__init__(
            self,
            label=label,
            disabled=disabled,
            hide=hide,
            ignored=ignored,
            hint=hint,
            warning=warning,
            field_type="IntegerField",
            group="integer",
        )
        NumberGroup.__init__(
            self,
            placeholder=placeholder,
            required=required,
            readonly=readonly,
            unique=unique,
        )
        if DEBUG:
            if input_type not in ["number", "range"]:
                raise AssertionError(
                    "Parameter `input_type` - Invalid input type! "
                    + "The permissible value of `number` or `range`."
                )
            if max_number is not None and not isinstance(max_number, int):
                raise AssertionError(
                    "Parameter `max_number` - Not а number `int` type!"
                )
            if min_number is not None and not isinstance(min_number, int):
                raise AssertionError(
                    "Parameter `min_number` - Not а number `int` type!"
                )
            if not isinstance(step, int):
                raise AssertionError("Parameter `step` - Not а number `int` type!")
            if (
                max_number is not None
                and min_number is not None
                and max_number <= min_number
            ):
                raise AssertionError(
                    "The `max_number` parameter should be more than the `min_number`!"
                )
            if default is not None:
                if not isinstance(default, int):
                    raise AssertionError(
                        "Parameter `default` - Not а number `int` type!"
                    )
                if max_number is not None and default > max_number:
                    raise AssertionError("Parameter `default` is more `max_number`!")
                if max_number is not None and default < min_number:  # type: ignore
                    raise AssertionError("Parameter `default` is less `min_number`!")

        self.__input_type: str = input_type
        self.__value: int | None = None
        self.__default = default
        self.__max_number = max_number
        self.__min_number = min_number
        self.__step = step

    @property
    def input_type(self) -> str:
        """Input type for a web form field.
        Html tag: input type="number|range".
        """
        return self.__input_type

    # --------------------------------------------------------------------------
    @property
    def value(self) -> int | None:
        """Sets value of field."""
        return self.__value

    @value.setter
    def value(self, value: int | None) -> None:
        self.__value = value

    # --------------------------------------------------------------------------
    @property
    def default(self) -> int | None:
        """Value by default."""
        return self.__default

    # --------------------------------------------------------------------------
    @property
    def max_number(self) -> int | None:
        """Maximum allowed number."""
        return self.__max_number

    # --------------------------------------------------------------------------
    @property
    def min_number(self) -> int | None:
        """Minimum allowed number."""
        return self.__min_number

    # --------------------------------------------------------------------------
    @property
    def step(self) -> int:
        """Increment step for numeric fields."""
        return self.__step

    # --------------------------------------------------------------------------
    def to_dict(self) -> dict[str, str | int | bool | list[str] | None]:
        """Convert fields to a dictionary."""
        json_dict: dict[str, str | int | bool | list[str] | None] = {}
        for f_name, f_type in self.__dict__.items():
            f_name = f_name.rsplit("__", maxsplit=1)[-1]
            if not callable(f_type):
                json_dict[f_name] = f_type
        return json_dict

    def to_json(self):
        """Convert a dictionary of fields to a JSON string."""
        return json.dumps(self.to_dict())
