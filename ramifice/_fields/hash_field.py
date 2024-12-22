"""Field of Model for enter identifier of document."""

from bson.objectid import ObjectId

from .general.field import Field
from .general.text_group import TextGroup


class HashField(Field, TextGroup):
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

    def object_id(self) -> ObjectId | None:
        """Get ObjectId from parameter `value`."""
        _hash = self.value
        _id = ObjectId(_hash) if _hash is not None else None
        return _id
