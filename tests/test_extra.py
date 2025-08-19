"""Testing AddValidMixin, IndexMixin and HooksMixin."""

from __future__ import annotations

import re
import unittest

from ramifice import NamedTuple, model, translations
from ramifice.fields import TextField


@model(service_name="Accounts")
class User:
    """Model for testing."""

    def fields(self):
        """Adding fields."""
        self.username = TextField(
            required=True,
        )


@model(service_name="Accounts")
class User2:
    """Model for testing."""

    def fields(self):
        """Adding fields."""
        self.username = TextField(
            required=True,
        )

    # Optional method
    async def add_validation(self) -> NamedTuple:
        """Additional validation of fields."""
        gettext = translations.gettext
        cd, err = self.get_clean_data()

        # Check username
        if re.match(r"^[a-zA-Z0-9_]+$", cd.username) is None:
            err.update("username", gettext("Allowed chars: %s") % "a-z A-Z 0-9 _")

        return err

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
        self.assertEqual(err_map.to_dict(), {})
        self.assertIsNone(await m.pre_create())
        self.assertIsNone(await m.post_create())
        self.assertIsNone(await m.pre_update())
        self.assertIsNone(await m.post_update())
        self.assertIsNone(await m.pre_delete())
        self.assertIsNone(await m.post_delete())

        m2 = User2()
        m2.username.value = "pythondev"
        err_map = await m2.add_validation()
        self.assertIsNone(err_map.username)
        self.assertIsNone(await m2.pre_create())
        self.assertIsNone(await m2.post_create())
        self.assertIsNone(await m2.pre_update())
        self.assertIsNone(await m2.post_update())
        self.assertIsNone(await m2.pre_delete())
        self.assertIsNone(await m2.post_delete())


if __name__ == "__main__":
    unittest.main()
