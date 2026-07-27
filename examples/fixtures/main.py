"""App."""

import asyncio
from pprint import pprint as pp

from pymongo import AsyncMongoClient

from ramifice import Migration, translations

from .models import SiteParameters


async def main() -> None:
    """Main."""
    client: AsyncMongoClient = AsyncMongoClient()

    await Migration(
        database_name="test_fixtures",
        mongo_client=client,
    ).migrate()

    # If you need to change the language of translation.
    # Hint: For Ramifice by default = "en"
    Translations.change_locale("en")

    params = await SiteParameters.find_one_to_instance_model({f"brand": "Brand Name"})

    if params is not None:
        print("Details of Parameters:")
        site_parameters = await SiteParameters.find_one_to_model_dict({"_id": params.id})
        pp(site_parameters)
    else:
        print("No parameters!")

    # Remove collection.
    # (if necessary)
    # await SiteParameters.collection().drop()

    # Close connection.
    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
