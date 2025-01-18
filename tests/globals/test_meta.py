"""Testing the module `ramifice.meta`."""

import unittest

from ramifice import Meta, Model
from ramifice.fields import DateTimeField, HashField, TextField


@Meta(service_name="Accounts")
class User(Model):
    """Class for testing."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__username = TextField()

    @property
    def username(self):
        """Username"""
        return self.__username


class TestModel(unittest.TestCase):
    """Testing the module `ramifice.meta`."""

    def setUp(self):
        self.model_params = {
            "service_name": "Accounts",
            "fixture_name": None,
            "db_query_docs_limit": 1000,
            "is_migrat_model": True,
            "is_create_doc": True,
            "is_update_doc": True,
            "is_delete_doc": True,
            "model_name": "User",
            "full_model_name": "test_meta__User",
            "collection_name": "Accounts_User",
            "field_name_and_type_list": {
                "created_at": "DateTimeField",
                "updated_at": "DateTimeField",
                "username": "TextField",
            },
            "field_name_params_list": {
                "created_at": {"type": "DateTimeField", "group": "date"},
                "updated_at": {"type": "DateTimeField", "group": "date"},
                "username": {"type": "TextField", "group": "text"},
            },
        }
        return super().setUp()

    def test_class_user(self):
        """Testing a class `User`."""
        self.assertIsNone(Model.META)
        self.assertEqual(User.META, self.model_params)
        self.assertEqual(User.__name__, "User")
        self.assertEqual(User.__module__, "test_meta")

    def test_instance_user(self):
        """Testing a instance `User`."""
        m = User()
        #
        self.assertEqual(m.model_name(), "User")
        self.assertEqual(m.full_model_name(), "test_meta__User")
        #
        self.assertIsNone(m.hash.value)
        self.assertIsNone(m.created_at.value)
        self.assertIsNone(m.updated_at.value)
        self.assertIsNone(m.username.value)
        self.assertIsNone(m.object_id())
        #
        with self.assertRaises(AttributeError):
            m.hash = HashField()
        with self.assertRaises(AttributeError):
            m.created_at = DateTimeField()
        with self.assertRaises(AttributeError):
            m.updated_at = DateTimeField()
        with self.assertRaises(AttributeError):
            m.username = TextField()
