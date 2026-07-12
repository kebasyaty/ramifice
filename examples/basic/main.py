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
        database_name="test_basic",
        mongo_client=client,
    ).migrate()

    # If you need to change the language of translation.
    # Hint: For Ramifice by default = "en"
    Translations.change_locale("en")

    user = User()
    # user.avatar.from_path("public/media/default/no-photo.png")
    user.username = "pythondev"
    user.first_name = {"en": "John", "ru": "Джон"}
    # user.first_name = "John"
    user.last_name = {"en": "Smith", "ru": "Смит"}
    # user.last_name = "Smith"
    user.email = "John_Smith@gmail.com"
    user.phone = "+447986123456"
    user.birthday = datetime(2000, 1, 25)
    user.description = {"en": "I program on Python!", "ru": "Я программирую на Python!"}
    # user.description = "I program on Python!"
    user.password = "12345678"
    user.сonfirm_password = "12345678"

    # Create User.
    if not await user.save():
        # Convenient to use during development.
        user.print_err()

    # Update User.
    user.username = "pythondev_123"
    if not await user.save():
        # Convenient to use during development.
        user.print_err()

    print("User details:")
    user_details = await User.find_one_to_raw_doc({"_id": user.id})
    if user_details is not None:
        pprint.pprint(user_details)
    else:
        print("No User!")

    # Remove User.
    # (if necessary)
    # await user.delete()

    # Remove collection.
    # (if necessary)
    # await User.collection().drop()

    # Close connection.
    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
