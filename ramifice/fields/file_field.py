"""Field of Model for upload file."""

import json
import os
import shutil
import uuid
from base64 import b64decode
from datetime import datetime
from pathlib import Path
from typing import Any

from ..errors import FileHasNoExtensionError
from ..types import FileData
from .general.field import Field
from .general.file_group import FileGroup


class FileField(Field, FileGroup):
    """Field of Model for upload file.
    How to use, see <a href="https://github.com/kebasyaty/ramifice/tree/main/examples/files" target="_blank">example</a>.
    """

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
        self.__value: FileData | None = None

    @property
    def value(self) -> FileData | None:
        """Sets value of field."""
        return self.__value

    @value.setter
    def value(self, value: FileData | None) -> None:
        self.__value = value

    # --------------------------------------------------------------------------
    def from_base64(
        self,
        base64_str: str | None = None,
        filename: str | None = None,
        delete: bool = False,
    ) -> None:
        """Convert base64 to a file,
        get file information and save in the target directory.
        """
        base64_str = base64_str or None
        filename = filename or None
        f_data = FileData()
        f_data.is_new_file = True
        f_data.delete = delete

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
            f_data.path = f_target_path
            f_data.url = f"{self.media_url}/{self.target_dir}/{date_str}/{f_uuid_name}"
            # Add original file name.
            f_data.name = filename
            # Add file extension.
            f_data.extension = extension
            # Add file size (in bytes).
            f_data.size = os.path.getsize(f_target_path)

        # FileData to value.
        self.__value = f_data

    # --------------------------------------------------------------------------
    def from_path(
        self,
        src_path: str | None = None,
        delete: bool = False,
    ) -> None:
        """Get file information and copy the file to the target directory."""
        src_path = src_path or None
        f_data = FileData()
        f_data.is_new_file = True
        f_data.delete = delete

        if src_path is not None:
            # Get file extension.
            extension = Path(src_path).suffix
            if len(extension) == 0:
                raise FileHasNoExtensionError(
                    f"The file `{src_path}` has no extension."
                )
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
            f_data.path = f_target_path
            f_data.url = f"{self.media_url}/{self.target_dir}/{date_str}/{f_uuid_name}"
            # Add original file name.
            f_data.name = os.path.basename(src_path)
            # Add file extension.
            f_data.extension = extension
            # Add file size (in bytes).
            f_data.size = os.path.getsize(f_target_path)

        # FileData to value.
        self.__value = f_data

    # --------------------------------------------------------------------------
    def to_dict(self) -> dict[str, str | int | bool | list[str] | None]:
        """Convert fields to a dictionary."""
        json_dict: dict[str, str | int | bool | list[str] | None] = {}
        for f_name, f_type in self.__dict__.items():
            f_name = f_name.rsplit("__", maxsplit=1)[-1]
            if not callable(f_type):
                if f_name != "value":
                    json_dict[f_name] = f_type
                else:
                    json_dict[f_name] = f_type.to_dict() if f_type is not None else None
        return json_dict

    @classmethod
    def from_dict(cls, json_dict: dict[str, Any]) -> Any:
        """Convert the JSON string to a Model instance."""
        f_obj = cls()
        for f_name, f_type in json_dict.items():
            f_obj.__dict__[f_name] = f_type
        return f_obj

    def to_json(self):
        """Convert a dictionary of fields to a JSON string."""
        return json.dumps(self.to_dict())
