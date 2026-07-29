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
        self.assertTrue(isinstance(user_details.resume, dict))

        # Create User
        # Use custom files
        user2 = User()
        await user2.avatar__core.from_path("public/media/default/no-photo.png")
        await user2.resume__core.from_path("public/media/default/no_doc.odt")
        is_saved = await user2.save()
        if not is_saved:
            user2.print_err()
        self.assertTrue(is_saved)

        user2_details: User | None = await User.find_one_to_instance_model({"_id": user2.id})
        self.assertIsNotNone(user2_details)
        self.assertTrue(isinstance(user2_details, User))
        self.assertTrue(isinstance(user2_details.avatar, dict))
        self.assertTrue(isinstance(user2_details.resume, dict))

        await user.delete()
        self.assertIsNone(user.id)
        self.assertIsNone(user.created_at)
        self.assertIsNone(user.updated_at)
        self.assertIsNone(user.avatar)
        self.assertIsNone(user.resume)

        await user2.delete(remove_files=False)
        self.assertIsNone(user2.id)
        self.assertIsNone(user2.created_at)
        self.assertIsNone(user2.updated_at)
        self.assertIsNone(user2.avatar)
        self.assertIsNone(user2.resume)
        # ----------------------------------------------------------------------
        #
        # Delete database after test.
        await client.drop_database(database_name)
        await client.close()


if __name__ == "__main__":
    unittest.main()
