"""App."""

import asyncio
import pprint
from datetime import datetime

from pymongo import AsyncMongoClient

from ramifice import Migration, translations

from .accounts import User


async def main() -> None:
    """Main."""
    client: AsyncMongoClient = AsyncMongoClient()

    await Migration(
        database_name="test_basic",
        mongo_client=client,
    ).migrate()

    # If you need to change the language of translation.
    # Hint: For Ramifice by default = "en"
    translations.change_locale("en")

    user = User()
    # user.avatar.from_path("public/media/default/no-photo.png")
    user.username.value = "pythondev"
    user.first_name.value = {"en": "John", "ru": "Джон"}
    # user.first_name.value = "John"
    user.last_name.value = {"en": "Smith", "ru": "Смит"}
    # user.last_name.value = "Smith"
    user.email.value = "John_Smith@gmail.com"
    user.phone.value = "+447986123456"
    user.birthday.value = datetime(2000, 1, 25)
    user.description.value = {"en": "I program on Python!", "ru": "Я программирую на Python!"}
    # user.description.value = "I program on Python!"
    user.password.value = "12345678"
    user.сonfirm_password.value = "12345678"

    # Create User.
    if not await user.save():
        # Convenient to use during development.
        user.print_err()

    # Update User.
    user.username.value = "pythondev_123"
    if not await user.save():
        # Convenient to use during development.
        user.print_err()

    print("User details:")
    user_details = await User.find_one_to_raw_doc({"_id": user.id.value})
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

    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
