"""Field of Model for upload file."""

import datetime
import os
import uuid

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
        target_dir: str = "",
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

    def from_base64(
        self,
        base64: str | None = None,
        filename: str | None = None,
        delete: bool = False,
    ) -> None:
        """Convert base64 to a file and save in the target directory."""
        base64 = base64 or None
        filename = filename or None
        value = FileData()
        value.is_new_file = True
        value.delete = delete

        if base64 is not None and filename is not None:
            extension: str = ""  # file extension
            target_name: str = ""  # target file name
            date_str: str = ""  # current date for the directory name
            target_path: str = ""  # path to target file
            # Get file extension.
            extension = os.path.splitext(filename)[1]
            if len(extension) == 0:
                raise FileHasNoExtensionError(
                    f"The file `{filename}` has no extension."
                )
            # Prepare Base64 content.
            base64 = base64.replace(",", "", 40)
            # Create target file name.
            target_name = f"{uuid.uuid4()}{extension}"
            # Create the current date for the directory name.
            date_str = datetime.datetime.now().strftime("%Y-%m-%d")
            # Create path to target file.
            target_path = f"{self.media_root}/{self.target_dir}/{date_str}"
            # Create target directory if it does not exist.
            if not os.path.exists(target_path):
                os.makedirs(target_path)
