"""Testing the module `ramifice.meta`."""

import unittest

from ramifice import Model, meta
from ramifice.fields import DateTimeField, HashField, TextField


@meta(service_name="Accounts")
class User(Model):
    """Class for testing."""

    def __init__(self):
        self.__username = TextField()
        #
        super().__init__()

    @property
    def username(self) -> TextField:
        """Username"""
        return self.__username


@meta(service_name="Profiles")
class UserProfile(Model):
    """Class for testing."""

    def __init__(self):
        self.profession = TextField()
        #
        super().__init__()


class TestModel(unittest.TestCase):
    """Testing the module `ramifice.meta`."""

    def setUp(self):
        self.user_meta = {
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
            "field_attrs": {
                "hash": {"id": "User--hash", "name": "hash"},
                "created_at": {"id": "User--created-at", "name": "created_at"},
                "updated_at": {"id": "User--updated-at", "name": "updated_at"},
                "username": {"id": "User--username", "name": "username"},
            },
            "data_dynamic_fields": {},
            "count_all_fields": 4,
            "count_fields_for_migrating": 3,
            "time_object_list": {
                "created_at": {"default": None, "max_date": None, "min_date": None},
                "updated_at": {"default": None, "max_date": None, "min_date": None},
            },
        }
        return super().setUp()

    def test_class_user(self):
        """Testing a class `User`."""
        self.assertFalse(bool(Model.META))
        self.assertEqual(User.META, self.user_meta)
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
        self.assertEqual(m.username.id, "User--username")
        self.assertEqual(m.username.name, "username")
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

    def test_instance_user_profile(self):
        """Testing a instance `UserProfile`."""
        m = UserProfile()
        #
        self.assertEqual(m.model_name(), "UserProfile")
        self.assertEqual(m.full_model_name(), "test_meta__UserProfile")
        #
        self.assertIsNone(m.hash.value)
        self.assertIsNone(m.created_at.value)
        self.assertIsNone(m.updated_at.value)
        self.assertIsNone(m.profession.value)
        self.assertEqual(m.profession.id, "UserProfile--profession")
        self.assertEqual(m.profession.name, "profession")
        self.assertIsNone(m.object_id())
