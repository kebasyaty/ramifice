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
        database_name="test_fixtures",
        mongo_client=client,
    ).migrate()

    site_parameters: dict[str, Any] | None = await SiteParameters.find_one_to_model_dict({"brand": "Brand Name"})

    print("Details of Parameters:")
    if params is not None:
        pp(site_parameters)
    else:
        print("No parameters!")

    # Remove collection.
    # (if necessary)
    # await SiteParameters.collection.drop()

    # Close connection.
    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
