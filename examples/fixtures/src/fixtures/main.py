"""App."""

import asyncio
import pprint

from pymongo import AsyncMongoClient
from ramifice import migration, translations

from models.accounts import User


async def main() -> None:
    """Main."""
    client: AsyncMongoClient = AsyncMongoClient()

    await migration.Monitor(
        database_name="test_db",
        mongo_client=client,
    ).migrat()

    # If you need to change the language of translation.
    translations.change_locale("en")

    user = await User.find_one_to_instance({"email": "John_Smith@gmail.com"})

    print("User details:")
    user_details = await User.find_one_to_raw_doc({"_id": user.id.value})
    pprint.pprint(user_details)

    if user is not None:
        await user.delete(remove_files=False)

    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
