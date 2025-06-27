"""App."""

import asyncio
import pprint
from datetime import datetime

from pymongo import AsyncMongoClient
from ramifice import migration, translations

from models.goods import Product


async def main() -> None:
    """Main."""
    client: AsyncMongoClient = AsyncMongoClient()

    await migration.Monitor(
        database_name="test_db",
        mongo_client=client,
    ).migrat()

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
