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
        database_name="test_indexing",
        mongo_client=client,
    ).migrate()

    print("Index information:")
    pp(await User.index_information())

    # Create User
    user = User()
    user.username = "pythondev"
    user.avatar.from_path("public/media/default/no-photo.png")
    user.resume.from_path("public/media/default/no_doc.odt")
    user.first_name = "John"
    user.last_name = "Smith"
    user.email = "John_Smith@gmail.com"
    user.birthday = datetime(2000, 1, 25)
    user.password = "12345678"
    user.сonfirm_password = "12345678"
    user.is_admin = True

    # Save User
    if not await user.save():
        # Convenient to use during development
        user.print_err()

    print("\n\nUser details:")
    user_details = await User.find_one_to_model_dict({"_id": user.id})
    if user_details is not None:
        pp(user_details)
    else:
        print("No User!")

    # Remove User
    # await user.delete()
    # or
    deleted_user: dict[str, Any] = await user.delete()
    print("\n\nInformation about the user who was deleted:")
    pp(deleted_user)

    # Remove indexes
    print("\n\nRemove indexes:")
    await User.drop_index("username_Idx")
    await User.drop_index("email_Idx")
     # remove all indexes
    # await User.drop_indexes()
    #
    print("Index information:")
    pp(await User.index_information())

    # Remove collection
    # (if necessary)
    # await User.collection.drop()

    # Close connection.
    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
