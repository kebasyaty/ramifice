"""Testing AddValidMixin, IndexMixin and HooksMixin."""

from __future__ import annotations

import re
import unittest

from ramifice import Model, NamedTuple, meta
from ramifice.fields import TextField


@meta(service_name="Accounts")
class User(Model):
    """Model for testing."""

    username = TextField(
        required=True,
    )


@meta(service_name="Accounts")
class User2(Model):
    """Model for testing."""

    username = TextField(
        required=True,
    )

    # Optional method
    async def add_validation(self) -> NamedTuple:
        """Additional validation of fields."""
        _ = self._CUSTOM_TRANSLATOR.gettext
        err_map = self.get_error_map()

        username = self.username

        # Check username
        if username is not None and re.match(r"^[a-zA-Z0-9_]+$", username) is None:
            err_map.update("username", _("Allowed chars: {}").format("a-z A-Z 0-9 _"))

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
        self.assertIsNone(await User2.indexing())

        m: User = User()
        err_map = await m.add_validation()
        self.assertTrue(isinstance(err_map, NamedTuple))
        self.assertEqual(len(err_map), 4)
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
        self.assertIsNone(err_map["username"])
        self.assertIsNone(await m2.pre_create())
        self.assertIsNone(await m2.post_create())
        self.assertIsNone(await m2.pre_update())
        self.assertIsNone(await m2.post_update())
        self.assertIsNone(await m2.pre_delete())
        self.assertIsNone(await m2.post_delete())


if __name__ == "__main__":
    unittest.main()
