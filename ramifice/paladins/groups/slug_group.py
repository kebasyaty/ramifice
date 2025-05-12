"""Group for checking slug fields.
Supported fields: SlugField
"""

from typing import Any

from slugify import slugify

from ...errors import PanicError


class SlugGroupMixin:
    """Group for checking slug fields.
    Supported fields: SlugField
    """

    def slug_group(self, params: dict[str, Any]) -> None:
        """Checking slug fields."""
        if not params["is_save"]:
            return
        #
        field = params["field_data"]
        raw_str_list: list[str] = []
        slug_sources = field.slug_sources
        #
        for field_name, field_data in self.__dict__.items():
            if callable(field_data):
                continue
            if field_name in slug_sources:
                value = field_data.value
                if value is None:
                    value = field_data.__dict__.get("default")
                if value is not None:
                    raw_str_list.append(value if field_name != "_id" else str(value))
                else:
                    err_msg = (
                        f"Model: `{self.full_model_name()}` > "  # type: ignore[attr-defined]
                        + f"Field: `{field.name}` => "
                        + f"{field_name} - "
                        + "This field is specified in slug_sources. "
                        + "This field should be mandatory or assign a default value."
                    )
                    raise PanicError(err_msg)
        # Insert result.
        if params["is_save"]:
            value = "-".join(raw_str_list)
            params["result_map"][field.name] = slugify(value)
