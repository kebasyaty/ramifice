"""Field of Model.
Type of selective integer field with static of elements.
"""

from ..mixins import JsonMixin
from ..store import DEBUG
from .general.choice_group import ChoiceGroup
from .general.field import Field


class ChoiceIntField(Field, ChoiceGroup, JsonMixin):
    """Field of Model.
    Type of selective integer field with static of elements.
    With a single choice.
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
        default: int | None = None,
        required: bool = False,
        readonly: bool = False,
        choices: dict[str, int] | None = None,
    ):
        Field.__init__(
            self,
            label=label,
            disabled=disabled,
            hide=hide,
            ignored=ignored,
            hint=hint,
            warning=warning,
            field_type="ChoiceIntField",
            group="choice",
        )
        ChoiceGroup.__init__(
            self,
            required=required,
            readonly=readonly,
        )
        JsonMixin.__init__(self)

        self.value: int | None = None
        self.default = default
        self.choices = choices

        if DEBUG:
            if choices is not None and not isinstance(choices, list):
                raise AssertionError("Parameter `choices` - Not а `list` type!")
            if default is not None and not isinstance(default, int):
                raise AssertionError("Parameter `default` - Not а `str` type!")
            if default is not None and choices is not None and not self.has_value():
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
            value_list = choices.values()
            if value not in value_list:
                flag = False
        return flag
