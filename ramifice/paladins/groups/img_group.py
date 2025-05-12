"""Group for checking image fields.
Supported fields: ImageField
"""

import shutil
from typing import Any

from PIL import Image

from ...tools import to_human_size


class ImgGroupMixin:
    """Group for checking image fields.
    Supported fields: ImageField
    """

    def img_group(self, params: dict[str, Any]) -> None:
        """Checking image fields."""
        field = params["field_data"]
        value = field.value or None
        #
        if not params["is_update"]:
            if value is None:
                default = field.default or None
                # If necessary, use the default value.
                if default is not None:
                    params["field_data"].from_path(default)
                    value = params["field_data"].value
                # Validation, if the field is required and empty, accumulate the error.
                # ( the default value is used whenever possible )
                if value is None:
                    if field.required:
                        err_msg = "Required field !"
                        self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
                    if params["is_save"]:
                        params["result_map"][field.name] = None
                    return
        # Return if the current value is missing
        if value is None:
            return
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
                    err_msg = "Required field !"
                    self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
                return
        # Accumulate an error if the file size exceeds the maximum value.
        if value["size"] > field.max_size:
            err_msg = f"Image size exceeds the maximum value {to_human_size(field.max_size)} !"
            self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
            return
        # Return if there is no need to save.
        if not params["is_save"]:
            if value["is_new_img"]:
                shutil.rmtree(value["imgs_dir_path"])
                params["field_data"].value = None
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
                with Image.open(path) as img:
                    for size_name in ["lg", "md", "sm", "xs"]:
                        max_size = thumbnails.get(size_name)
                        if max_size is None:
                            continue
                        size = max_size, max_size
                        img.thumbnail(size)
                        if size_name == "lg":
                            value["path_lg"] = f"{imgs_dir_path}/lg{extension}"
                            value["url_lg"] = f"{imgs_dir_url}/lg{extension}"
                            img.save(value["path_lg"], ext_upper)
                        elif size_name == "md":
                            value["path_md"] = f"{imgs_dir_path}/md{extension}"
                            value["url_md"] = f"{imgs_dir_url}/md{extension}"
                            img.save(value["path_md"], ext_upper)
                        elif size_name == "sm":
                            value["path_sm"] = f"{imgs_dir_path}/sm{extension}"
                            value["path_sm"] = f"{imgs_dir_url}/sm{extension}"
                            img.save(value["path_sm"], ext_upper)
                        elif size_name == "xs":
                            value["path_xs"] = f"{imgs_dir_path}/xs{extension}"
                            value["path_xs"] = f"{imgs_dir_url}/xs{extension}"
                            img.save(value["path_xs"], ext_upper)
        # Insert result.
        if params["is_save"]:
            if value["is_new_img"] or value["save_as_is"]:
                value["is_delete"] = False
                value["save_as_is"] = True
                params["result_map"][field.name] = value
