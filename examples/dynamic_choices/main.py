"""App."""

import asyncio
import pprint

from pymongo import AsyncMongoClient

from ramifice import Migration, Unit, translations

from .goods import Product


async def main() -> None:
    """Main."""
    client: AsyncMongoClient = AsyncMongoClient()

    await Migration(
        database_name="test_dynamic_choices",
        mongo_client=client,
    ).migrate()

    # If you need to change the language of translation.
    # Hint: For Ramifice by default = "en"
    translations.change_locale("en")

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
    products = await Product.find_many_to_raw_docs()
    if bool(products):
        pprint.pprint(products)
    else:
        print("No Products!")

    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
