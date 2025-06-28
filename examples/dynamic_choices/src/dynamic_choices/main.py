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
        database_name="test_db",
        mongo_client=client,
    ).migrate()

    # If you need to change the language of translation.
    # Hint: For Ramifice by default = "en"
    translations.change_locale("en")

    # Add Units:
    for title, value in {"Big": 25.8, "Middle": 15.6, "Small": 12.5}.items():
        unit = Unit(
            field="size_float",
            title=title,
            value=value,
        )
        await Product.unit_manager(unit)
        unit = Unit(
            field="sizes_float",
            title=title,
            value=value,
        )
        await Product.unit_manager(unit)
    for title, value in {"Big": 25, "Middle": 15, "Small": 12}.items():
        unit = Unit(
            field="size_int",
            title=title,
            value=value,
        )
        await Product.unit_manager(unit)
        unit = Unit(
            field="sizes_int",
            title=title,
            value=value,
        )
        await Product.unit_manager(unit)
    for title, value in {"Big": "big", "Middle": "middle", "Small": "small"}.items():
        unit = Unit(
            field="size_txt",
            title=title,
            value=value,
        )
        await Product.unit_manager(unit)
        unit = Unit(
            field="sizes_txt",
            title=title,
            value=value,
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

    # Update Product.
    product.size_txt.value = "big"
    if not await product.save():
        product.print_err()

    print("Product details:")
    product_details = await Product.find_one_to_raw_doc({"_id": product.id.value})
    if product_details is not None:
        pprint.pprint(product_details)
    else:
        print("No Product!")

    # Remove Product.
    if product_details is not None:
        await product.delete(remove_files=False)

    # Remove collection.
    # (if necessary)
    await Product.collection().drop()

    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
