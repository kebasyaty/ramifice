"""Testing AddValidMixin, IndexMixin and HooksMixin."""

from __future__ import annotations

import re
import unittest
from typing import Any

from ramifice import Translations, model
from ramifice.fields import TextField

Translations.init_params()


@model(service_name="Accounts")
class User:
    """Model for testing."""

    username = TextField(
        required=True,
    )


@model(service_name="Accounts")
class User2:
    """Model for testing."""

    username = TextField(
        required=True,
    )

    # Optional method
    async def add_validation(self) -> dict[str, Any]:
        """Additional validation of fields."""
        err_map = self.get_error_map()
        username = self.username

        # Check username
        if username is not None and re.match(r"^[a-zA-Z0-9_]+$", username) is None:
            err_map["username"] = Translations.gettext("Allowed chars: {}").format("a-z A-Z 0-9 _")

        return err_map

    @classmethod
    async def indexing(cls) -> None:
        """For set up and start indexing."""

    async def pre_create(self) -> None:
        """Called before a new document is created in the database."""

    async def post_create(self) -> None:
        """Called after a new document has been created in the database."""

    async def pre_update(self) -> None:
        """Called before updating an existing document in the database."""

    async def post_update(self) -> None:
        """Called after an existing document in the database is updated."""

    async def pre_delete(self) -> None:
        """Called before deleting an existing document in the database."""

    async def post_delete(self) -> None:
        """Called after an existing document in the database has been deleted."""


class TestExtra(unittest.IsolatedAsyncioTestCase):
    """Testing AddValidMixin, IndexMixin and HooksMixin."""

    async def test_extra_methods(self):
        """Testing a `Model` and extra methods."""
        self.assertIsNone(await User.indexing())
        self.assertIsNone(await User2.indexing())

        m: User = User()
        err_map = await m.add_validation()
        self.assertEqual(err_map, {})
        self.assertIsNone(await m.pre_create())
        self.assertIsNone(await m.post_create())
        self.assertIsNone(await m.pre_update())
        self.assertIsNone(await m.post_update())
        self.assertIsNone(await m.pre_delete())
        self.assertIsNone(await m.post_delete())

        m2 = User2()
        m2.username = "pythondev"
        err_map = await m2.add_validation()
        self.assertIsNone(err_map["id"])
        self.assertIsNone(err_map["created_at"])
        self.assertIsNone(err_map["updated_at"])
        self.assertEqual(err_map["username"], "pythondev")
        self.assertIsNone(await m2.pre_create())
        self.assertIsNone(await m2.post_create())
        self.assertIsNone(await m2.pre_update())
        self.assertIsNone(await m2.post_update())
        self.assertIsNone(await m2.pre_delete())
        self.assertIsNone(await m2.post_delete())


if __name__ == "__main__":
    unittest.main()
