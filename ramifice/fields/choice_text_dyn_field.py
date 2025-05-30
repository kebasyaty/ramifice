"""Field of Model.
Type of selective text field with dynamic addition of elements.
"""

from .. import translations
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

    def has_value(self) -> bool:
        """Does the field value match the possible options in choices."""
        value = self.value
        if value is not None:
            choices = self.choices
            if not bool(choices):
                return False
            if value not in choices.values():  # type: ignore[union-attr]
                return False
        return True
