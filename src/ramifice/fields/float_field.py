"""Field of Model for enter (float) number."""

from __future__ import annotations

__all__ = ("FloatField",)

import logging
from typing import Literal

from ramifice.fields.general.field import Field
from ramifice.fields.general.number_group import NumberGroup
from ramifice.utils import constants
from ramifice.utils.mixins import JsonMixin

logger = logging.getLogger(__name__)


class FloatField(Field, NumberGroup, JsonMixin):
    """Field of Model for enter (float) number.

    Agrs:
        label: Text label for a web form field.
        placeholder: Displays prompt text.
        default: Value by default.
        hide: Hide field from user.
        disabled: Blocks access and modification of the element.
        ignored: If true, the value of this field is not saved in the database.
        hint: An alternative for the `placeholder` parameter.
        warning: Warning information.
        required: Required field.
        readonly: Specifies that the field cannot be modified by the user.
        unique: The unique value of a field in a collection.
        max_number: Maximum allowed number.
        min_number: Minimum allowed number.
        step: Increment step for numeric fields.
        input_type: Field type - `number` or `range`.
    """

    def __init__(  # noqa: D107
        self,
        label: str = "",
        placeholder: str = "",
        default: float | None = None,
        hide: bool = False,
        disabled: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        required: bool = False,
        readonly: bool = False,
        unique: bool = False,
        max_number: float | None = None,
        min_number: float | None = None,
        step: float = 1.0,
        input_type: Literal["number", "range"] = "number",
    ) -> None:
        if constants.DEBUG:
            try:
                if input_type not in ["number", "range"]:
                    raise AssertionError(
                        "Parameter `input_type` - Invalid input type! "
                        + "The permissible value of `number` or `range`.",
                    )
                if max_number is not None and not isinstance(max_number, float):
                    raise AssertionError("Parameter `max_number` - Not а number `float` type!")
                if min_number is not None and not isinstance(min_number, float):
                    raise AssertionError("Parameter `min_number` - Not а number `float` type!")
                if not isinstance(step, float):
                    raise AssertionError("Parameter `step` - Not а number `float` type!")
                if max_number is not None and min_number is not None and max_number <= min_number:
                    raise AssertionError("The `max_number` parameter should be more than the `min_number`!")
                if default is not None:
                    if not isinstance(default, float):
                        raise AssertionError("Parameter `default` - Not а number `float` type!")
                    if max_number is not None and default > max_number:
                        raise AssertionError("Parameter `default` is more `max_number`!")
                    if max_number is not None and default < min_number:
                        raise AssertionError("Parameter `default` is less `min_number`!")
                if not isinstance(label, str):
                    raise AssertionError("Parameter `default` - Not а `str` type!")
                if not isinstance(disabled, bool):
                    raise AssertionError("Parameter `disabled` - Not а `bool` type!")
                if not isinstance(hide, bool):
                    raise AssertionError("Parameter `hide` - Not а `bool` type!")
                if not isinstance(ignored, bool):
                    raise AssertionError("Parameter `ignored` - Not а `bool` type!")
                if not isinstance(ignored, bool):
                    raise AssertionError("Parameter `ignored` - Not а `bool` type!")
                if not isinstance(hint, str):
                    raise AssertionError("Parameter `hint` - Not а `str` type!")
                if warning is not None and not isinstance(warning, list):
                    raise AssertionError("Parameter `warning` - Not а `list` type!")
                if not isinstance(placeholder, str):
                    raise AssertionError("Parameter `placeholder` - Not а `str` type!")
                if not isinstance(required, bool):
                    raise AssertionError("Parameter `required` - Not а `bool` type!")
                if not isinstance(readonly, bool):
                    raise AssertionError("Parameter `readonly` - Not а `bool` type!")
                if not isinstance(unique, bool):
                    raise AssertionError("Parameter `unique` - Not а `bool` type!")
            except AssertionError as err:
                logger.critical(str(err))
                raise err

        Field.__init__(
            self,
            label=label,
            disabled=disabled,
            hide=hide,
            ignored=ignored,
            hint=hint,
            warning=warning,
            field_type="FloatField",
            group="num",
        )
        NumberGroup.__init__(
            self,
            placeholder=placeholder,
            required=required,
            readonly=readonly,
            unique=unique,
        )
        JsonMixin.__init__(self)

        self.input_type: str = input_type
        self.value: float | None = None
        self.default = default
        self.max_number = max_number
        self.min_number = min_number
        self.step = step
