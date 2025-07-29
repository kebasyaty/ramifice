"""Accounts."""

from ramifice import model, translations
from ramifice.fields import FileField, ImageField


@model(service_name="Accounts")
class User:
    """Model of User."""

    def fields(self) -> None:
        """Adding fields."""
        # For custom translations.
        gettext = translations.gettext

        self.avatar = ImageField(
            label=gettext("Avatar"),
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
        self.resume = FileField(
            label=gettext("Resume"),
            default="public/media/default/no_doc.odt",
        )
