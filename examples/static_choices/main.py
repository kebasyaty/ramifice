"""App."""

import asyncio
import pprint

from pymongo import AsyncMongoClient
from ramifice import MigrationManager, translations

from .goods import Product


async def main() -> None:
    """Main."""
    client: AsyncMongoClient = AsyncMongoClient()

    await MigrationManager(
        database_name="test_static_choices",
        mongo_client=client,
    ).migrate()

    # If you need to change the language of translation.
    # Hint: For Ramifice by default = "en"
    translations.change_locale("en")

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

    print("Products:")
    products = await Product.find_many_to_raw_docs()
    if products is not None:
        pprint.pprint(products)
    else:
        print("No Products!")

    # Remove Product.
    # (if necessary)
    # if product_details is not None:
    #     await product.delete(remove_files=False)

    # Remove collection.
    # (if necessary)
    # await Product.collection().drop()

    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
