"""Testing the `files` example."""

from __future__ import annotations

import unittest

from pymongo import AsyncMongoClient

from ramifice import (
    Migration,
    Model,
    Translator,
    fields,
    meta,
    to_human_size,
)
from ramifice.config import Config

_ = Translator.STUB_TRANSLATOR_FOR_ATTRIBUTES_OF_FIELD


@meta(service_name="Accounts")
class User(Model):
    """User Model."""

    avatar = fields.ImageField(
        label=_("Avatar"),
        default="public/media/default/no-photo.png",
        # Available 4 sizes from lg to xs or None.
        # Hint: By default = None
        thumbnails={"lg": 512, "md": 256, "sm": 128, "xs": 64},
        # The maximum size of the original image in bytes.
        # Hint: By default = 2 MB
        max_size=524288,  # 0.5 MB = 524288 Bytes (in binary)
        warning=[
            _("Maximum size: {}").format(to_human_size(524288)),
        ],
    )
    resume = fields.FileField(
        label=_("Resume"),
        default="public/media/default/no_doc.odt",
    )


class TestFilesExample(unittest.IsolatedAsyncioTestCase):
    """Testing the `files` example."""

    async def test_files_example(self):
        """Testing the `files` example."""
        # Maximum number of characters 60.
        database_name = "files_example"

        client = AsyncMongoClient(host=Config.MONGO_HOST)

        # Delete database before test.
        # (if the test fails)
        await client.drop_database(database_name)
        await client.close()
        #
        # ----------------------------------------------------------------------
        client = AsyncMongoClient(host=Config.MONGO_HOST)
        await Migration(
            database_name=database_name,
            mongo_client=client,
        ).migrate()

        # Create User
        # Use defaule values
        user = User()
        is_saved = await user.save()
        if not is_saved:
            user.print_err()
        self.assertTrue(is_saved)

        user_details: User | None = await User.find_one_to_instance_model({"_id": user.id})
        self.assertIsNotNone(user_details)
        self.assertTrue(isinstance(user_details, User))
        self.assertTrue(isinstance(user_details.avatar, dict))
        self.assertEqual(user_details.avatar, {})
        self.assertTrue(isinstance(user_details.resume, dict))
        self.assertEqual(user_details.resume, {})

        # Create User
        # Use custom files
        user2 = User()
        user2.avatar__core.from_path("public/media/default/no-photo.png")
        user2.resume__core.from_path("public/media/default/no_doc.odt")
        is_saved = await user2.save()
        if not is_saved:
            user2.print_err()
        self.assertTrue(is_saved)
        # ----------------------------------------------------------------------
        #
        # Delete database after test.
        await client.drop_database(database_name)
        await client.close()


if __name__ == "__main__":
    unittest.main()
