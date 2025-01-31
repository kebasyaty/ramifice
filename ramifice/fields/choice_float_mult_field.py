"""Field of Model.
Type of selective float field with static of elements.
"""

from ..mixins import JsonMixin
from ..store import DEBUG
from .general.choice_group import ChoiceGroup
from .general.field import Field


class ChoiceFloatMultField(Field, ChoiceGroup, JsonMixin):
    """Field of Model.
    Type of selective float field with static of elements.
    With multiple choice.
    How to use, see <a href="https://github.com/kebasyaty/ramifice/tree/main/examples/static_choices" target="_blank">example</a>.
    """

    def __init__(
        self,
        label: str = "",
        disabled: bool = False,
        hide: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        default: list[float] | None = None,
        required: bool = False,
        readonly: bool = False,
        choices: dict[str, float] | None = None,
    ):
        Field.__init__(
            self,
            label=label,
            disabled=disabled,
            hide=hide,
            ignored=ignored,
            hint=hint,
            warning=warning,
            field_type="ChoiceFloatMultField",
            group="choice",
        )
        ChoiceGroup.__init__(
            self,
            required=required,
            readonly=readonly,
            multiple=True,
        )
        JsonMixin.__init__(self)

        self.value: list[float] | None = None
        self.default = default
        self.choices = choices

        if DEBUG:
            if choices is not None:
                if not isinstance(choices, list):
                    raise AssertionError("Parameter `choices` - Not а `list` type!")
                if len(choices) == 0:
                    raise AssertionError(
                        "The `choices` parameter should not contain an empty list!"
                    )
            if default is not None:
                if not isinstance(default, list):
                    raise AssertionError("Parameter `default` - Not а `list` type!")
                if len(default) == 0:
                    raise AssertionError(
                        "The `default` parameter should not contain an empty list!"
                    )
                if choices is not None and not self.has_value():
                    raise AssertionError(
                        "Parameter `default` does not coincide with "
                        + "list of permissive values in `choicees`."
                    )

    def has_value(self) -> bool:
        """Does the field value match the possible options in choices."""
        flag = True
        value = self.value or self.default or None
        choices = self.choices or None
        if value is not None and choices is not None:
            value_list = [item[0] for item in choices]
            for item in value:
                if item not in value_list:
                    flag = False
                    break
        return flag
