"""App."""

import asyncio
import pprint

from models.site import Parameters
from pymongo import AsyncMongoClient

from ramifice import migration, translations


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

    params = await Parameters.find_one_to_instance(
        {f"brand.{translations.CURRENT_LOCALE}": "Brand Name"}
    )

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
