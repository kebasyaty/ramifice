"""Group for checking slug fields.

Supported fields:
    SlugField
"""

from __future__ import annotations

__all__ = ("SlugGroupMixin",)

import logging
from typing import Any

from slugify import slugify

from ramifice.paladins.tools import check_uniqueness
from ramifice.utils.errors import PanicError

logger = logging.getLogger(__name__)


class SlugGroupMixin:
    """Group for checking slug fields.

    Supported fields:
        SlugField
    """

    async def slug_group(self, params: dict[str, Any]) -> None:
        """Checking slug fields."""
        if not params["is_save"]:
            return
        #
        field = params["field_data"]
        field_name = field.name
        raw_str_list: list[str] = []
        slug_sources = field.slug_sources
        #
        for _field_name, field_data in self.__dict__.items():
            if callable(field_data):
                continue
            if _field_name in slug_sources:
                value = field_data.value
                if value is None:
                    value = field_data.__dict__.get("default")
                if value is not None:
                    raw_str_list.append(value if _field_name != "_id" else str(value))
                else:
                    err_msg = (
                        f"Model: `{params['full_model_name']}` > "
                        + f"Field: `{field_name}` => "
                        + f"{_field_name} - "
                        + "This field is specified in slug_sources. "
                        + "This field should be mandatory or assign a default value."
                    )
                    logger.critical(err_msg)
                    raise PanicError(err_msg)
        # Insert result.
        if params["is_save"]:
            # Convert to slug.
            value = slugify("-".join(raw_str_list))
            # Validation of uniqueness of the value.
            if not await check_uniqueness(
                value,
                params,
                field_name,
            ):
                err_msg = (
                    f"Model: `{params['full_model_name']}` > "
                    + f"Field: `{field_name}` > "
                    + "Parameter: `slug_sources` => "
                    + "At least one field should be unique!"
                )
                logger.critical(err_msg)
                raise PanicError(err_msg)
            # Add value to map.
            params["result_map"][field_name] = value
