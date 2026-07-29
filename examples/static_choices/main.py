"""App."""

import asyncio
from pprint import pprint as pp

from pymongo import AsyncMongoClient

from ramifice import Migration
from .models import Product


async def main() -> None:
    """Main."""
    client: AsyncMongoClient = AsyncMongoClient()

    await Migration(
        database_name="test_static_choices",
        mongo_client=client,
    ).migrate()

    # Create Product
    product = Product()
    product.size_float = 15.6
    product.sizes_float = [25.8, 12.5]
    product.size_int = 25
    product.sizes_int = [15, 12]
    product.size_txt = "middle"
    product.sizes_txt = ["big", "small"]

    # Save Product
    if not await product.save():
        # Convenient to use during development
        product.print_err()

    # Update Product
    product.size_txt = "big"
    if not await product.save():
        product.print_err()

    print("Products:")
    products = await Product.find_many_to_model_dict()
    if products is not None:
        pp(products)
    else:
        print("No Products!")

    # Remove collection
    # (if necessary)
    # await Product.collection.drop()

    # Close connection.
    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
