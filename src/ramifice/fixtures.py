"""Fixtures - To populate the database with pre-created data.

Runs automatically during Model migration.
"""

from datetime import datetime
from typing import Any

import yaml
from dateutil.parser import parse
from pymongo.asynchronous.collection import AsyncCollection
from termcolor import colored

from .errors import PanicError


async def apply_fixture(
    fixture_name: str,
    cls_model: Any,
    collection: AsyncCollection,
) -> None:
    """Apply fixture for current Model.

    Runs automatically during Model migration.
    """
    fixture_path: str = f"config/fixtures/{fixture_name}.yml"
    data_yaml: dict[str, Any] | list[dict[str, Any]] | None = None

    with open(fixture_path, "r") as file:
        data_yaml = yaml.safe_load(file)

    if not bool(data_yaml):
        msg = (
            f"Model: `{cls_model.META['full_model_name']}` > "
            + f"META param: `fixture_name` ({fixture_name}) => "
            + "It seems that fixture is empty or it has incorrect contents!"
        )
        raise PanicError(msg)

    if not isinstance(data_yaml, list):
        data_yaml = [data_yaml]

    for data in data_yaml:
        inst_model = cls_model()
        for field_name, field_data in inst_model.__dict__.items():
            if callable(field_data) or field_data.ignored:
                continue
            group = field_data.group
            value: Any | None = data.get(field_name)
            if value == "None":
                value = None
            if value is not None:
                if group == "file" or group == "img":
                    field_data.from_path(value)
                elif group == "date":
                    field_data.value = parse(value)
                else:
                    field_data.value = value
        # Check Model.
        result_check: dict[str, Any] = await inst_model.check(
            is_save=True,
            collection=collection,
        )
        # If the check fails.
        if not result_check["is_valid"]:
            await collection.database.drop_collection(collection.name)
            print(colored("\nFIXTURE:", "red", attrs=["bold"]))
            print(colored(fixture_path, "blue", attrs=["bold"]))
            inst_model.print_err()
            raise PanicError("!!!")
        # Get data for document.
        checked_data: dict[str, Any] = result_check["data"]
        # Add date and time.
        today = datetime.now()
        checked_data["created_at"] = today
        checked_data["updated_at"] = today
        # Run hook.
        await inst_model.pre_create()
        # Insert doc.
        try:
            await collection.insert_one(checked_data)
        except:
            await collection.database.drop_collection(collection.name)
        # Run hook.
        await inst_model.post_create()
