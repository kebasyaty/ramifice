"""Field of Model.
Type of selective float field with dynamic addition of elements.
"""

from .. import translations
from ..mixins import JsonMixin
from .general.choice_group import ChoiceGroup
from .general.field import Field


class ChoiceFloatMultDynField(Field, ChoiceGroup, JsonMixin):
    """Field of Model.
    Type of selective float field with dynamic addition of elements.
    For simulate relationship Many-to-Many.
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

        if len(label) > 0:
            label = translations.gettext(label)
        if len(hint) > 0:
            hint = translations.gettext(hint)
        if bool(warning):
            warning = [translations.gettext(item) for item in warning]

        Field.__init__(
            self,
            label=label,
            disabled=disabled,
            hide=hide,
            ignored=ignored,
            hint=hint,
            warning=warning,
            field_type="ChoiceFloatMultDynField",
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
        self.choices: dict[str, float] | None = None

    def has_value(self) -> bool:
        """Does the field value match the possible options in choices."""
        value = self.value
        if value is not None:
            choices = self.choices
            if len(value) == 0 or not bool(choices):
                return False
            value_list = choices.values()  # type: ignore[union-attr]
            for item in value:
                if item not in value_list:
                    return False
        return True
