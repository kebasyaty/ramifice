"""Testing the module `ramifice.decorators`."""

from __future__ import annotations

import re
import unittest

from ramifice import model
from ramifice.fields import ChoiceTextDynField, TextField
from ramifice.models.model import Model


@model(service_name="Accounts")
class User:
    """Model for testing."""

    username = TextField()
    favorite_color = ChoiceTextDynField()


@model(service_name="Profiles")
class UserProfile:
    """Model for testing."""

    profession = TextField()


class TestModel(unittest.TestCase):
    """Testing the module `ramifice.decorators`."""

    def setUp(self):
        """Set data for testing."""
        self.user_meta = {
            "collection_name": "Accounts_User",
            "all_descriptor_fields": ["username", "favorite_color"],
            "data_dynamic_fields": {"favorite_color": None},
            "db_query_docs_limit": 1000,
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
            "all_descriptor_fields": ["profession"],
            "data_dynamic_fields": {},
            "db_query_docs_limit": 1000,
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

        self.assertIsNone(m.id)
        self.assertIsNone(m.created_at)
        self.assertIsNone(m.updated_at)
        self.assertIsNone(m.username)
        self.assertIsNone(m.favorite_color)
        self.assertEqual(m.username_html_attrs["id"], "id-username")
        self.assertEqual(m.username_html_attrs["name"], "username")

    def test_class_user_profile(self):
        """Testing a class `UserProfile`."""
        self.assertEqual(Model.META, {})
        self.assertEqual(UserProfile.META, self.user_profile_meta)

    def test_instance_user_profile(self):
        """Testing a instance `UserProfile`."""
        m = UserProfile()

        self.assertEqual(m.model_name(), "UserProfile")
        self.assertEqual(m.full_model_name(), "test_decorators.UserProfile")

        self.assertIsNone(m.id)
        self.assertIsNone(m.created_at)
        self.assertIsNone(m.updated_at)
        self.assertIsNone(m.profession)
        self.assertEqual(m.profession_html_attrs["id"], "id-profession")
        self.assertEqual(m.profession_html_attrs["name"], "profession")


if __name__ == "__main__":
    unittest.main()
