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
                "Big": 25.8,
                "Middle": 15.6,
                "Small": 12.5,
            },
        )
        self.sizes_float = ChoiceFloatMultField(
            label=gettext("Sizes in float"),
            choices={
                "Big": 25.8,
                "Middle": 15.6,
                "Small": 12.5,
            },
        )
        self.size_int = ChoiceIntField(
            label=gettext("Size in Int"),
            choices={
                "Big": 25,
                "Middle": 15,
                "Small": 12,
            },
        )
        self.sizes_int = ChoiceIntMultField(
            label=gettext("Sizes in Int"),
            choices={
                "Big": 25,
                "Middle": 15,
                "Small": 12,
            },
        )
        self.size_txt = ChoiceTextField(
            label=gettext("Size in Text"),
            choices={
                "Big": "big",
                "Middle": "middle",
                "Small": "small",
            },
        )
        self.sizes_txt = ChoiceTextMultField(
            label=gettext("Sizes in Text"),
            choices={
                "Big": "big",
                "Middle": "middle",
                "Small": "small",
            },
        )
