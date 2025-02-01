"""Field of Model for enter identifier of document."""

from bson.objectid import ObjectId

from ..mixins import JsonMixin
from .general.field import Field
from .general.text_group import TextGroup


class HashField(Field, TextGroup, JsonMixin):
    """Field of Model for enter identifier of document."""

    def __init__(
        self,
        label: str = "",
        disabled: bool = False,
        hide: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        placeholder: str = "",
        required: bool = False,
        readonly: bool = False,
        unique: bool = False,
    ):
        Field.__init__(
            self,
            label=label,
            disabled=disabled,
            hide=hide,
            ignored=ignored,
            hint=hint,
            warning=warning,
            field_type="HashField",
            group="hash",
        )
        TextGroup.__init__(
            self,
            input_type="text",
            placeholder=placeholder,
            required=required,
            readonly=readonly,
            unique=unique,
        )
        JsonMixin.__init__(self)

        self.alerts: list[str] | None = None

    def __str__(self):
        return str(self.value)

    def to_obj_id(self) -> ObjectId | None:
        """Get ObjectId from parameter `value`."""
        value = self.value
        return ObjectId(value) if bool(value) else None
