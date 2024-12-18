"""Field of Model for enter identifier of document."""

from typing import Any
from bson.objectid import ObjectId
from .general.text_group import TextGroup
from .general.field import Field


class HashField(Field, TextGroup):
    """Field of Model for enter identifier of document."""

    def __init__(self,
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
                 maxlength: int = 24,
                 ):
        Field.__init__(self,
                       label=label,
                       disabled=disabled,
                       hide=hide,
                       ignored=ignored,
                       hint=hint,
                       warning=warning,
                       field_type='HashField',
                       group='hash',
                       )
        TextGroup.__init__(self,
                           input_type='text',
                           placeholder=placeholder,
                           required=required,
                           readonly=readonly,
                           unique=unique,
                           )
        self.__maxlength = maxlength

    @property
    def maxlength(self) -> int:
        """Maximum allowed number of characters."""
        return self.__maxlength

    def object_id(self) -> ObjectId | None:
        """Get ObjectId from value."""
        _hash = self.value
        _id = ObjectId(_hash) if _hash is not None else None
        return _id
