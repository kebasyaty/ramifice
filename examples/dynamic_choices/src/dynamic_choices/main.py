"""App."""

import asyncio
import pprint

from models.goods import Product
from pymongo import AsyncMongoClient

from ramifice import Unit, migration, translations


async def main() -> None:
    """Main."""
    client: AsyncMongoClient = AsyncMongoClient()

    await migration.Monitor(
        database_name="test_dynamic_choices",
        mongo_client=client,
    ).migrate()

    # If you need to change the language of translation.
    # Hint: For Ramifice by default = "en"
    translations.change_locale("en")
    # Add Units:
    # Hint: Enough once, then you can to comment or delete.
    for item in [
        {"title": {"en": "Big"}, "value": 25.8},
        {"title": {"en": "Middle"}, "value": 15.6},
        {"title": {"en": "Small"}, "value": 12.5},
    ]:
        unit = Unit(
            field="size_float",
            title=item["title"]["en"],
            value=item["value"],
        )
        await Product.unit_manager(unit)
        unit = Unit(
            field="sizes_float",
            title=item["title"]["en"],
            value=item["value"],
        )
        await Product.unit_manager(unit)
    for item in [
        {"title": {"en": "Big"}, "value": 25},
        {"title": {"en": "Middle"}, "value": 15},
        {"title": {"en": "Small"}, "value": 12},
    ]:
        unit = Unit(
            field="size_int",
            title=item["title"]["en"],
            value=item["value"],
        )
        await Product.unit_manager(unit)
        unit = Unit(
            field="sizes_int",
            title=item["title"]["en"],
            value=item["value"],
        )
        await Product.unit_manager(unit)
    for item in [
        {"title": {"en": "Big"}, "value": "big"},
        {"title": {"en": "Middle"}, "value": "middle"},
        {"title": {"en": "Small"}, "value": "small"},
    ]:
        unit = Unit(
            field="size_txt",
            title=item["title"]["en"],
            value=item["value"],
        )
        await Product.unit_manager(unit)
        unit = Unit(
            field="sizes_txt",
            title=item["title"]["en"],
            value=item["value"],
        )
        await Product.unit_manager(unit)

    product = Product()
    product.size_float.value = 15.6
    product.sizes_float.value = [25.8, 12.5]
    product.size_int.value = 25
    product.sizes_int.value = [15, 12]
    product.size_txt.value = "middle"
    product.sizes_txt.value = ["big", "small"]

    # Create Product.
    if not await product.save():
        # Convenient to use during development.
        product.print_err()

    print("Products:")
    products = await Product.find_many_to_raw_doc()
    if products is not None:
        pprint.pprint(products)
    else:
        print("No Products!")

    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
