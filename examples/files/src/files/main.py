"""App."""

import asyncio
import pprint

from models.accounts import User
from pymongo import AsyncMongoClient

from ramifice import migration, translations


async def main() -> None:
    """Main."""
    client: AsyncMongoClient = AsyncMongoClient()

    await migration.Monitor(
        database_name="test_files",
        mongo_client=client,
    ).migrate()

    # If you need to change the language of translation.
    # Hint: For Ramifice by default = "en"
    translations.change_locale("en")

    user = User()
    user.avatar.from_path("public/media/default/no-photo.png")
    user.resume.from_path("public/media/default/no_doc.odt")

    if not await user.save():
        # Convenient to use during development.
        user.print_err()

    print("User details:")
    user_details = await User.find_one_to_raw_doc({"_id": user.id.value})
    pprint.pprint(user_details)

    await user.delete(remove_files=False)

    # Remove collection.
    # (if necessary)
    await User.collection().drop()

    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
