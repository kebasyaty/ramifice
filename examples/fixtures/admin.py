"""Site."""

from ramifice import model, translations
from ramifice.fields import (
    BooleanField,
    DateField,
    EmailField,
    FileField,
    ImageField,
    TextField,
)


@model(
    service_name="Admin",
    fixture_name="SiteParameters",  # config/fixtures/SiteParameters.yml
    is_create_doc=False,  # Site parameters should be in a single document.
    is_delete_doc=False,
)
class SiteParameters:
    """Model of Site Parameters."""

    def fields(self) -> None:
        """For adding fields."""
        # For custom translations.
        gettext = translations.gettext
        ngettext = translations.ngettext
        self.logo = ImageField(
            label=gettext("Logo"),
            default="public/media/default/no-photo.png",
            # Available 4 sizes from lg to xs or None.
            # Hint: By default = None
            thumbnails={"lg": 512, "md": 256, "sm": 128, "xs": 64},
            # True - high quality and low performance for thumbnails.
            # Hint: By default = False
            high_quality=True,
            # The maximum size of the original image in bytes.
            # Hint: By default = 2 MB
            max_size=524288,  # 0.5 MB = 524288 Bytes (in binary)
        )
        self.copyright = FileField(
            label=gettext("File of copyright"),
            default="public/media/default/no_doc.odt",
        )
        self.brand = TextField(
            label=gettext("Brand Name"),
            required=True,
        )
        self.slogan = TextField(
            label=gettext("Slogan"),
            required=True,
        )
        self.about_site = TextField(
            label=gettext("About the site"),
        )
        self.email_feedback = EmailField(
            label=gettext("Email feedback"),
            required=True,
        )
        self.start_date = DateField(
            label=gettext("Brand foundation date"),
        )
        self.is_active = BooleanField(
            label=gettext("Site is active?"),
            default=True,
        )
