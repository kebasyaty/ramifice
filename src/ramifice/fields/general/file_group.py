"""General additional parameters for file fields."""

from __future__ import annotations

__all__ = ("FileGroup",)


class FileGroup:
    """General additional parameters for file fields.

    Args:
        placeholder: Displays prompt text.
        required: Required field.
        max_size: The maximum allowed file size in bytes.
        default: Default file path.
        target_dir: Directory for files inside media directory.
        accept: Describing which file types to allow.
    """

    def __init__(  # noqa: D107
        self,
        placeholder: str = "",
        required: bool = False,
        max_size: int = 2097152,  # 2 MB
        default: str | None = None,
        target_dir: str = "",
        accept: str = "",
    ) -> None:
        self.input_type = "file"
        self.placeholder = placeholder
        self.required = required
        self.max_size = max_size
        self.default = default
        self.target_dir = target_dir
        self.accept = accept
