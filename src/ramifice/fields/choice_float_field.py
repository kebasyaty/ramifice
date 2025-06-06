"""Field of Model.
Type of selective float field with static of elements.
"""

from ..mixins import JsonMixin
from ..store import DEBUG
from .general.choice_group import ChoiceGroup
from .general.field import Field


class ChoiceFloatField(Field, ChoiceGroup, JsonMixin):
    """Field of Model.
    Type of selective integer float with static of elements.
    With a single choice.
    How to use, see <a href="https://github.com/kebasyaty/ramifice/tree/main/examples/static_choices" target="_blank">example</a>.
    """

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
            field_type="ChoiceFloatField",
            group="choice",
        )
        ChoiceGroup.__init__(
            self,
            required=required,
            readonly=readonly,
        )
        JsonMixin.__init__(self)

        self.value: float | None = None
        self.default = default
        self.choices = choices

        if DEBUG:
            if choices is not None and not isinstance(choices, dict):
                raise AssertionError("Parameter `choices` - Not а `dict` type!")
            if default is not None and not isinstance(default, float):
                raise AssertionError("Parameter `default` - Not а `float` type!")
            if default is not None and choices is not None and not self.has_value():
                raise AssertionError(
                    "Parameter `default` does not coincide with "
                    + "list of permissive values in `choicees`."
                )

    def has_value(self) -> bool:
        """Does the field value match the possible options in choices."""
        value = self.value
        if value is None:
            value = self.default
        if value is not None:
            choices = self.choices
            if not bool(choices):
                return False
            if value not in choices.values():  # type: ignore[union-attr]
                return False
        return True
