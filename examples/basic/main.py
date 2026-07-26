"""App."""

import asyncio
import pprint
from datetime import date

from pymongo import AsyncMongoClient

from ramifice import Migration

from .models import User


async def main() -> None:
    """Main."""
    client: AsyncMongoClient = AsyncMongoClient()

    await Migration(
        database_name="test_basic",
        mongo_client=client,
    ).migrate()

    user = User()
    user.username = "pythondev"
    user.first_name = {"en": "John", "ru": "Джон"}  # multi_language=True
    # user.first_name = "John"
    user.last_name = {"en": "Smith", "ru": "Смит"}  # multi_language=True
    # user.last_name = "Smith"
    user.email = "John_Smith@gmail.com"
    user.phone = "+447986123456"
    user.birthday = date(2000, 1, 25)  # "25-01-2000" | "22 Décembre 2010" | "yaklaşık 23 saat önce" | "" == None
    user.description = {"en": "I program on Python!", "ru": "Я программирую на Python!"}  # multi_language=True
    # user.description = "I program on Python!"
    user.password = "12345678"
    user.сonfirm_password = "12345678"

    # Create User
    if not await user.save():
        # Convenient to use during development
        user.print_err()

    # Update User.
    user.username = "pythondev_123"
    if not await user.save():
        # Convenient to use during development
        user.print_err()

    print("User details:")
    user_details = await User.find_one_to_model_dict({"_id": user.id}, "ru")
    if user_details is not None:
        pprint.pprint(user_details)
    else:
        print("No User!")

    # Remove User
    # (if necessary)
    # await user.delete()

    # Remove collection
    # (if necessary)
    # await User.collection().drop()

    # Close connection
    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
