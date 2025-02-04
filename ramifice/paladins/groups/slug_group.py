"""Group for checking slug fields.
Supported fields: SlugField
"""

from typing import Any

from slugify import slugify


class SlugGroupMixin:
    """Group for checking slug fields.
    Supported fields: SlugField
    """

    def slug_group(self, params: dict[str, Any]) -> None:
        """Checking slug fields."""
        field = params["field_data"]
        raw_str_list: list[str] = []
        slug_sources = field.slug_sources
