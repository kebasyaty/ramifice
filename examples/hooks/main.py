"""App."""

import asyncio

from pymongo import AsyncMongoClient

from ramifice import Migration

from .models import User


async def main() -> None:
    """Main."""
    client: AsyncMongoClient = AsyncMongoClient()

    await Migration(
        database_name="test_hooks",
        mongo_client=client,
    ).migrate()

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

    # Remove collection.
    # (if necessary)
    await User.collection().drop()

    # Close connection.
    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
