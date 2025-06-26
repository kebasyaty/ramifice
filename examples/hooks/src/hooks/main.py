"""App."""

import asyncio

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
    # Hint: For Ramifice by default = "en"
    # translations.change_locale("ru")

    user = User()
    user.username.value = "pythondev"
    user.email.value = "John_Smith@gmail.com"

    # Create User
    if not await user.save():
        # Convenient to use during development.
        user.print_err()

    # Update User.
    user.username.value = "pythondev-123"
    if not await user.save():
        # Convenient to use during development.
        user.print_err()

    # Remove User.
    await user.delete()

    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
