"""General additional parameters for file fields."""


class FileGroup:
    """General additional parameters for file fields."""

    def __init__(self,
                 input_type: str = "",
                 required: bool = False,
                 max_size: int = 2097152,  # 2 MB
                 default: str | None = None,
                 ):
        self.__input_type = input_type
        self.__value: str | None = None
        self.__required = required
        self.__max_size = max_size
        self.__default = default

    @property
    def input_type(self) -> str:
        """Input type for a web form field.
        Html tag: input type="file".
        """
        return self.__input_type

    # --------------------------------------------------------------------------
    @property
    def value(self) -> str | None:
        """Sets the value of an element."""
        return self.__value

    @value.setter
    def value(self, value: str | None) -> None:
        self.__value = value

    # --------------------------------------------------------------------------
    @property
    def required(self) -> bool:
        """Required field."""
        return self.__required

    # --------------------------------------------------------------------------
    @property
    def max_size(self) -> int:
        """The maximum allowed file size in bytes.
        1 MB = 1048576 Bytes (in binary).
        """
        return self.__max_size

    # --------------------------------------------------------------------------
    @property
    def default(self) -> str | None:
        """Default file path.
        Example: 'public/media/default/nodoc.docx'
        """
        return self.__default
