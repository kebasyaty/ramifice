"""App."""

import asyncio
from pprint import pprint as pp

from typing import Any

from pymongo import AsyncMongoClient

from ramifice import Migration

from .models import SiteParameters


async def main() -> None:
    """Main."""
    client: AsyncMongoClient = AsyncMongoClient()

    await Migration(
        database_name="test_multi_fixture",
        mongo_client=client,
    ).migrate()

    count: int = await SiteParameters.estimated_document_count()
    print(count)  # 2

    site_parameters: dict[str, Any] | None = await SiteParameters.find_one_to_model_dict({"brand": "Brand Name"})
    print("Details of Parameters:")
    if params is not None:
        pp(site_parameters)
    else:
        print("No parameters!")

    site_parameters_2: dict[str, Any] | None = await SiteParameters.find_one_to_model_dict({"brand": "Brand Name 2"})
    print("Details of Parameters 2:")
    if params is not None:
        pp(site_parameters_2)
    else:
        print("No parameters 2!")

    # Remove collection.
    # (if necessary)
    # await SiteParameters.collection.drop()

    # Close connection.
    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
