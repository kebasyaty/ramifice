"""Field of Model for upload file."""

import os
import shutil
import uuid
from base64 import b64decode
from datetime import datetime
from pathlib import Path
from typing import Any

from ..errors import FileHasNoExtensionError
from ..mixins import JsonMixin
from ..store import DEBUG
from ..types import FILE_DATA_TYPE
from .general.field import Field
from .general.file_group import FileGroup


class FileField(Field, FileGroup, JsonMixin):
    """Field of Model for upload file.
    How to use, see <a href="https://github.com/kebasyaty/ramifice/tree/main/examples/files" target="_blank">example</a>.
    """

    # pylint: disable=too-many-arguments
    def __init__(
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
        target_dir: str = "files",
        accept: str = "",
    ):
        if DEBUG:
            if default is not None:
                if not isinstance(default, str):
                    raise AssertionError("Parameter `default` - Not а `str` type!")
                if len(default) == 0:
                    raise AssertionError(
                        "The `default` parameter should not contain an empty string!"
                    )

        Field.__init__(
            self,
            label=label,
            disabled=disabled,
            hide=hide,
            ignored=ignored,
            hint=hint,
            warning=warning,
            field_type="FileField",
            group="file",
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

    def from_base64(
        self,
        base64_str: str | None = None,
        filename: str | None = None,
        is_delete: bool = False,
    ) -> None:
        """Convert base64 to a file,
        get file information and save in the target directory.
        """
        base64_str = base64_str or None
        filename = filename or None
        f_data = FILE_DATA_TYPE.copy()
        f_data["is_new_file"] = True
        f_data["is_delete"] = is_delete

        if base64_str is not None and filename is not None:
            # Get file extension.
            extension = Path(filename).suffix
            if len(extension) == 0:
                raise FileHasNoExtensionError(
                    f"The file `{filename}` has no extension."
                )
            # Prepare Base64 content.
            for item in enumerate(base64_str):
                if item[1] == ",":
                    base64_str = base64_str[item[0] + 1 :]
                    break
                if item[0] == 40:
                    break
            # Create new (uuid) file name.
            f_uuid_name = f"{uuid.uuid4()}{extension}"
            # Create the current date for the directory name.
            date_str = datetime.now().strftime("%Y-%m-%d")
            # Create path to target directory.
            dir_target_path = f"{self.media_root}/{self.target_dir}/{date_str}"
            # Create target directory if it does not exist.
            if not os.path.exists(dir_target_path):
                os.makedirs(dir_target_path)
            # Create path to target file.
            f_target_path = f"{dir_target_path}/{f_uuid_name}"
            # Save file in target directory.
            with open(f_target_path, mode="wb") as open_f:
                f_content = b64decode(base64_str)
                open_f.write(f_content)
            # Add paths to target file.
            f_data["path"] = f_target_path
            f_data["url"] = (
                f"{self.media_url}/{self.target_dir}/{date_str}/{f_uuid_name}"
            )
            # Add original file name.
            f_data["name"] = filename
            # Add file extension.
            f_data["extension"] = extension
            # Add file size (in bytes).
            f_data["size"] = os.path.getsize(f_target_path)

        # to value.
        self.value = f_data

    # --------------------------------------------------------------------------
    def from_path(
        self,
        src_path: str | None = None,
        is_delete: bool = False,
    ) -> None:
        """Get file information and copy the file to the target directory."""
        src_path = src_path or None
        f_data = FILE_DATA_TYPE.copy()
        f_data["is_new_file"] = True
        f_data["is_delete"] = is_delete

        if src_path is not None:
            # Get file extension.
            extension = Path(src_path).suffix
            if len(extension) == 0:
                msg = f"The file `{src_path}` has no extension."
                raise FileHasNoExtensionError(msg)
            # Create new (uuid) file name.
            f_uuid_name = f"{uuid.uuid4()}{extension}"
            # Create the current date for the directory name.
            date_str = datetime.now().strftime("%Y-%m-%d")
            # Create path to target directory.
            dir_target_path = f"{self.media_root}/{self.target_dir}/{date_str}"
            # Create target directory if it does not exist.
            if not os.path.exists(dir_target_path):
                os.makedirs(dir_target_path)
            # Create path to target file.
            f_target_path = f"{dir_target_path}/{f_uuid_name}"
            # Save file in target directory.
            shutil.copyfile(src_path, f_target_path)
            # Add paths to target file.
            f_data["path"] = f_target_path
            f_data["url"] = (
                f"{self.media_url}/{self.target_dir}/{date_str}/{f_uuid_name}"
            )
            # Add original file name.
            f_data["name"] = os.path.basename(src_path)
            # Add file extension.
            f_data["extension"] = extension
            # Add file size (in bytes).
            f_data["size"] = os.path.getsize(f_target_path)

        # to value.
        self.value = f_data
