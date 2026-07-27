"""Testing the `dynamic_choices` example."""

from __future__ import annotations

import unittest

from pymongo import AsyncMongoClient

from ramifice import (
    Migration,
    Model,
    Translator,
    Unit,
    fields,
    meta,
)
from ramifice.config import Config

_ = Translator.STUB_TRANSLATOR_FOR_ATTRIBUTES_OF_FIELD


@meta(service_name="Goods")
class Product(Model):
    """Product Model."""

    size_float = fields.ChoiceFloatDynField(
        label=_("Size in float"),
    )
    sizes_float = fields.ChoiceFloatMultDynField(
        label=_("Sizes in float"),
    )
    size_int = fields.ChoiceIntDynField(
        label=_("Size in Int"),
    )
    sizes_int = fields.ChoiceIntMultDynField(
        label=_("Sizes in Int"),
    )
    size_txt = fields.ChoiceTextDynField(
        label=_("Size in Text"),
    )
    sizes_txt = fields.ChoiceTextMultDynField(
        label=_("Sizes in Text"),
    )


class TestDynamicChoicesExample(unittest.IsolatedAsyncioTestCase):
    """Testing the `dynamic_choices` example."""

    async def test_dynamic_choices_example(self):
        """Testing the `dynamic_choices` example."""
        # Maximum number of characters 60.
        database_name = "dynamic_choices_example"

        client = AsyncMongoClient(host=Config.MONGO_HOST)

        # Delete database before test.
        # (if the test fails)
        await client.drop_database(database_name)
        await client.close()
        #
        # ----------------------------------------------------------------------
        client = AsyncMongoClient(host=Config.MONGO_HOST)
        await Migration(
            database_name=database_name,
            mongo_client=client,
        ).migrate()

        # Add Units:
        # Hint: Enough once, then you can to comment or delete.
        for item in [
            {"title": {"en": "Big", "ru": "Большой"}, "value": 25.8},
            {"title": {"en": "Middle", "ru": "Средний"}, "value": 15.6},
            {"title": {"en": "Small", "ru": "Маленький"}, "value": 12.5},
        ]:
            unit = Unit(
                field="size_float",
                title=item["title"],
                value=item["value"],
            )
            await Product.unit_manager(unit)
            unit = Unit(
                field="sizes_float",
                title=item["title"],
                value=item["value"],
            )
            await Product.unit_manager(unit)

        for item in [
            {"title": {"en": "Big", "ru": "Большой"}, "value": 25},
            {"title": {"en": "Middle", "ru": "Средний"}, "value": 15},
            {"title": {"en": "Small", "ru": "Маленький"}, "value": 12},
        ]:
            unit = Unit(
                field="size_int",
                title=item["title"],
                value=item["value"],
            )
            await Product.unit_manager(unit)
            unit = Unit(
                field="sizes_int",
                title=item["title"],
                value=item["value"],
            )
            await Product.unit_manager(unit)

        for item in [
            {"title": {"en": "Big", "ru": "Большой"}, "value": "big"},
            {"title": {"en": "Middle", "ru": "Средний"}, "value": "middle"},
            {"title": {"en": "Small", "ru": "Маленький"}, "value": "small"},
        ]:
            unit = Unit(
                field="size_txt",
                title=item["title"],
                value=item["value"],
            )
            await Product.unit_manager(unit)
            unit = Unit(
                field="sizes_txt",
                title=item["title"],
                value=item["value"],
            )
            await Product.unit_manager(unit)

        product = Product("ru")
        product.size_float = 15.6
        product.sizes_float = [25.8, 12.5]
        product.size_int = 25
        product.sizes_int = [15, 12]
        product.size_txt = "middle"
        product.sizes_txt = ["big", "small"]

        # Create Product.
        is_saved = await product.save()
        if not is_saved:
            # Convenient to use during development.
            product.print_err()
        self.assertTrue(is_saved)

        product_details: dict | None = await Product.find_one_to_instance_model({"_id": product.id}, "ru")
        self.assertIsNotNone(product_details)
        self.assertEqual(product_details.size_float, 15.6)
        self.assertEqual(product_details.sizes_float, [25.8, 12.5])
        self.assertEqual(product_details.size_int, 25)
        self.assertEqual(product_details.sizes_int, [15, 12])
        self.assertEqual(product_details.size_txt, "middle")
        self.assertEqual(product_details.sizes_txt, ["big", "small"])

        # JSON
        unit_dict = Unit(
            field="choice_txt_mult_dyn",
            title={"en": "Title", "ru": "Заголовок"},
            value="Some text 2",
            is_delete=True,
        ).to_dict()
        self.assertTrue(isinstance(unit_dict, dict))
        self.assertEqual(unit_dict.get("field"), "choice_txt_mult_dyn")
        self.assertEqual(unit_dict.get("title"), {"en": "Title", "ru": "Заголовок"})
        self.assertEqual(unit_dict.get("value"), "Some text 2")
        #
        unit_json = Unit(
            field="choice_txt_mult_dyn",
            title={"en": "Title", "ru": "Заголовок"},
            value="Some text 2",
            is_delete=True,
        ).to_json()
        self.assertTrue(isinstance(unit_json, str))
        self.assertTrue(isinstance(unit_dict, dict))
        self.assertEqual(unit_dict.field, "choice_txt_mult_dyn")
        self.assertEqual(unit_dict.title, {"en": "Title", "ru": "Заголовок"})
        self.assertEqual(unit_dict.value, "Some text 2")
        # ----------------------------------------------------------------------
        #
        # Delete database after test.
        await client.drop_database(database_name)
        await client.close()


if __name__ == "__main__":
    unittest.main()
