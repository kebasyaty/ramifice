"""App."""

import asyncio
import pprint

from pymongo import AsyncMongoClient

from ramifice import MongoMigrationModels, translations

from .site import Parameters


async def main() -> None:
    """Main."""
    client: AsyncMongoClient = AsyncMongoClient()

    await MongoMigrationModels(
        database_name="test_fixtures",
        mongo_client=client,
    ).migrate()

    # If you need to change the language of translation.
    # Hint: For Ramifice by default = "en"
    translations.change_locale("en")

    params = await Parameters.find_one_to_instance({f"brand": "Brand Name"})

    if params is not None:
        print("Details of Parameters:")
        user_details = await Parameters.find_one_to_raw_doc({"_id": params.id.value})
        pprint.pprint(user_details)

        # await params.delete(remove_files=False)
    else:
        print("No parameters!")

    # Remove collection.
    # (if necessary)
    await Parameters.collection().drop()

    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
