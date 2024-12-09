"""Classes of Group parameters for fields of Model."""


class TextGroup:
    """Parameters for the text group of fields."""

    def __init__(self,
                 input_type: str = "",
                 ):
        self.__input_type = input_type

    # --------------------------------------------------------------------------
    @property
    def input_type(self) -> str:
        """Input type for a web form field."""
        return self.__input_type
