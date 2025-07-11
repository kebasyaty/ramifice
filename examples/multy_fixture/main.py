"""App."""

import asyncio
import pprint

from pymongo import AsyncMongoClient

from ramifice import Migration, translations

from .site import Parameters


async def main() -> None:
    """Main."""
    client: AsyncMongoClient = AsyncMongoClient()

    await Migration(
        database_name="test_multy_fixture",
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

    params_2 = await Parameters.find_one_to_instance({f"brand": "Brand Name 2"})
    if params_2 is not None:
        print("\nDetails of Parameters:")
        user_details_2 = await Parameters.find_one_to_raw_doc({"_id": params_2.id.value})
        pprint.pprint(user_details_2)
        # await params_2.delete(remove_files=False)
    else:
        print("No parameters 2!")

    # Remove collection.
    # (if necessary)
    await Parameters.collection().drop()

    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
