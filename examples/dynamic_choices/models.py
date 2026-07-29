"""Models."""

from ramifice import (
    Model,
    Translator,
    fields,
    meta,
)

_ = Translator.STUB_TRANSLATOR_FOR_ATTRIBUTES_OF_FIELD


@meta(service_name="Goods")
class Product(Model):
    """Product Model."""

    size_float = fields.ChoiceFloatDynField(
        label=_("Size in float"),
    )
    sizes_float = fields.ChoiceFloatMultDynField(
        label=_("Sizes in float"),
    )
    size_int = fields.ChoiceIntDynField(
        label=_("Size in Int"),
    )
    sizes_int = fields.ChoiceIntMultDynField(
        label=_("Sizes in Int"),
    )
    size_txt = fields.ChoiceTextDynField(
        label=_("Size in Text"),
    )
    sizes_txt = fields.ChoiceTextMultDynField(
        label=_("Sizes in Text"),
    )
