"""Field of Model for upload file."""

from __future__ import annotations

__all__ = ("FileField",)

import logging
import uuid
from base64 import b64decode
from datetime import datetime
from os.path import getsize
from shutil import copyfile
from typing import Any

from anyio import Path, open_file, to_thread
from xloft.converters import to_human_size

from ramifice.fields.general.field import Field
from ramifice.fields.general.file_group import FileGroup
from ramifice.utils import constants
from ramifice.utils.constants import (
    MEDIA_ROOT,
    MEDIA_URL,
    UTC_TIMEZONE,
)
from ramifice.utils.errors import FileHasNoExtensionError
from ramifice.utils.mixins import JsonMixin

logger = logging.getLogger(__name__)


class FileField(Field, FileGroup, JsonMixin):
    """Field of Model for upload file.

    Agrs:
        label: Text label for a web form field.
        placeholder: Displays prompt text.
        default: Value by default.
        hide: Hide field from user.
        disabled: Blocks access and modification of the element.
        ignored: If true, the value of this field is not saved in the database.
        hint: An alternative for the `placeholder` parameter.
        warning: Warning information.
        required: Required field.
        max_size: The maximum allowed file size in bytes.
        target_dir: Directory for files inside media directory.
        accept: Describing which file types to allow. Example: ".pdf,.doc,.docx,application/msword".
    """

    def __init__(  # noqa: D107
        self,
        label: str = "",
        placeholder: str = "",
        default: str | None = None,
        hide: bool = False,
        disabled: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        required: bool = False,
        # The maximum size of the file in bytes.
        max_size: int = 2097152,  # 2 MB = 2097152 Bytes (in binary)
        target_dir: str = "files",
        accept: str = "",  # Example: ".pdf,.doc,.docx,application/msword"
    ) -> None:
        if constants.DEBUG:
            try:
                if default is not None:
                    if not isinstance(default, str):
                        raise AssertionError("Parameter `default` - Not а `str` type!")
                    if len(default) == 0:
                        raise AssertionError("The `default` parameter should not contain an empty string!")
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
            except AssertionError as err:
                logger.critical(str(err))
                raise err

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
        file_info: dict[str, Any] = {"save_as_is": False}
        file_info["is_new_file"] = True
        file_info["is_delete"] = is_delete

        if base64_str is not None and filename is not None:
            # Get file extension.
            extension = Path(filename).suffix
            if len(extension) == 0:
                msg = f"The file `{filename}` has no extension."
                logger.error(msg)
                raise FileHasNoExtensionError(msg)
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
            date_str: str = str(datetime.now(UTC_TIMEZONE).date())
            # Create path to target directory.
            dir_target_path = Path(
                MEDIA_ROOT,
                "uploads",
                self.target_dir,
                date_str,
            )
            # Create target directory if it does not exist.
            if not await dir_target_path.exists():
                await dir_target_path.mkdir(parents=True)
            # Create path to target file.
            f_target_path = f"{dir_target_path.as_posix()}/{f_uuid_name}"
            # Save file in target directory.
            async with await open_file(f_target_path, mode="wb") as open_f:
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
            file_info["size"] = await to_thread.run_sync(getsize, f_target_path)
            # Convert the number of bytes into a human-readable format.
            # Examples: 200 bytes | 1 KB | 1.5 MB.
            file_info["human_size"] = to_human_size(file_info["size"])
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
        file_info: dict[str, Any] = {"save_as_is": False}
        file_info["is_new_file"] = True
        file_info["is_delete"] = is_delete

        if src_path is not None:
            # Get file extension.
            extension = Path(src_path).suffix
            if len(extension) == 0:
                msg = f"The file `{src_path}` has no extension."
                logger.error(msg)
                raise FileHasNoExtensionError(msg)
            # Create new (uuid) file name.
            f_uuid_name = f"{uuid.uuid4()}{extension}"
            # Create the current date for the directory name.
            date_str: str = str(datetime.now(UTC_TIMEZONE).date())
            # Create path to target directory.
            dir_target_path = Path(
                MEDIA_ROOT,
                "uploads",
                self.target_dir,
                date_str,
            )
            # Create target directory if it does not exist.
            if not await dir_target_path.exists():
                await dir_target_path.mkdir(parents=True)
            # Create path to target file.
            f_target_path = f"{dir_target_path.as_posix()}/{f_uuid_name}"
            # Save file in target directory.
            await to_thread.run_sync(copyfile, src_path, f_target_path)
            # Add paths to target file.
            file_info["path"] = f_target_path
            file_info["url"] = f"{MEDIA_URL}/uploads/{self.target_dir}/{date_str}/{f_uuid_name}"
            # Add original file name.
            file_info["name"] = Path(src_path).name
            # Add file extension.
            file_info["extension"] = extension
            # Add file size (in bytes).
            file_info["size"] = await to_thread.run_sync(getsize, f_target_path)
            # Convert the number of bytes into a human-readable format.
            # Examples: 200 bytes | 1 KB | 1.5 MB.
            file_info["human_size"] = to_human_size(file_info["size"])
        #
        # to value.
        self.value = file_info
