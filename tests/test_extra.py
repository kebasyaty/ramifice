"""Testing AddValidMixin, IndexMixin and HooksMixin."""

import collections
import re
import unittest

from ramifice import model
from ramifice.fields import TextField
from ramifice.utils import translations


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

    async def add_validation(self) -> dict[str, str]:
        """It is supposed to be use to additional validation of fields.

        Format: <"field_name", "Error message">
        """
        gettext = translations.gettext
        cd, err_map = self.get_clean_data()

        if re.match(r"^[a-zA-Z0-9_]+$", cd["username"]) is None:
            err_map["username"] = gettext("Allowed chars: %s") % "a-z A-Z 0-9 _"

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
        self.assertEqual(await m.add_validation(), {})
        self.assertIsNone(await m.pre_create())
        self.assertIsNone(await m.post_create())
        self.assertIsNone(await m.pre_update())
        self.assertIsNone(await m.post_update())
        self.assertIsNone(await m.pre_delete())
        self.assertIsNone(await m.post_delete())

        m2 = User2()
        m2.username.value = "pythondev"
        err_map = await m2.add_validation()
        self.assertIsNone(err_map.get("username"))
        self.assertIsNone(await m2.pre_create())
        self.assertIsNone(await m2.post_create())
        self.assertIsNone(await m2.pre_update())
        self.assertIsNone(await m2.post_update())
        self.assertIsNone(await m2.pre_delete())
        self.assertIsNone(await m2.post_delete())


if __name__ == "__main__":
    unittest.main()
