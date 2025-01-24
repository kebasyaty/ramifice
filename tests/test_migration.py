"""Testing the module `ramifice.migration`."""

import unittest

from ramifice.migration import ModelState

# from pymongo import AsyncMongoClient


class TestMigration(unittest.IsolatedAsyncioTestCase):
    """Testing the module `ramifice.migration`."""

    async def test_class_model_state(self):
        """Testing a class `ModelState`."""
        ms = ModelState()
        self.assertEqual(ms.collection_name, "")
        self.assertEqual(ms.field_name_and_type_list, {})
        self.assertEqual(ms.data_dynamic_fields, {})
        self.assertFalse(ms.is_model_exist)
