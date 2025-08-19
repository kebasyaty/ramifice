"""Groups - Model instance methods for specific processing of fields."""

from __future__ import annotations

__all__ = (
    "BoolGroupMixin",
    "ChoiceGroupMixin",
    "DateGroupMixin",
    "FileGroupMixin",
    "IDGroupMixin",
    "ImgGroupMixin",
    "NumGroupMixin",
    "PassGroupMixin",
    "SlugGroupMixin",
    "TextGroupMixin",
)

from ramifice.paladins.groups.bool_group import BoolGroupMixin
from ramifice.paladins.groups.choice_group import ChoiceGroupMixin
from ramifice.paladins.groups.date_group import DateGroupMixin
from ramifice.paladins.groups.file_group import FileGroupMixin
from ramifice.paladins.groups.id_group import IDGroupMixin
from ramifice.paladins.groups.img_group import ImgGroupMixin
from ramifice.paladins.groups.num_group import NumGroupMixin
from ramifice.paladins.groups.pass_group import PassGroupMixin
from ramifice.paladins.groups.slug_group import SlugGroupMixin
from ramifice.paladins.groups.text_group import TextGroupMixin
