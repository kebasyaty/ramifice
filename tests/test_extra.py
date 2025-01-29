"""Testing the module `ramifice.model + ramifice.extra`."""

import unittest

from ramifice import Model
from ramifice.fields import TextField


class User(Model):
    """For testing a `Extra`."""

    def __init__(self, *args, **kwargs):
        self.username = TextField()
        #
        super().__init__(*args, **kwargs)


class User2(Model):
    """For testing a `Extra`."""

    def __init__(self, *args, **kwargs):
        self.username = TextField()
        #
        super().__init__(*args, **kwargs)

    def add_validation(self) -> dict[str, str]:
        """It is supposed to be use to additional validation of fields.
        Format: <"field_name", "Error message">
        """
        error_map: dict[str, str] = {}
        return error_map

    @classmethod
    def indexing(cls) -> None:
        """For set up and start indexing."""

    def pre_create(self) -> None:
        """Called before a new document is created in the database."""

    def post_create(self) -> None:
        """Called after a new document has been created in the database."""

    def pre_update(self) -> None:
        """Called before updating an existing document in the database."""

    def post_update(self) -> None:
        """Called after an existing document in the database is updated."""

    def pre_delete(self) -> None:
        """Called before deleting an existing document in the database."""

    def post_delete(self) -> None:
        """Called after an existing document in the database has been deleted."""


class TestModel(unittest.TestCase):
    """Testing the module `ramifice.model + ramifice.extra`."""

    def test_extra_methods(self):
        """Testing a `Model` and extra methods."""
        self.assertIsNone(User.indexing())
        self.assertIsNone(User2.indexing())
        #
        m = User()
        self.assertEqual(m.add_validation(), {})
        self.assertIsNone(m.pre_create())
        self.assertIsNone(m.post_create())
        self.assertIsNone(m.pre_update())
        self.assertIsNone(m.post_update())
        self.assertIsNone(m.pre_delete())
        self.assertIsNone(m.post_delete())
        #
        m2 = User2()
        self.assertEqual(m2.add_validation(), {})
        self.assertIsNone(m2.pre_create())
        self.assertIsNone(m2.post_create())
        self.assertIsNone(m2.pre_update())
        self.assertIsNone(m2.post_update())
        self.assertIsNone(m2.pre_delete())
        self.assertIsNone(m2.post_delete())
