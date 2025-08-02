"""Models."""

from ramifice import model, translations
from ramifice.fields import (
    ChoiceFloatField,
    ChoiceFloatMultField,
    ChoiceIntField,
    ChoiceIntMultField,
    ChoiceTextField,
    ChoiceTextMultField,
)


@model(service_name="Goods")
class Product:
    """Model of Product."""

    def fields(self) -> None:
        """Adding fields."""
        # For custom translations.
        gettext = translations.gettext
        ngettext = translations.ngettext
        self.size_float = ChoiceFloatField(
            label=gettext("Size in float"),
            choices=[
                [25.8, gettext("Big")],
                [15.6, gettext("Middle")],
                [12.5, gettext("Small")],
            ],
        )
        self.sizes_float = ChoiceFloatMultField(
            label=gettext("Sizes in float"),
            choices=[
                [25.8, gettext("Big")],
                [15.6, gettext("Middle")],
                [12.5, gettext("Small")],
            ],
        )
        self.size_int = ChoiceIntField(
            label=gettext("Size in Int"),
            choices=[
                [25, gettext("Big")],
                [15, gettext("Middle")],
                [12, gettext("Small")],
            ],
        )
        self.sizes_int = ChoiceIntMultField(
            label=gettext("Sizes in Int"),
            choices=[
                [25, gettext("Big")],
                [15, gettext("Middle")],
                [12, gettext("Small")],
            ],
        )
        self.size_txt = ChoiceTextField(
            label=gettext("Size in Text"),
            choices=[
                ["big", gettext("Big")],
                ["middle", gettext("Middle")],
                ["small", gettext("Small")],
            ],
        )
        self.sizes_txt = ChoiceTextMultField(
            label=gettext("Sizes in Text"),
            choices=[
                ["big", gettext("Big")],
                ["middle", gettext("Middle")],
                ["small", gettext("Small")],
            ],
        )
