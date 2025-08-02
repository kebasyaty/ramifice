"""App."""

import asyncio
import pprint
from datetime import datetime

from pymongo import AsyncMongoClient

from ramifice import Migration, translations

from .models import User


async def main() -> None:
    """Main."""
    client: AsyncMongoClient = AsyncMongoClient()

    await Migration(
        database_name="test_indexing",
        mongo_client=client,
    ).migrate()

    print("Index information:")
    pprint.pprint(await User.index_information())

    # If you need to change the language of translation.
    # Hint: For Ramifice by default = "en"
    translations.change_locale("en")

    user = User()
    user.username.value = "pythondev"
    user.avatar.from_path("public/media/default/no-photo.png")
    user.resume.from_path("public/media/default/no_doc.odt")
    user.first_name.value = "John"
    user.last_name.value = "Smith"
    user.email.value = "John_Smith@gmail.com"
    user.birthday.value = datetime(2000, 1, 25)
    user.password.value = "12345678"
    user.сonfirm_password.value = "12345678"
    user.is_admin.value = True

    # Create User.
    if not await user.save():
        # Convenient to use during development.
        user.print_err()

    # Update User.
    user.username.value = "pythondev-123"
    if not await user.save():
        user.print_err()

    print("\n\nUser details:")
    user_details = await User.find_one_to_raw_doc(
        # {"_id": user.id.value}
        {f"username": user.username.value}
    )
    if user_details is not None:
        pprint.pprint(user_details)
    else:
        print("No User!")

    # Remove User.
    if user_details is not None:
        await user.delete(remove_files=False)

    # Remove indexes:
    print("\n\nRemove indexes:")
    await User.drop_index("username_Idx")
    await User.drop_index("email_Idx")
    # await User.drop_indexes()  # remove all indexes.
    print("Index information:")
    pprint.pprint(await User.index_information())

    # Remove collection.
    # (if necessary)
    await User.collection().drop()

    # Close connection.
    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
