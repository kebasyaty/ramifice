"""General additional parameters for file fields."""


class FileGroup:
    """General additional parameters for file fields."""

    def __init__(self,
                 required: bool = False,
                 max_size: int = 2097152,  # 2 MB
                 default: str | None = None,
                 target_dir: str = '',
                 accept: str = '',
                 ):
        self.__input_type = 'file'
        self.__value: str | None = None
        self.__required = required
        self.__max_size = max_size
        self.__default = default
        self.__target_dir = target_dir
        self.__accept = accept

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

    # --------------------------------------------------------------------------
    @property
    def target_dir(self) -> str | None:
        """Directory for files inside media directory.
        Example (file): 'files|resume|reports'
        Example (image): 'avatars|photos|images'
        """
        return self.__target_dir

    # --------------------------------------------------------------------------
    @property
    def accept(self) -> str | None:
        """Describing which file types to allow.
        HTML attribute: accept.
        Example (file): '.pdf,.doc,.docx,application/msword'
        Example (image): 'image/png,image/jpeg,image/webp'
        """
        return self.__accept
