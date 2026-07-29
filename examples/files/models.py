"""Models."""

from ramifice import (
    Model,
    Translator,
    fields,
    meta,
    to_human_size,
)

_ = Translator.STUB_TRANSLATOR_FOR_ATTRIBUTES_OF_FIELD


@meta(service_name="Accounts")
class User(Model):
    """User Model."""

    avatar = fields.ImageField(
        label=_("Avatar"),
        default="public/media/default/no-photo.png",
        # Available 4 sizes from lg to xs or None.
        # Hint: By default = None
        thumbnails={"lg": 512, "md": 256, "sm": 128, "xs": 64},
        # The maximum size of the original image in bytes.
        # Hint: By default = 2 MB
        max_size=524288,  # 0.5 MB = 524288 Bytes (in binary)
        warning=[
            _("Maximum size: {}").format(to_human_size(524288)),
        ],
    )
    resume = fields.FileField(
        label=_("Resume"),
        default="public/media/default/no_doc.odt",
    )
