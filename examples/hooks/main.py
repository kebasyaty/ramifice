"""App."""

import asyncio
from pprint import pprint as pp
from typing import Any

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

    # Create User
    user = User()
    user.username = "pythondev"
    user.email = "John_Smith@gmail.com"

    # Save User
    if not await user.save():
        # Convenient to use during development
        user.print_err()

    # Update User
    user.username = "pythondev-123"
    if not await user.save():
        # Convenient to use during development
        user.print_err()

    # Remove User
    deleted_user: dict[str, Any] = await user.delete()
    pp(deleted_user)

    # Remove collection
    # (if necessary)
    # await User.collection.drop()

    # Close connection
    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
