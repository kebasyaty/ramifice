"""Goods."""

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
        """For adding fields."""
        # For custom translations.
        gettext = translations.gettext
        ngettext = translations.ngettext
        self.size_float = ChoiceFloatField(
            label=gettext("Size in float"),
            choices={
                gettext("Big"): 25.8,
                gettext("Middle"): 15.6,
                gettext("Small"): 12.5,
            },
        )
        self.sizes_float = ChoiceFloatMultField(
            label=gettext("Sizes in float"),
            choices={
                gettext("Big"): 25.8,
                gettext("Middle"): 15.6,
                gettext("Small"): 12.5,            },
        )
        self.size_int = ChoiceIntField(
            label=gettext("Size in Int"),
            choices={
                gettext("Big"): 25,
                gettext("Middle"): 15,
                gettext("Small"): 12,            },
        )
        self.sizes_int = ChoiceIntMultField(
            label=gettext("Sizes in Int"),
            choices={
                gettext("Big"): 25,
                gettext("Middle"): 15,
                gettext("Small"): 12,            },
        )
        self.size_txt = ChoiceTextField(
            label=gettext("Size in Text"),
            choices={
                gettext("Big"): "big",
                gettext("Middle"): "middle",
                gettext("Small"): "small",
            },
        )
        self.sizes_txt = ChoiceTextMultField(
            label=gettext("Sizes in Text"),
            choices={
                gettext("Big"): "big",
                gettext("Middle"): "middle",
                gettext("Small"): "small",            },
        )
