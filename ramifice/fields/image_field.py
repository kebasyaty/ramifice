"""Field of Model for upload image."""

import os
import shutil
import uuid
from base64 import b64decode
from datetime import datetime
from pathlib import Path
from typing import Any

from ..errors import FileHasNoExtensionError
from ..mixins import FileJsonMixin
from ..types import ImageData
from .general.field import Field
from .general.file_group import FileGroup


class ImageField(Field, FileGroup, FileJsonMixin):
    """Field of Model for upload image.
    How to use, see <a href="https://github.com/kebasyaty/ramifice/tree/main/examples/files" target="_blank">example</a>.
    """

    def __init__(  # pylint: disable=too-many-arguments
        self,
        label: str = "",
        disabled: bool = False,
        hide: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        required: bool = False,
        max_size: int = 2097152,  # 2 MB
        default: str | None = None,
        placeholder: str = "",
        target_dir: str = "images",
        accept: str = "image/png,image/jpeg,image/webp",
    ):
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
        FileJsonMixin.__init__(self)

        self.value: ImageData | None = None

    def __str__(self):
        title = str(None)
        value = self.value
        if value is not None:
            title = str(value)
        return title

    def from_base64(
        self,
        base64_str: str | None = None,
        filename: str | None = None,
        is_delete: bool = False,
    ) -> None:
        """Convert base64 to a image,
        get image information and save in the target directory.
        """
        base64_str = base64_str or None
        filename = filename or None
        i_data = ImageData()
        i_data.is_new_img = True
        i_data.is_delete = is_delete

        if base64_str is not None and filename is not None:
            # Get file extension.
            extension = Path(filename).suffix
            if len(extension) == 0:
                raise FileHasNoExtensionError(
                    f"The image `{filename}` has no extension."
                )
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
            imgs_dir_path = (
                f"{self.media_root}/{self.target_dir}/{date_str}/{general_dir}"
            )
            # Create url path to target directory with images.
            imgs_dir_url = (
                f"{self.media_url}/{self.target_dir}/{date_str}/{general_dir}"
            )
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
            i_data.path = main_img_path
            i_data.url = f"{imgs_dir_url}/{new_original_name}"
            # Add original image name.
            i_data.name = filename
            # Add image extension.
            i_data.extension = extension
            # Add path to target directory with images.
            i_data.imgs_dir_path = imgs_dir_path
            # Add url path to target directory with images.
            i_data.imgs_dir_url = imgs_dir_url
            # Add size of main image (in bytes).
            i_data.size = os.path.getsize(main_img_path)

        # FileData to value.
        self.value = i_data

    # --------------------------------------------------------------------------
    def from_path(
        self,
        src_path: str | None = None,
        is_delete: bool = False,
    ) -> None:
        """Get image information and copy the image to the target directory."""
        src_path = src_path or None
        i_data = ImageData()
        i_data.is_new_img = True
        i_data.is_delete = is_delete

        if src_path is not None:
            # Get file extension.
            extension = Path(src_path).suffix
            if len(extension) == 0:
                raise FileHasNoExtensionError(
                    f"The image `{src_path}` has no extension."
                )
            # Create the current date for the directory name.
            date_str = datetime.now().strftime("%Y-%m-%d")
            # Directory name for the original image and its thumbnails.
            general_dir = uuid.uuid4()
            # Create path to target directory with images.
            imgs_dir_path = (
                f"{self.media_root}/{self.target_dir}/{date_str}/{general_dir}"
            )
            # Create url path to target directory with images.
            imgs_dir_url = (
                f"{self.media_url}/{self.target_dir}/{date_str}/{general_dir}"
            )
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
            i_data.path = main_img_path
            i_data.url = f"{imgs_dir_url}/{new_original_name}"
            # Add original image name.
            i_data.name = os.path.basename(src_path)
            # Add image extension.
            i_data.extension = extension
            # Add path to target directory with images.
            i_data.imgs_dir_path = imgs_dir_path
            # Add url path to target directory with images.
            i_data.imgs_dir_url = imgs_dir_url
            # Add size of main image (in bytes).
            i_data.size = os.path.getsize(main_img_path)

        # FileData to value.
        self.value = i_data

    @classmethod
    def from_dict(cls, json_dict: dict[str, Any]) -> Any:
        """Convert JSON string to a object instance."""
        obj = cls()
        for name, data in json_dict.items():
            if name != "value" or data is None:
                obj.__dict__[name] = data
            else:
                obj.__dict__[name] = ImageData.from_dict(data)
        return obj
