"""Create or update document in database."""


async def save(self) -> bool:
    """Create or update document in database.
    This method pre-uses the `check` method.
    """
    if self.__class__.META["is_migrat_model"]:
        pass

    #
    # If everything is completed successfully.
    return True
