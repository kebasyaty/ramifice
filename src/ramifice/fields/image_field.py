"""Field of Model for upload image."""

import os
import shutil
import uuid
from base64 import b64decode
from datetime import datetime
from pathlib import Path
from typing import Any

from PIL import Image

from ..errors import FileHasNoExtensionError
from ..mixins import JsonMixin
from ..store import DEBUG, IMG_INFO_DICT
from .general.field import Field
from .general.file_group import FileGroup


class ImageField(Field, FileGroup, JsonMixin):
    """Field of Model for upload image."""

    def __init__(  # noqa: D107
        self,
        label: str = "",
        disabled: bool = False,
        hide: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        required: bool = False,
        # The maximum size of the original image in bytes.
        max_size: int = 2097152,  # 2 MB = 2097152 Bytes (in binary)
        default: str | None = None,
        placeholder: str = "",
        target_dir: str = "images",
        accept: str = "image/png,image/jpeg,image/webp",
        # Available 4 sizes from lg to xs or None.
        # Example: {"lg": 1200, "md": 600, "sm": 300, "xs": 150 }
        thumbnails: dict[str, int] | None = None,
        # True - high quality and low performance for thumbnails.
        high_quality: bool = False,
    ):
        if DEBUG:
            if default is not None:
                if not isinstance(default, str):
                    raise AssertionError("Parameter `default` - Not а `str` type!")
                if len(default) == 0:
                    raise AssertionError(
                        "The `default` parameter should not contain an empty string!"
                    )
            if thumbnails is not None:
                if not isinstance(thumbnails, dict):
                    raise AssertionError("Parameter `thumbnails` - Not а `dict` type!")
                if len(thumbnails) == 0:
                    raise AssertionError(
                        "The `thumbnails` parameter should not contain an empty dictionary!"
                    )
                size_name_list = ["lg", "md", "sm", "xs"]
                curr_size_thumb: int = 0
                for size_name in thumbnails.keys():
                    if size_name not in size_name_list:
                        raise AssertionError(
                            f"The `thumbnails` parameter contains an unacceptable size name `{size_name}`!\n"
                            + " Allowed names: lg, md, sm, xs.\n"
                            + " Use all sizes is not necessary.",
                        )
                    max_size_thumb: int | None = thumbnails.get(size_name)
                    if max_size_thumb is not None:
                        if curr_size_thumb > 0 and max_size_thumb >= curr_size_thumb:
                            raise AssertionError(
                                "The `thumbnails` parameter -> "
                                + f"The `{size_name}` key should be less than a previous size!"
                                + 'Example: {"lg": 1200, "md": 600, "sm": 300, "xs": 150 }'
                            )
                        curr_size_thumb = max_size_thumb
            if not isinstance(label, str):
                raise AssertionError("Parameter `default` - Not а `str` type!")
            if not isinstance(disabled, bool):
                raise AssertionError("Parameter `disabled` - Not а `bool` type!")
            if not isinstance(hide, bool):
                raise AssertionError("Parameter `hide` - Not а `bool` type!")
            if not isinstance(ignored, bool):
                raise AssertionError("Parameter `ignored` - Not а `bool` type!")
            if not isinstance(ignored, bool):
                raise AssertionError("Parameter `ignored` - Not а `bool` type!")
            if not isinstance(hint, str):
                raise AssertionError("Parameter `hint` - Not а `str` type!")
            if warning is not None and not isinstance(warning, list):
                raise AssertionError("Parameter `warning` - Not а `list` type!")
            if not isinstance(placeholder, str):
                raise AssertionError("Parameter `placeholder` - Not а `str` type!")
            if not isinstance(required, bool):
                raise AssertionError("Parameter `required` - Not а `bool` type!")
            if not isinstance(max_size, int):
                raise AssertionError("Parameter `max_size` - Not а `int` type!")
            if not isinstance(target_dir, str):
                raise AssertionError("Parameter `target_dir` - Not а `str` type!")
            if not isinstance(accept, str):
                raise AssertionError("Parameter `accept` - Not а `str` type!")
            if not isinstance(high_quality, bool):
                raise AssertionError("Parameter `high_quality` - Not а `bool` type!")

        Field.__init__(
            self,
            label=label,
            disabled=disabled,
            hide=hide,
            ignored=ignored,
            hint=hint,
            warning=warning,
            field_type="ImageField",
            group="img",
        )
        FileGroup.__init__(
            self,
            placeholder=placeholder,
            required=required,
            max_size=max_size,
            default=default,
            target_dir=target_dir,
            accept=accept,
        )
        JsonMixin.__init__(self)

        self.value: dict[str, Any] | None = None
        # Available 4 sizes from lg to xs or None.
        # Example: {"lg": 1200, "md": 600, "sm": 300, "xs": 150 }
        self.thumbnails = thumbnails
        # True is high quality and low performance.
        self.high_quality = high_quality

    def from_base64(
        self,
        base64_str: str | None = None,
        filename: str | None = None,
        is_delete: bool = False,
    ) -> None:
        """Convert base64 to a image,
        get image information and save in the target directory.
        """  # noqa: D205
        base64_str = base64_str or None
        filename = filename or None
        img_info = IMG_INFO_DICT.copy()
        img_info["is_new_img"] = True
        img_info["is_delete"] = is_delete

        if base64_str is not None and filename is not None:
            # Get file extension.
            extension = Path(filename).suffix
            if len(extension) == 0:
                raise FileHasNoExtensionError(f"The image `{filename}` has no extension.")
            # Prepare Base64 content.
            for item in enumerate(base64_str):
                if item[1] == ",":
                    base64_str = base64_str[item[0] + 1 :]
                    break
                if item[0] == 40:
                    break
            # Create the current date for the directory name.
            date_str = datetime.now().strftime("%Y-%m-%d")
            # Directory name for the original image and its thumbnails.
            general_dir = uuid.uuid4()
            # Create path to target directory with images.
            imgs_dir_path = f"{self.media_root}/{self.target_dir}/{date_str}/{general_dir}"
            # Create url path to target directory with images.
            imgs_dir_url = f"{self.media_url}/{self.target_dir}/{date_str}/{general_dir}"
            # Create a new name for the original image.
            new_original_name = f"original{extension}"
            # Create path to main image.
            main_img_path = f"{imgs_dir_path}/{new_original_name}"
            # Create target directory if it does not exist.
            if not os.path.exists(imgs_dir_path):
                os.makedirs(imgs_dir_path)
            # Save main image in target directory.
            with open(main_img_path, mode="wb") as open_f:
                f_content = b64decode(base64_str)
                open_f.write(f_content)
            # Add paths for main image.
            img_info["path"] = main_img_path
            img_info["url"] = f"{imgs_dir_url}/{new_original_name}"
            # Add width and height.
            with Image.open(main_img_path) as img:
                width, height = img.size
                img_info["width"] = width
                img_info["height"] = height
            # Add original image name.
            img_info["name"] = filename
            # Add image extension.
            img_info["extension"] = extension
            # Transform extension to the upper register and delete the point.
            ext_upper = extension[1:].upper()
            if ext_upper == "JPG":
                ext_upper = "JPEG"
            img_info["ext_upper"] = ext_upper
            # Add path to target directory with images.
            img_info["imgs_dir_path"] = imgs_dir_path
            # Add url path to target directory with images.
            img_info["imgs_dir_url"] = imgs_dir_url
            # Add size of main image (in bytes).
            img_info["size"] = os.path.getsize(main_img_path)

        # to value.
        self.value = img_info

    # --------------------------------------------------------------------------
    def from_path(
        self,
        src_path: str | None = None,
        is_delete: bool = False,
    ) -> None:
        """Get image information and copy the image to the target directory."""
        src_path = src_path or None
        img_info = IMG_INFO_DICT.copy()
        img_info["is_new_img"] = True
        img_info["is_delete"] = is_delete

        if src_path is not None:
            # Get file extension.
            extension = Path(src_path).suffix
            if len(extension) == 0:
                msg = f"The image `{src_path}` has no extension."
                raise FileHasNoExtensionError(msg)
            # Create the current date for the directory name.
            date_str = datetime.now().strftime("%Y-%m-%d")
            # Directory name for the original image and its thumbnails.
            general_dir = uuid.uuid4()
            # Create path to target directory with images.
            imgs_dir_path = f"{self.media_root}/{self.target_dir}/{date_str}/{general_dir}"
            # Create url path to target directory with images.
            imgs_dir_url = f"{self.media_url}/{self.target_dir}/{date_str}/{general_dir}"
            # Create a new name for the original image.
            new_original_name = f"original{extension}"
            # Create path to main image.
            main_img_path = f"{imgs_dir_path}/{new_original_name}"
            # Create target directory if it does not exist.
            if not os.path.exists(imgs_dir_path):
                os.makedirs(imgs_dir_path)
            # Save main image in target directory.
            shutil.copyfile(src_path, main_img_path)
            # Add paths for main image.
            img_info["path"] = main_img_path
            img_info["url"] = f"{imgs_dir_url}/{new_original_name}"
            # Add width and height.
            with Image.open(main_img_path) as img:
                width, height = img.size
                img_info["width"] = width
                img_info["height"] = height
            # Add original image name.
            img_info["name"] = os.path.basename(src_path)
            # Add image extension.
            img_info["extension"] = extension
            # Transform extension to the upper register and delete the point.
            ext_upper = extension[1:].upper()
            if ext_upper == "JPG":
                ext_upper = "JPEG"
            img_info["ext_upper"] = ext_upper
            # Add path to target directory with images.
            img_info["imgs_dir_path"] = imgs_dir_path
            # Add url path to target directory with images.
            img_info["imgs_dir_url"] = imgs_dir_url
            # Add size of main image (in bytes).
            img_info["size"] = os.path.getsize(main_img_path)

        # to value.
        self.value = img_info
