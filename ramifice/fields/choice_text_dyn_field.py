"""Field of Model.
Type of selective text field with dynamic addition of elements.
"""

from ..mixins import JsonMixin
from .general.choice_group import ChoiceGroup
from .general.field import Field


class ChoiceTextDynField(Field, ChoiceGroup, JsonMixin):
    """Field of Model.
    Type of selective text field with dynamic addition of elements.
    For simulate relationship Many-to-One.
    Element are (add|delete) via `ModelName.unit_manager(unit)` method.
    How to use, see <a href="https://github.com/kebasyaty/ramifice/tree/main/examples/dynamic_choices" target="_blank">example</a>.
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
            field_type="ChoiceTextDynField",
            group="choice",
        )
        ChoiceGroup.__init__(
            self,
            required=required,
            readonly=readonly,
        )
        JsonMixin.__init__(self)

        self.value: str | None = None
        self.choices: dict[str, str] | None = None

    def __str__(self):
        return str(self.value)

    def has_value(self) -> bool:
        """Does the field value match the possible options in choices."""
        flag = True
        value = self.value or None
        choices = self.choices or None
        if value is not None and choices is not None:
            value_list = choices.values()
            # pylint: disable=not-an-iterable
            if value not in value_list:
                flag = False
        return flag
