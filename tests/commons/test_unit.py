"""Testing `Ramifice > QCommonsMixin > UnitMixin` module."""

import unittest
from typing import Any

from pymongo import AsyncMongoClient
from pymongo.asynchronous.collection import AsyncCollection

from ramifice import Unit, model
from ramifice.fields import (
    ChoiceFloatDynField,
    ChoiceFloatMultDynField,
    ChoiceIntDynField,
    ChoiceIntMultDynField,
    ChoiceTextDynField,
    ChoiceTextMultDynField,
)
from ramifice.utils import globals
from ramifice.utils.errors import PanicError
from ramifice.utils.migration import Monitor


@model(service_name="Accounts")
class User:
    """Model for testing."""

    def fields(self):
        """For adding fields."""
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

        client: AsyncMongoClient = AsyncMongoClient()

        # Delete database before test.
        # (if the test fails)
        await client.drop_database(database_name)
        await client.close()

        client = AsyncMongoClient()
        await Monitor(
            database_name=database_name,
            mongo_client=client,
        ).migrate()
        #
        # HELLISH BURN
        # ----------------------------------------------------------------------
        super_collection: AsyncCollection = globals.MONGO_DATABASE[globals.SUPER_COLLECTION_NAME]
        #
        model_state: dict[str, Any] | None = await super_collection.find_one(
            {"collection_name": User.META["collection_name"]}
        )
        if model_state is None:
            raise PanicError("Error: Model State - Not found!")
        data_dynamic_fields = model_state["data_dynamic_fields"]
        choices: dict[str, float | int | str] = data_dynamic_fields["choice_float_dyn"]
        self.assertIsNone(choices)
        choices = data_dynamic_fields["choice_float_mult_dyn"]
        self.assertIsNone(choices)
        choices = data_dynamic_fields["choice_int_dyn"]
        self.assertIsNone(choices)
        choices = data_dynamic_fields["choice_int_mult_dyn"]
        self.assertIsNone(choices)
        choices = data_dynamic_fields["choice_txt_dyn"]
        self.assertIsNone(choices)
        choices = data_dynamic_fields["choice_txt_mult_dyn"]
        self.assertIsNone(choices)
        # Add Units:
        # ---------
        unit = Unit(
            field="choice_float_dyn",
            title={"en": "Title"},
            value=1.0,
        )
        await User.unit_manager(unit)
        unit = Unit(
            field="choice_float_mult_dyn",
            title={"en": "Title"},
            value=2.0,
        )
        await User.unit_manager(unit)
        unit = Unit(
            field="choice_int_dyn",
            title={"en": "Title"},
            value=1,
        )
        await User.unit_manager(unit)
        unit = Unit(
            field="choice_int_mult_dyn",
            title={"en": "Title"},
            value=2,
        )
        await User.unit_manager(unit)
        unit = Unit(
            field="choice_txt_dyn",
            title={"en": "Title"},
            value="Some text",
        )
        await User.unit_manager(unit)
        unit = Unit(
            field="choice_txt_mult_dyn",
            title={"en": "Title"},
            value="Some text 2",
        )
        await User.unit_manager(unit)
        #
        model_state = await super_collection.find_one(
            {"collection_name": User.META["collection_name"]}
        )
        if model_state is None:
            raise PanicError("Error: Model State - Not found!")
        #
        data_dynamic_fields = model_state["data_dynamic_fields"]
        choices = data_dynamic_fields["choice_float_dyn"][0]
        self.assertEqual(choices["title"]["en"], "Title")
        self.assertEqual(choices["value"], 1.0)
        choices = data_dynamic_fields["choice_float_mult_dyn"][0]
        self.assertEqual(choices["title"]["en"], "Title")
        self.assertEqual(choices["value"], 2.0)
        choices = data_dynamic_fields["choice_int_dyn"][0]
        self.assertEqual(choices["title"]["en"], "Title")
        self.assertEqual(choices["value"], 1.0)
        choices = data_dynamic_fields["choice_int_mult_dyn"][0]
        self.assertEqual(choices["title"]["en"], "Title")
        self.assertEqual(choices["value"], 2)
        choices = data_dynamic_fields["choice_txt_dyn"][0]
        self.assertEqual(choices["title"]["en"], "Title")
        self.assertEqual(choices["value"], "Some text")
        choices = data_dynamic_fields["choice_txt_mult_dyn"][0]
        self.assertEqual(choices["title"]["en"], "Title")
        self.assertEqual(choices["value"], "Some text 2")
        #
        data_dynamic_fields = User.META["data_dynamic_fields"]
        choices = data_dynamic_fields["choice_float_dyn"][0]
        self.assertEqual(choices["title"]["en"], "Title")
        self.assertEqual(choices["value"], 1.0)
        choices = data_dynamic_fields["choice_float_mult_dyn"][0]
        self.assertEqual(choices["title"]["en"], "Title")
        self.assertEqual(choices["value"], 2.0)
        choices = data_dynamic_fields["choice_int_dyn"][0]
        self.assertEqual(choices["title"]["en"], "Title")
        self.assertEqual(choices["value"], 1.0)
        choices = data_dynamic_fields["choice_int_mult_dyn"][0]
        self.assertEqual(choices["title"]["en"], "Title")
        self.assertEqual(choices["value"], 2)
        choices = data_dynamic_fields["choice_txt_dyn"][0]
        self.assertEqual(choices["title"]["en"], "Title")
        self.assertEqual(choices["value"], "Some text")
        choices = data_dynamic_fields["choice_txt_mult_dyn"][0]
        self.assertEqual(choices["title"]["en"], "Title")
        self.assertEqual(choices["value"], "Some text 2")
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
        #
        # Delete Units:
        # ------------
        unit = Unit(
            field="choice_float_dyn",
            title={"en": "Title"},
            value=1.0,
            is_delete=True,
        )
        await User.unit_manager(unit)
        unit = Unit(
            field="choice_float_mult_dyn",
            title={"en": "Title"},
            value=2.0,
            is_delete=True,
        )
        await User.unit_manager(unit)
        unit = Unit(
            field="choice_int_dyn",
            title={"en": "Title"},
            value=1,
            is_delete=True,
        )
        await User.unit_manager(unit)
        unit = Unit(
            field="choice_int_mult_dyn",
            title={"en": "Title"},
            value=2,
            is_delete=True,
        )
        await User.unit_manager(unit)
        unit = Unit(
            field="choice_txt_dyn",
            title={"en": "Title"},
            value="Some text",
            is_delete=True,
        )
        await User.unit_manager(unit)
        unit = Unit(
            field="choice_txt_mult_dyn",
            title={"en": "Title"},
            value="Some text 2",
            is_delete=True,
        )
        await User.unit_manager(unit)
        #
        model_state = await super_collection.find_one(
            {"collection_name": User.META["collection_name"]}
        )
        if model_state is None:
            raise PanicError("Error: Model State - Not found!")
        #
        data_dynamic_fields = model_state["data_dynamic_fields"]
        choices = data_dynamic_fields["choice_float_dyn"]
        self.assertIsNone(choices)
        choices = data_dynamic_fields["choice_float_mult_dyn"]
        self.assertIsNone(choices)
        choices = data_dynamic_fields["choice_int_dyn"]
        self.assertIsNone(choices)
        choices = data_dynamic_fields["choice_int_mult_dyn"]
        self.assertIsNone(choices)
        choices = data_dynamic_fields["choice_txt_dyn"]
        self.assertIsNone(choices)
        choices = data_dynamic_fields["choice_txt_mult_dyn"]
        self.assertIsNone(choices)
        #
        data_dynamic_fields = User.META["data_dynamic_fields"]
        choices = data_dynamic_fields["choice_float_dyn"]
        self.assertIsNone(choices)
        choices = data_dynamic_fields["choice_float_mult_dyn"]
        self.assertIsNone(choices)
        choices = data_dynamic_fields["choice_int_dyn"]
        self.assertIsNone(choices)
        choices = data_dynamic_fields["choice_int_mult_dyn"]
        self.assertIsNone(choices)
        choices = data_dynamic_fields["choice_txt_dyn"]
        self.assertIsNone(choices)
        choices = data_dynamic_fields["choice_txt_mult_dyn"]
        self.assertIsNone(choices)
        #
        await user.refrash_from_db()
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
