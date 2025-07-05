"""Goods."""

from ramifice import model, translations
from ramifice.fields import (
    ChoiceFloatDynField,
    ChoiceFloatMultDynField,
    ChoiceIntDynField,
    ChoiceIntMultDynField,
    ChoiceTextDynField,
    ChoiceTextMultDynField,
)


@model(service_name="Goods")
class Product:
    """Model of Product."""

    def fields(self) -> None:
        """For adding fields."""
        # For custom translations.
        gettext = translations.gettext
        ngettext = translations.ngettext
        self.size_float = ChoiceFloatDynField(
            label=gettext("Size in float"),
        )
        self.sizes_float = ChoiceFloatMultDynField(
            label=gettext("Sizes in float"),
        )
        self.size_int = ChoiceIntDynField(
            label=gettext("Size in Int"),
        )
        self.sizes_int = ChoiceIntMultDynField(
            label=gettext("Sizes in Int"),
        )
        self.size_txt = ChoiceTextDynField(
            label=gettext("Size in Text"),
        )
        self.sizes_txt = ChoiceTextMultDynField(
            label=gettext("Sizes in Text"),
        )
