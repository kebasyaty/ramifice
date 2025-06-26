"""App."""

import asyncio
import pprint
from datetime import datetime

from pymongo import AsyncMongoClient
from ramifice import migration

from models.accounts import User


async def main() -> None:
    """Main."""
    client: AsyncMongoClient = AsyncMongoClient()

    await migration.Monitor(
        database_name="test_db",
        mongo_client=client,
    ).migrat()

    # If you need to change the language of translation.
    # translations.change_locale("ru")

    user = User()
    user.username.value = "pythondev"
    user.first_name.value = "John"
    user.last_name.value = "Smith"
    user.email.value = "John_Smith@gmail.com"
    user.birthday.value = datetime(2000, 1, 25)
    user.password.value = "12345678"
    user.сonfirm_password.value = "12345678"

    # Create User.
    if not await user.save():
        # Convenient to use during development.
        user.print_err()

    # Update User.
    user.username.value = "pythondev-123"
    if not await user.save():
        # Convenient to use during development.
        user.print_err()

    print("User details:")
    user_details = await User.find_one_to_raw_doc({"_id": user.id.value})
    pprint.pprint(user_details)

    # Remove User.
    await user.delete()

    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
