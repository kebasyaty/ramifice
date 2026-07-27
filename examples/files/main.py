"""App."""

import asyncio
from pprint import pprint as pp

from pymongo import AsyncMongoClient

from ramifice import Migration

from .models import User


async def main() -> None:
    """Main."""
    client: AsyncMongoClient = AsyncMongoClient()

    await Migration(
        database_name="test_files",
        mongo_client=client,
    ).migrate()

    user = User()
    await user.avatar__core.from_path("public/media/default/no-photo.png")
    await user.resume__core.from_path("public/media/default/no_doc.odt")

    if not await user.save():
        # Convenient to use during development.
        user.print_err()

    print("User details:")
    user_details = await User.find_one_to_model_dict({"_id": user.id})
    if user_details is not None:
        pp(user_details)
    else:
        print("No User!")

    await user.delete(remove_files=False)

    # Remove collection.
    # (if necessary)
    # await User.collection().drop()

    # Close connection.
    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
