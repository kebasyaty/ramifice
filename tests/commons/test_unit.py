"""Testing `Ramifice > QCommonsMixin > UnitMixin` module."""

import unittest
from typing import Any

from pymongo import AsyncMongoClient
from pymongo.asynchronous.collection import AsyncCollection

from ramifice import model, store
from ramifice.errors import PanicError
from ramifice.fields import (
    ChoiceFloatDynField,
    ChoiceFloatMultDynField,
    ChoiceIntDynField,
    ChoiceIntMultDynField,
    ChoiceTextDynField,
    ChoiceTextMultDynField,
)
from ramifice.migration import Monitor


@model(service_name="Accounts")
class User:
    """Model for testing."""

    def fields(self):
        self.choice_float_dyn = ChoiceFloatDynField()
        self.choice_float_mult_dyn = ChoiceFloatMultDynField()
        self.choice_int_dyn = ChoiceIntDynField()
        self.choice_int_mult_dyn = ChoiceIntMultDynField()
        self.choice_txt_dyn = ChoiceTextDynField()
        self.choice_txt_mult_dyn = ChoiceTextMultDynField()


class TestCommonUnitMixin(unittest.IsolatedAsyncioTestCase):
    """Testing `Ramifice > QCommonsMixin > UnitMixin` module."""

    async def test_unit_mixin_methods(self):
        """Testing OneMixin methods."""
        # Maximum number of characters 60.
        database_name = "test_unit_mixin_methods"

        # Delete database before test.
        # (if the test fails)
        client = AsyncMongoClient()
        await client.drop_database(database_name)
        await client.close()

        client = AsyncMongoClient()
        await Monitor(
            database_name=database_name,
            mongo_client=client,
        ).migrat()
        #
        # HELLISH BURN
        # ----------------------------------------------------------------------
        user = User()
        # self.assertTrue(await m.save())
        if not await user.save():
            user.print_err()
        #
        super_collection: AsyncCollection = store.MONGO_DATABASE[  # type: ignore[annotation-unchecked]
            store.SUPER_COLLECTION_NAME
        ]
        #
        model_state: dict[str, Any] | None = await super_collection.find_one(  # type: ignore[annotation-unchecked]
            {"collection_name": User.META["collection_name"]}
        )
        if model_state is None:
            raise PanicError("Error: Model State - Not found!")
        choices: dict[str, float | int | str] = model_state["data_dynamic_fields"][  # type: ignore[annotation-unchecked]
            "choice_float_dyn"
        ]
        self.assertIsNone(choices)
        choices = model_state["data_dynamic_fields"][  # type: ignore[annotation-unchecked]
            "choice_float_mult_dyn"
        ]
        self.assertIsNone(choices)
        choices = model_state["data_dynamic_fields"][  # type: ignore[annotation-unchecked]
            "choice_int_dyn"
        ]
        self.assertIsNone(choices)
        choices = model_state["data_dynamic_fields"][  # type: ignore[annotation-unchecked]
            "choice_int_mult_dyn"
        ]
        self.assertIsNone(choices)
        choices = model_state["data_dynamic_fields"][  # type: ignore[annotation-unchecked]
            "choice_txt_dyn"
        ]
        self.assertIsNone(choices)
        choices = model_state["data_dynamic_fields"][  # type: ignore[annotation-unchecked]
            "choice_txt_mult_dyn"
        ]
        self.assertIsNone(choices)
        # ----------------------------------------------------------------------
        #
        # Delete database after test.
        await client.drop_database(database_name)
        await client.close()


if __name__ == "__main__":
    unittest.main()
