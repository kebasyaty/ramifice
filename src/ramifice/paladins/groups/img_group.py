"""Group for checking image fields.

Supported fields: ImageField
"""

from __future__ import annotations

__all__ = ("ImgGroupMixin",)

from asyncio import to_thread
from typing import Any

from PIL import Image
from xloft.converters import to_human_size

from ramifice.paladins.tools import accumulate_error, panic_type_error
from ramifice.utils import translations


class ImgGroupMixin:
    """Group for checking image fields.

    Supported fields: ImageField
    """

    async def img_group(self, params: dict[str, Any]) -> None:
        """Checking image fields."""
        field = params["field_data"]
        value = field.value or None

        if not isinstance(value, (dict, type(None))):
            panic_type_error("dict | None", params)

        if not params["is_update"] and value is None:
            default = field.default or None
            # If necessary, use the default value.
            if default is not None:
                params["field_data"].from_path(default)
                value = params["field_data"].value
            # Validation, if the field is required and empty, accumulate the error.
            # ( the default value is used whenever possible )
            if value is None:
                if field.required:
                    err_msg = translations._("Required field !")
                    accumulate_error(err_msg, params)
                if params["is_save"]:
                    params["result_map"][field.name] = None
                return
        # Return if the current value is missing
        if value is None:
            return
        if not value["save_as_is"]:
            # If the file needs to be delete.
            if value["is_delete"] and len(value["path"]) == 0:
                default = field.default or None
                # If necessary, use the default value.
                if default is not None:
                    params["field_data"].from_path(default)
                    value = params["field_data"].value
                else:
                    if not field.required:
                        if params["is_save"]:
                            params["result_map"][field.name] = None
                    else:
                        err_msg = translations._("Required field !")
                        accumulate_error(err_msg, params)
                    return
            # Accumulate an error if the file size exceeds the maximum value.
            if value["size"] > field.max_size:
                human_size = to_human_size(field.max_size)
                err_msg = translations._(
                    "Image size exceeds the maximum value {} !",
                ).format(human_size)
                accumulate_error(err_msg, params)
                return
            # Create thumbnails.
            if value["is_new_img"]:
                thumbnails = field.thumbnails
                if thumbnails is not None:
                    path = value["path"]
                    imgs_dir_path = value["imgs_dir_path"]
                    imgs_dir_url = value["imgs_dir_url"]
                    extension = value["extension"]
                    # Extension to the upper register and delete the point.
                    ext_upper = value["ext_upper"]
                    # Get image file.
                    with await to_thread(Image.open, path) as img:
                        width, height = img.size
                        value["width"] = width
                        value["height"] = height
                        for size_name in ["lg", "md", "sm", "xs"]:
                            max_size = thumbnails.get(size_name)
                            if max_size is None:
                                continue
                            size = max_size, max_size
                            img.thumbnail(size=size, resample=Image.Resampling.LANCZOS)
                            match size_name:
                                case "lg":
                                    value["path_lg"] = f"{imgs_dir_path}/lg{extension}"
                                    value["url_lg"] = f"{imgs_dir_url}/lg{extension}"
                                    await to_thread(
                                        img.save,
                                        fp=value["path_lg"],
                                        format=ext_upper,
                                    )
                                case "md":
                                    value["path_md"] = f"{imgs_dir_path}/md{extension}"
                                    value["url_md"] = f"{imgs_dir_url}/md{extension}"
                                    await to_thread(
                                        img.save,
                                        fp=value["path_md"],
                                        format=ext_upper,
                                    )
                                case "sm":
                                    value["path_sm"] = f"{imgs_dir_path}/sm{extension}"
                                    value["url_sm"] = f"{imgs_dir_url}/sm{extension}"
                                    await to_thread(
                                        img.save,
                                        fp=value["path_sm"],
                                        format=ext_upper,
                                    )
                                case "xs":
                                    value["path_xs"] = f"{imgs_dir_path}/xs{extension}"
                                    value["url_xs"] = f"{imgs_dir_url}/xs{extension}"
                                    await to_thread(
                                        img.save,
                                        fp=value["path_xs"],
                                        format=ext_upper,
                                    )
        # Insert result.
        if params["is_save"] and (value["is_new_img"] or value["save_as_is"]):
            value["is_delete"] = False
            value["save_as_is"] = True
            params["result_map"][field.name] = value
