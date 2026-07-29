"""Testing the `static_choices` example."""

from __future__ import annotations

import unittest

from pymongo import AsyncMongoClient

from ramifice import (
    Migration,
    Model,
    Translator,
    fields,
    meta,
)
from ramifice.config import Config

_ = Translator.STUB_TRANSLATOR_FOR_ATTRIBUTES_OF_FIELD


@meta(service_name="Goods")
class Product(Model):
    """Product Model."""

    size_float = fields.ChoiceFloatField(
        label=_("Size in float"),
        choices=[
            [25.8, _("Big")],
            [15.6, _("Middle")],
            [12.5, _("Small")],
        ],
    )
    sizes_float = fields.ChoiceFloatMultField(
        label=_("Sizes in float"),
        choices=[
            [25.8, _("Big")],
            [15.6, _("Middle")],
            [12.5, _("Small")],
        ],
    )
    size_int = fields.ChoiceIntField(
        label=_("Size in Int"),
        choices=[
            [25, _("Big")],
            [15, _("Middle")],
            [12, _("Small")],
        ],
    )
    sizes_int = fields.ChoiceIntMultField(
        label=_("Sizes in Int"),
        choices=[
            [25, _("Big")],
            [15, _("Middle")],
            [12, _("Small")],
        ],
    )
    size_txt = fields.ChoiceTextField(
        label=_("Size in Text"),
        choices=[
            ["big", _("Big")],
            ["middle", _("Middle")],
            ["small", _("Small")],
        ],
    )
    sizes_txt = fields.ChoiceTextMultField(
        label=_("Sizes in Text"),
        choices=[
            ["big", _("Big")],
            ["middle", _("Middle")],
            ["small", _("Small")],
        ],
    )


class TestStaticChoicesExample(unittest.IsolatedAsyncioTestCase):
    """Testing the `static_choices` example."""

    async def test_static_choices_example(self):
        """Testing the `static_choices` example."""
        # Maximum number of characters 60.
        database_name = "static_choices_example"

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

        # Update Product
        product.size_txt = "big"
        if not await product.save():
            product.print_err()

        product_details: dict | None = await Product.find_one_to_instance_model({"_id": product.id}, "ru")
        self.assertIsNotNone(product_details)
        self.assertEqual(product_details.size_float, 15.6)
        self.assertEqual(product_details.sizes_float, [25.8, 12.5])
        self.assertEqual(product_details.size_int, 25)
        self.assertEqual(product_details.sizes_int, [15, 12])
        self.assertEqual(product_details.size_txt, "big")
        self.assertEqual(product_details.sizes_txt, ["big", "small"])
        # ----------------------------------------------------------------------
        #
        # Delete database after test.
        await client.drop_database(database_name)
        await client.close()


if __name__ == "__main__":
    unittest.main()
