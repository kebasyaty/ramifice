"""Testing `Ramifice > QCommonsMixin > UnitMixin` module."""

import unittest

from pymongo import AsyncMongoClient

from ramifice import model, store
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
        m = User()
        # self.assertTrue(await m.save())
        if not await m.save():
            m.print_err()
        #
        doc = await User.find_one({"_id": m._id.value})
        self.assertTrue(isinstance(doc, dict))
        #
        model = await User.find_one_to_instance({"_id": m._id.value})
        self.assertEqual(model._id.value, m._id.value)
        #
        json_str = await User.find_one_to_json({"_id": m._id.value})
        self.assertEqual(json_str, m.to_json())
        #
        await User.delete_one({"_id": m._id.value})
        self.assertEqual(await User.estimated_document_count(), 0)
        #
        m = User()
        if not await m.save():
            m.print_err()
        doc = await User.find_one_and_delete({"_id": m._id.value})
        self.assertEqual(doc["_id"], m._id.value)
        self.assertEqual(await User.estimated_document_count(), 0)
        # ----------------------------------------------------------------------
        #
        # Delete database after test.
        await client.drop_database(database_name)
        await client.close()


if __name__ == "__main__":
    unittest.main()
