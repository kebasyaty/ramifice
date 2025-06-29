"""Units Management.

Management for `choices` parameter in dynamic field types.
"""

from typing import Any

from pymongo.asynchronous.collection import AsyncCollection

from ..utils import globals, translations
from ..utils.errors import PanicError
from ..utils.unit import Unit


class UnitMixin:
    """Units Management.

    Management for `choices` parameter in dynamic field types.
    """

    @classmethod
    async def unit_manager(cls: Any, unit: Unit) -> None:
        """Units Management.

        Management for `choices` parameter in dynamic field types.
        """
        curr_lang = translations.CURRENT_LOCALE
        # Get access to super collection.
        # (Contains Model state and dynamic field data.)
        super_collection: AsyncCollection = globals.MONGO_DATABASE[globals.SUPER_COLLECTION_NAME]
        # Get Model state.
        model_state: dict[str, Any] | None = await super_collection.find_one(
            filter={"collection_name": cls.META["collection_name"]}
        )
        # Check the presence of a Model state.
        if model_state is None:
            raise PanicError("Error: Model State - Not found!")
        # Get dynamic field data.
        choices: list | None = model_state["data_dynamic_fields"][unit.field]
        # Get Title.
        title = unit.title
        title = {lang: title.get(lang, "- -") for lang in translations.LANGUAGES}
        main_lang = translations.DEFAULT_LOCALE
        main_title = title[main_lang]
        # Add Unit to Model State.
        if not unit.is_delete:
            if choices is not None:
                choices.append({"title": title, "value": unit.value})
            else:
                choices = [{"title": title, "value": unit.value}]
            model_state["data_dynamic_fields"][unit.field] = choices
        else:
            # Delete Unit from Model State.
            if choices is None:
                msg = (
                    "Error: It is not possible to delete Unit."
                    + f"Title `{main_title}` not exists!"
                )
                raise PanicError(msg)
            is_key_exists: bool = False
            for item in choices:
                if main_title == item["title"][main_lang]:
                    is_key_exists = True
                    break
            if not is_key_exists:
                msg = (
                    "Error: It is not possible to delete Unit."
                    + f"Title `{main_title}` not exists!"
                )
                raise PanicError(msg)
            choices = [item for item in choices if item["title"][main_lang] != main_title]
            model_state["data_dynamic_fields"][unit.field] = choices or None
        # Update state of current Model in super collection.
        await super_collection.replace_one(
            filter={"collection_name": model_state["collection_name"]},
            replacement=model_state,
        )
        # Update metadata of current Model.
        cls.META["data_dynamic_fields"][unit.field] = choices or None
        # Update documents in the collection of the current Model.
        if unit.is_delete:
            unit_field: str = unit.field
            unit_value: float | int | str | None = unit.value
            collection: AsyncCollection = globals.MONGO_DATABASE[cls.META["collection_name"]]
            async for mongo_doc in collection.find():
                field_value = mongo_doc[unit_field]
                if field_value is not None:
                    if isinstance(unit_value, list):
                        value_list = mongo_doc[unit_field]
                        value_list.remove(unit_value)
                        mongo_doc[unit_field] = value_list or None
                    else:
                        mongo_doc[unit_field] = None
                await collection.replace_one(
                    filter={"_id": mongo_doc["_id"]},
                    replacement=mongo_doc,
                )
