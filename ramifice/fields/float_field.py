"""Field of Model for enter (float) number."""

from ..mixins import JsonMixin
from ..store import DEBUG
from .general.field import Field
from .general.number_group import NumberGroup


class FloatField(Field, NumberGroup, JsonMixin):
    """Field of Model for enter (float) number."""

    # pylint: disable=too-many-locals
    # pylint: disable=too-many-arguments
    def __init__(
        self,
        label: str = "",
        disabled: bool = False,
        hide: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        default: float | None = None,
        placeholder: str = "",
        required: bool = False,
        readonly: bool = False,
        unique: bool = False,
        max_number: int | None = None,
        min_number: int | None = None,
        step: float = 1.0,
        input_type: str = "number",  # number | range
    ):
        if DEBUG:
            if input_type not in ["number", "range"]:
                raise AssertionError(
                    "Parameter `input_type` - Invalid input type! "
                    + "The permissible value of `number` or `range`."
                )
            if max_number is not None and not isinstance(max_number, float):
                raise AssertionError(
                    "Parameter `max_number` - Not а number `float` type!"
                )
            if min_number is not None and not isinstance(min_number, float):
                raise AssertionError(
                    "Parameter `min_number` - Not а number `float` type!"
                )
            if not isinstance(step, float):
                raise AssertionError("Parameter `step` - Not а number `float` type!")
            if (
                max_number is not None
                and min_number is not None
                and max_number <= min_number
            ):
                raise AssertionError(
                    "The `max_number` parameter should be more than the `min_number`!"
                )
            if default is not None:
                if not isinstance(default, float):
                    raise AssertionError(
                        "Parameter `default` - Not а number `float` type!"
                    )
                if max_number is not None and default > max_number:
                    raise AssertionError("Parameter `default` is more `max_number`!")
                if max_number is not None and default < min_number:  # type: ignore
                    raise AssertionError("Parameter `default` is less `min_number`!")

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
