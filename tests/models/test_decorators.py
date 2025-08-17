"""Testing the module `ramifice.decorators`."""

import re
import unittest

from ramifice import model
from ramifice.fields import ChoiceTextDynField, TextField
from ramifice.models.model import Model


@model(service_name="Accounts")
class User:
    """Model for testing."""

    def fields(self):
        """Adding fields."""
        self.username = TextField()
        self.favorite_color = ChoiceTextDynField()


@model(service_name="Profiles")
class UserProfile:
    """Model for testing."""

    def fields(self):
        """Adding fields."""
        self.profession = TextField()


class TestModel(unittest.TestCase):
    """Testing the module `ramifice.decorators`."""

    def setUp(self):
        """Set data for testing."""
        self.user_meta = {
            "collection_name": "Accounts_User",
            "count_all_fields": 5,
            "count_fields_no_ignored": 5,
            "data_dynamic_fields": {"favorite_color": None},
            "db_query_docs_limit": 1000,
            "field_attrs": {
                "_id": {"id": "User--id", "name": "_id"},
                "created_at": {"id": "User--created-at", "name": "created_at"},
                "favorite_color": {
                    "id": "User--favorite-color",
                    "name": "favorite_color",
                },
                "updated_at": {"id": "User--updated-at", "name": "updated_at"},
                "username": {"id": "User--username", "name": "username"},
            },
            "field_name_and_type": {
                "_id": "IDField",
                "created_at": "DateTimeField",
                "favorite_color": "ChoiceTextDynField",
                "updated_at": "DateTimeField",
                "username": "TextField",
            },
            "regex_mongo_filter": re.compile(r'(?P<field>"(?:)":)'),
            "fixture_name": None,
            "full_model_name": "test_decorators.User",
            "is_create_doc": True,
            "is_delete_doc": True,
            "is_update_doc": True,
            "model_name": "User",
            "service_name": "Accounts",
        }
        self.user_profile_meta = {
            "collection_name": "Profiles_UserProfile",
            "count_all_fields": 4,
            "count_fields_no_ignored": 4,
            "data_dynamic_fields": {},
            "db_query_docs_limit": 1000,
            "field_attrs": {
                "_id": {"id": "UserProfile--id", "name": "_id"},
                "created_at": {"id": "UserProfile--created-at", "name": "created_at"},
                "profession": {"id": "UserProfile--profession", "name": "profession"},
                "updated_at": {"id": "UserProfile--updated-at", "name": "updated_at"},
            },
            "field_name_and_type": {
                "_id": "IDField",
                "created_at": "DateTimeField",
                "profession": "TextField",
                "updated_at": "DateTimeField",
            },
            "regex_mongo_filter": re.compile(r'(?P<field>"(?:)":)'),
            "fixture_name": None,
            "full_model_name": "test_decorators.UserProfile",
            "is_create_doc": True,
            "is_delete_doc": True,
            "is_update_doc": True,
            "model_name": "UserProfile",
            "service_name": "Profiles",
        }
        return super().setUp()

    def test_class_user(self):
        """Testing a class `User`."""
        self.assertEqual(Model.META, {})
        self.assertEqual(User.META, self.user_meta)
        self.assertEqual(User.__name__, "User")
        self.assertEqual(User.__module__, "test_decorators")

    def test_instance_user(self):
        """Testing a instance `User`."""
        m = User()

        self.assertEqual(m.model_name(), "User")
        self.assertEqual(m.full_model_name(), "test_decorators.User")

        self.assertIsNone(m.id.value)
        self.assertIsNone(m.created_at.value)
        self.assertIsNone(m.updated_at.value)
        self.assertIsNone(m.username.value)
        self.assertIsNone(m.favorite_color.value)
        self.assertEqual(m.username.id, "User--username")
        self.assertEqual(m.username.name, "username")

    def test_class_user_profile(self):
        """Testing a class `UserProfile`."""
        self.assertEqual(Model.META, {})
        self.assertEqual(UserProfile.META, self.user_profile_meta)
        self.assertEqual(UserProfile.__name__, "UserProfile")
        self.assertEqual(UserProfile.__module__, "test_decorators")

    def test_instance_user_profile(self):
        """Testing a instance `UserProfile`."""
        m = UserProfile()

        self.assertEqual(m.model_name(), "UserProfile")
        self.assertEqual(m.full_model_name(), "test_decorators.UserProfile")

        self.assertIsNone(m.id.value)
        self.assertIsNone(m.created_at.value)
        self.assertIsNone(m.updated_at.value)
        self.assertIsNone(m.profession.value)
        self.assertEqual(m.profession.id, "UserProfile--profession")
        self.assertEqual(m.profession.name, "profession")


if __name__ == "__main__":
    unittest.main()
