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

    size_float = fields.ChoiceFloatField(
        label=_("Size in float"),
        choices=[
            [25.8, _("Big")],
            [15.6, _("Middle")],
            [12.5, _("Small")],
        ],
    )
    sizes_float = fields.ChoiceFloatMultField(
        label=_("Sizes in float"),
        choices=[
            [25.8, _("Big")],
            [15.6, _("Middle")],
            [12.5, _("Small")],
        ],
    )
    size_int = fields.ChoiceIntField(
        label=_("Size in Int"),
        choices=[
            [25, _("Big")],
            [15, _("Middle")],
            [12, _("Small")],
        ],
    )
    sizes_int = fields.ChoiceIntMultField(
        label=_("Sizes in Int"),
        choices=[
            [25, _("Big")],
            [15, _("Middle")],
            [12, _("Small")],
        ],
    )
    size_txt = fields.ChoiceTextField(
        label=_("Size in Text"),
        choices=[
            ["big", _("Big")],
            ["middle", _("Middle")],
            ["small", _("Small")],
        ],
    )
    sizes_txt = fields.ChoiceTextMultField(
        label=_("Sizes in Text"),
        choices=[
            ["big", _("Big")],
            ["middle", _("Middle")],
            ["small", _("Small")],
        ],
    )
