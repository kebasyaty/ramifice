"""Create or update document in database."""

from .. import store
from ..errors import PanicError


class SaveMixin:
    """Create or update document in database."""

    async def save(self) -> bool:
        """Create or update document in database.
        This method pre-uses the `check` method.
        """
        if not self.__class__.META["is_migrat_model"]:  # type: ignore[attr-defined]
            msg = (
                f"Model: `{self.full_model_name()}` > "  # type: ignore[attr-defined]
                + "Param: `is_migrat_model` (False) => "
                + "This Model is not migrated to database!"
            )
            raise PanicError(msg)
        # Get collection.
        collection = store.MONGO_DATABASE[self.__class__.META["collection_name"]]  # type: ignore[index, attr-defined]
        # Check and get ResultCheck.
        result_check = self.check(is_save=True)  # type: ignore[attr-defined]
        #
        # If everything is completed successfully.
        return True
