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
from ramifice.types import Unit


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
        super_collection: AsyncCollection = store.MONGO_DATABASE[  # type: ignore[annotation-unchecked]
            store.SUPER_COLLECTION_NAME
        ]
        #
        model_state: dict[str, Any] | None = await super_collection.find_one(  # type: ignore[annotation-unchecked]
            {"collection_name": User.META["collection_name"]}
        )
        if model_state is None:
            raise PanicError("Error: Model State - Not found!")
        data_dynamic_fields = model_state["data_dynamic_fields"]
        choices: dict[str, float | int | str] = data_dynamic_fields["choice_float_dyn"]  # type: ignore[annotation-unchecked]
        self.assertIsNone(choices)
        choices = data_dynamic_fields["choice_float_mult_dyn"]  # type: ignore[annotation-unchecked]
        self.assertIsNone(choices)
        choices = data_dynamic_fields["choice_int_dyn"]  # type: ignore[annotation-unchecked]
        self.assertIsNone(choices)
        choices = data_dynamic_fields["choice_int_mult_dyn"]  # type: ignore[annotation-unchecked]
        self.assertIsNone(choices)
        choices = data_dynamic_fields["choice_txt_dyn"]  # type: ignore[annotation-unchecked]
        self.assertIsNone(choices)
        choices = data_dynamic_fields["choice_txt_mult_dyn"]  # type: ignore[annotation-unchecked]
        self.assertIsNone(choices)
        # Add Units:
        # ---------
        unit = Unit(
            field="choice_float_dyn",
            title="Title",
            value=1.0,
        )
        await User.unit_manager(unit)
        unit = Unit(
            field="choice_float_mult_dyn",
            title="Title",
            value=2.0,
        )
        await User.unit_manager(unit)
        unit = Unit(
            field="choice_int_dyn",
            title="Title",
            value=1,
        )
        await User.unit_manager(unit)
        unit = Unit(
            field="choice_int_mult_dyn",
            title="Title",
            value=2,
        )
        await User.unit_manager(unit)
        unit = Unit(
            field="choice_txt_dyn",
            title="Title",
            value="Some text",
        )
        await User.unit_manager(unit)
        unit = Unit(
            field="choice_txt_mult_dyn",
            title="Title",
            value="Some text 2",
        )
        await User.unit_manager(unit)
        #
        model_state = await super_collection.find_one(  # type: ignore[annotation-unchecked]
            {"collection_name": User.META["collection_name"]}
        )
        if model_state is None:
            raise PanicError("Error: Model State - Not found!")
        #
        data_dynamic_fields = model_state["data_dynamic_fields"]
        choices = data_dynamic_fields["choice_float_dyn"]  # type: ignore[annotation-unchecked]
        self.assertEqual(choices["Title"], 1.0)
        choices = data_dynamic_fields["choice_float_mult_dyn"]  # type: ignore[annotation-unchecked]
        self.assertEqual(choices["Title"], 2.0)
        choices = data_dynamic_fields["choice_int_dyn"]  # type: ignore[annotation-unchecked]
        self.assertEqual(choices["Title"], 1)
        choices = data_dynamic_fields["choice_int_mult_dyn"]  # type: ignore[annotation-unchecked]
        self.assertEqual(choices["Title"], 2)
        choices = data_dynamic_fields["choice_txt_dyn"]  # type: ignore[annotation-unchecked]
        self.assertEqual(choices["Title"], "Some text")
        choices = data_dynamic_fields["choice_txt_mult_dyn"]  # type: ignore[annotation-unchecked]
        self.assertEqual(choices["Title"], "Some text 2")
        #
        data_dynamic_fields = User.META["data_dynamic_fields"]
        choices = data_dynamic_fields["choice_float_dyn"]  # type: ignore[annotation-unchecked]
        self.assertEqual(choices["Title"], 1.0)
        choices = data_dynamic_fields["choice_float_mult_dyn"]  # type: ignore[annotation-unchecked]
        self.assertEqual(choices["Title"], 2.0)
        choices = data_dynamic_fields["choice_int_dyn"]  # type: ignore[annotation-unchecked]
        self.assertEqual(choices["Title"], 1)
        choices = data_dynamic_fields["choice_int_mult_dyn"]  # type: ignore[annotation-unchecked]
        self.assertEqual(choices["Title"], 2)
        choices = data_dynamic_fields["choice_txt_dyn"]  # type: ignore[annotation-unchecked]
        self.assertEqual(choices["Title"], "Some text")
        choices = data_dynamic_fields["choice_txt_mult_dyn"]  # type: ignore[annotation-unchecked]
        self.assertEqual(choices["Title"], "Some text 2")
        #
        user = User()
        self.assertEqual(user.choice_float_dyn.choices, {"Title": 1.0})
        self.assertEqual(user.choice_float_mult_dyn.choices, {"Title": 2.0})
        self.assertEqual(user.choice_int_dyn.choices, {"Title": 1})
        self.assertEqual(user.choice_int_mult_dyn.choices, {"Title": 2})
        self.assertEqual(user.choice_txt_dyn.choices, {"Title": "Some text"})
        self.assertEqual(user.choice_txt_mult_dyn.choices, {"Title": "Some text 2"})
        user.choice_float_dyn.value = 1.0
        user.choice_float_mult_dyn.value = [2.0]
        user.choice_int_dyn.value = 1
        user.choice_int_mult_dyn.value = [2]
        user.choice_txt_dyn.value = "Some text"
        user.choice_txt_mult_dyn.value = ["Some text 2"]
        #
        if not await user.save():
            user.print_err()
        #
        self.assertEqual(user.choice_float_dyn.value, 1.0)
        self.assertEqual(user.choice_float_mult_dyn.value, [2.0])
        self.assertEqual(user.choice_int_dyn.value, 1)
        self.assertEqual(user.choice_int_mult_dyn.value, [2])
        self.assertEqual(user.choice_txt_dyn.value, "Some text")
        self.assertEqual(user.choice_txt_mult_dyn.value, ["Some text 2"])
        # Delete Units:
        # ------------
        unit = Unit(
            field="choice_float_dyn",
            title="Title",
            value=1.0,
            is_delete=True,
        )
        await User.unit_manager(unit)
        unit = Unit(
            field="choice_float_mult_dyn",
            title="Title",
            value=2.0,
            is_delete=True,
        )
        await User.unit_manager(unit)
        unit = Unit(
            field="choice_int_dyn",
            title="Title",
            value=1,
            is_delete=True,
        )
        await User.unit_manager(unit)
        unit = Unit(
            field="choice_int_mult_dyn",
            title="Title",
            value=2,
            is_delete=True,
        )
        await User.unit_manager(unit)
        unit = Unit(
            field="choice_txt_dyn",
            title="Title",
            value="Some text",
            is_delete=True,
        )
        await User.unit_manager(unit)
        unit = Unit(
            field="choice_txt_mult_dyn",
            title="Title",
            value="Some text 2",
            is_delete=True,
        )
        await User.unit_manager(unit)
        #
        model_state = await super_collection.find_one(  # type: ignore[annotation-unchecked]
            {"collection_name": User.META["collection_name"]}
        )
        if model_state is None:
            raise PanicError("Error: Model State - Not found!")
        #
        data_dynamic_fields = model_state["data_dynamic_fields"]
        choices = data_dynamic_fields["choice_float_dyn"]  # type: ignore[annotation-unchecked]
        self.assertIsNone(choices)
        choices = data_dynamic_fields["choice_float_mult_dyn"]  # type: ignore[annotation-unchecked]
        self.assertIsNone(choices)
        choices = data_dynamic_fields["choice_int_dyn"]  # type: ignore[annotation-unchecked]
        self.assertIsNone(choices)
        choices = data_dynamic_fields["choice_int_mult_dyn"]  # type: ignore[annotation-unchecked]
        self.assertIsNone(choices)
        choices = data_dynamic_fields["choice_txt_dyn"]  # type: ignore[annotation-unchecked]
        self.assertIsNone(choices)
        choices = data_dynamic_fields["choice_txt_mult_dyn"]  # type: ignore[annotation-unchecked]
        self.assertIsNone(choices)
        #
        data_dynamic_fields = User.META["data_dynamic_fields"]
        choices = data_dynamic_fields["choice_float_dyn"]  # type: ignore[annotation-unchecked]
        self.assertIsNone(choices)
        choices = data_dynamic_fields["choice_float_mult_dyn"]  # type: ignore[annotation-unchecked]
        self.assertIsNone(choices)
        choices = data_dynamic_fields["choice_int_dyn"]  # type: ignore[annotation-unchecked]
        self.assertIsNone(choices)
        choices = data_dynamic_fields["choice_int_mult_dyn"]  # type: ignore[annotation-unchecked]
        self.assertIsNone(choices)
        choices = data_dynamic_fields["choice_txt_dyn"]  # type: ignore[annotation-unchecked]
        self.assertIsNone(choices)
        choices = data_dynamic_fields["choice_txt_mult_dyn"]  # type: ignore[annotation-unchecked]
        self.assertIsNone(choices)
        #
        user = await User.find_one_to_instance(filter={"_id": user._id.value})
        if user is None:
            raise PanicError("Error: User not found!")
        #
        self.assertIsNone(user.choice_float_dyn.choices)
        self.assertIsNone(user.choice_float_mult_dyn.choices)
        self.assertIsNone(user.choice_int_dyn.choices)
        self.assertIsNone(user.choice_int_mult_dyn.choices)
        self.assertIsNone(user.choice_txt_dyn.choices)
        self.assertIsNone(user.choice_txt_mult_dyn.choices)
        # ----------------------------------------------------------------------
        #
        # Delete database after test.
        await client.drop_database(database_name)
        await client.close()


if __name__ == "__main__":
    unittest.main()
