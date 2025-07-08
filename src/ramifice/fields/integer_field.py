"""Field of Model for enter (int) number."""

from ramifice.fields.general.field import Field
from ramifice.fields.general.number_group import NumberGroup
from ramifice.utils import constants
from ramifice.utils.mixins.json_converter import JsonMixin


class IntegerField(Field, NumberGroup, JsonMixin):
    """Field of Model for enter (int) number."""

    def __init__(  # noqa: D107
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
        if constants.DEBUG:
            if input_type not in ["number", "range"]:
                raise AssertionError(
                    "Parameter `input_type` - Invalid input type! "
                    + "The permissible value of `number` or `range`."
                )
            if max_number is not None and not isinstance(max_number, int):
                raise AssertionError("Parameter `max_number` - Not а number `int` type!")
            if min_number is not None and not isinstance(min_number, int):
                raise AssertionError("Parameter `min_number` - Not а number `int` type!")
            if not isinstance(step, int):
                raise AssertionError("Parameter `step` - Not а number `int` type!")
            if max_number is not None and min_number is not None and max_number <= min_number:
                raise AssertionError(
                    "The `max_number` parameter should be more than the `min_number`!"
                )
            if default is not None:
                if not isinstance(default, int):
                    raise AssertionError("Parameter `default` - Not а number `int` type!")
                if max_number is not None and default > max_number:
                    raise AssertionError("Parameter `default` is more `max_number`!")
                if max_number is not None and default < min_number:  # type: ignore
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

        Field.__init__(
            self,
            label=label,
            disabled=disabled,
            hide=hide,
            ignored=ignored,
            hint=hint,
            warning=warning,
            field_type="IntegerField",
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
        self.value: int | None = None
        self.default = default
        self.max_number = max_number
        self.min_number = min_number
        self.step = step
