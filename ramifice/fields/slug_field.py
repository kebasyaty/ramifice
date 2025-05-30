"""Field of Model for automatic generation of string `slug`."""

from ..mixins import JsonMixin
from .general.field import Field
from .general.text_group import TextGroup


class SlugField(Field, TextGroup, JsonMixin):
    """Field of Model for automatic generation of string `slug`.
    Convenient to use for Url addresses.
    """

    # pylint: disable=dangerous-default-value
    # pylint: disable=too-many-arguments
    def __init__(
        self,
        label: str = "",
        disabled: bool = False,
        hide: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        placeholder: str = "",
        readonly: bool = False,
        slug_sources: list[str] = ["_id"],
    ):

        Field.__init__(
            self,
            label=label,
            disabled=disabled,
            hide=hide,
            ignored=ignored,
            hint=hint,
            warning=warning,
            field_type="SlugField",
            group="slug",
        )
        TextGroup.__init__(
            self,
            input_type="text",
            placeholder=placeholder,
            required=False,
            readonly=readonly,
            unique=True,
        )
        JsonMixin.__init__(self)

        self.slug_sources = slug_sources
