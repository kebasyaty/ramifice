"""App."""

import asyncio
from datetime import datetime

from pymongo import AsyncMongoClient

from ramifice import Migration, translations

from .models import User


async def main() -> None:
    """Main."""
    client: AsyncMongoClient = AsyncMongoClient()

    await Migration(
        database_name="test_password",
        mongo_client=client,
    ).migrate()

    # If you need to change the language of translation.
    # Hint: For Ramifice by default = "en"
    translations.change_locale("en")

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

    if not await user.save():
        # Convenient to use during development.
        user.print_err()

    # Verification of password.
    if await user.verify_password(password="12345678"):
        print("12345678 - The password is valid")

    # Replacement of password.
    print("Replacement of password from `12345678` to `O2eA4GIr38KGGlS`")
    await user.update_password(
        old_password="12345678",
        new_password="O2eA4GIr38KGGlS",
    )

    # Verification of new password.
    if await user.verify_password(password="O2eA4GIr38KGGlS"):
        print("O2eA4GIr38KGGlS - The password is valid")

    await user.delete(remove_files=False)

    # Remove collection.
    # (if necessary)
    await User.collection().drop()

    # Close connection.
    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
