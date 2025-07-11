"""Field of Model for upload file."""

import os
import uuid
from base64 import b64decode
from datetime import date
from pathlib import Path

import aiofiles
from aioshutil import copyfile

from ramifice.fields.general.field import Field
from ramifice.fields.general.file_group import FileGroup
from ramifice.utils import constants
from ramifice.utils.constants import MEDIA_ROOT, MEDIA_URL
from ramifice.utils.errors import FileHasNoExtensionError
from ramifice.utils.mixins.json_converter import JsonMixin


class FileField(Field, FileGroup, JsonMixin):
    """Field of Model for upload file."""

    def __init__(  # noqa: D107
        self,
        label: str = "",
        disabled: bool = False,
        hide: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        required: bool = False,
        # The maximum size of the file in bytes.
        max_size: int = 2097152,  # 2 MB = 2097152 Bytes (in binary)
        default: str | None = None,
        placeholder: str = "",
        target_dir: str = "files",
        accept: str = "",
    ):
        if constants.DEBUG:
            if default is not None:
                if not isinstance(default, str):
                    raise AssertionError("Parameter `default` - Not а `str` type!")
                if len(default) == 0:
                    raise AssertionError(
                        "The `default` parameter should not contain an empty string!"
                    )
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

        self.value: dict[str, str | int | bool] | None = None

    async def from_base64(
        self,
        base64_str: str | None = None,
        filename: str | None = None,
        is_delete: bool = False,
    ) -> None:
        """Convert base64 to a file,
        get file information and save in the target directory.
        """  # noqa: D205
        base64_str = base64_str or None
        filename = filename or None
        file_info: dict[str, str | int | bool] = {"save_as_is": False}
        file_info["is_new_file"] = True
        file_info["is_delete"] = is_delete

        if base64_str is not None and filename is not None:
            # Get file extension.
            extension = Path(filename).suffix
            if len(extension) == 0:
                raise FileHasNoExtensionError(f"The file `{filename}` has no extension.")
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
            date_str: str = str(date.today())
            # Create path to target directory.
            dir_target_path = f"{MEDIA_ROOT}/uploads/{self.target_dir}/{date_str}"
            # Create target directory if it does not exist.
            if not await aiofiles.os.path.exists(dir_target_path):
                await aiofiles.os.makedirs(dir_target_path)
            # Create path to target file.
            f_target_path = f"{dir_target_path}/{f_uuid_name}"
            # Save file in target directory.
            async with aiofiles.open(f_target_path, mode="wb") as open_f:
                f_content = b64decode(base64_str)
                await open_f.write(f_content)
            # Add paths to target file.
            file_info["path"] = f_target_path
            file_info["url"] = f"{MEDIA_URL}/uploads/{self.target_dir}/{date_str}/{f_uuid_name}"
            # Add original file name.
            file_info["name"] = filename
            # Add file extension.
            file_info["extension"] = extension
            # Add file size (in bytes).
            file_info["size"] = await aiofiles.os.path.getsize(f_target_path)
        #
        # to value.
        self.value = file_info

    async def from_path(
        self,
        src_path: str | None = None,
        is_delete: bool = False,
    ) -> None:
        """Get file information and copy the file to the target directory."""
        src_path = src_path or None
        file_info: dict[str, str | int | bool] = {"save_as_is": False}
        file_info["is_new_file"] = True
        file_info["is_delete"] = is_delete

        if src_path is not None:
            # Get file extension.
            extension = Path(src_path).suffix
            if len(extension) == 0:
                msg = f"The file `{src_path}` has no extension."
                raise FileHasNoExtensionError(msg)
            # Create new (uuid) file name.
            f_uuid_name = f"{uuid.uuid4()}{extension}"
            # Create the current date for the directory name.
            date_str: str = str(date.today())
            # Create path to target directory.
            dir_target_path = f"{MEDIA_ROOT}/uploads/{self.target_dir}/{date_str}"
            # Create target directory if it does not exist.
            if not await aiofiles.os.path.exists(dir_target_path):
                await aiofiles.os.makedirs(dir_target_path)
            # Create path to target file.
            f_target_path = f"{dir_target_path}/{f_uuid_name}"
            # Save file in target directory.
            await copyfile(src_path, f_target_path)
            # Add paths to target file.
            file_info["path"] = f_target_path
            file_info["url"] = f"{MEDIA_URL}/uploads/{self.target_dir}/{date_str}/{f_uuid_name}"
            # Add original file name.
            file_info["name"] = os.path.basename(src_path)
            # Add file extension.
            file_info["extension"] = extension
            # Add file size (in bytes).
            file_info["size"] = await aiofiles.os.path.getsize(f_target_path)
        #
        # to value.
        self.value = file_info
