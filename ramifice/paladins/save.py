"""Create or update document in database."""

from ..errors import PanicError


async def save(self) -> bool:
    """Create or update document in database.
    This method pre-uses the `check` method.
    """
    if not self.__class__.META["is_migrat_model"]:
        msg = (
            f"Model: `{self.full_model_name()}` > "
            + "Param: `is_migrat_model` (False) => "
            + "This Model is not migrated to database!"
        )
        raise PanicError(msg)

    #
    # If everything is completed successfully.
    return True
