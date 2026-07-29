"""Models."""

from ramifice import (
    Model,
    Translator,
    fields,
    meta,
    to_human_size,
)

_ = Translator.STUB_TRANSLATOR_FOR_ATTRIBUTES_OF_FIELD


@meta(
    service_name="Admin",
    fixture_name="SiteParameters",  # config/fixtures/SiteParameters.yml
    is_create_doc=False,  # Site parameters should be in a single document.
    is_delete_doc=False,
)
class SiteParameters(Model):
    """Site Parameters Model."""

    logo = fields.ImageField(
        label=_("Logo"),
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
    copyright = fields.FileField(
        label=_("File of copyright"),
        default="public/media/default/no_doc.odt",
    )
    brand = fields.TextField(
        label=_("Brand Name"),
        is_require=True,
    )
    slogan = fields.TextField(
        label=_("Slogan"),
        is_require=True,
    )
    about_site = fields.TextField(
        label=_("About the site"),
    )
    email_feedback = fields.EmailField(
        label=_("Email feedback"),
        is_require=True,
    )
    start_date = fields.DateField(
        label=_("Brand foundation date"),
    )
    is_active = fields.BooleanField(
        label=_("Site is active?"),
        default=True,
    )
