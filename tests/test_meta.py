"""Testing the module `ramifice.decorators`."""

from __future__ import annotations

import re
import unittest

from ramifice import Model, meta
from ramifice.fields import ChoiceTextDynField, TextField


@meta(service_name="Accounts")
class User(Model):
    """Model for testing."""

    username = TextField()
    favorite_color = ChoiceTextDynField()


@meta(service_name="Profiles")
class UserProfile(Model):
    """Model for testing."""

    profession = TextField(multi_language=True)


class TestModel(unittest.TestCase):
    """Testing the module `ramifice.decorators`."""

    def setUp(self):
        """Set data for testing."""
        self.user_meta = {
            "service_name": "Accounts",
            "fixture_name": None,
            "db_query_docs_limit": 1000,
            "is_create_doc": True,
            "is_update_doc": True,
            "is_delete_doc": True,
            "model_name": "User",
            "full_model_name": "test_decorator.User",
            "collection_name": "Accounts_User",
            "all_descriptor_fields": ["id", "created_at", "updated_at", "username", "favorite_color"],
            "field_name_and_type": {"username": "TextField", "favorite_color": "ChoiceTextDynField"},
            "data_dynamic_fields": {"favorite_color": None},
            "regex_mongo_filter": re.compile(r'(?P<field>"(?:)":)'),
        }
        self.user_profile_meta = {
            "service_name": "Profiles",
            "fixture_name": None,
            "db_query_docs_limit": 1000,
            "is_create_doc": True,
            "is_update_doc": True,
            "is_delete_doc": True,
            "model_name": "UserProfile",
            "full_model_name": "test_decorator.UserProfile",
            "collection_name": "Profiles_UserProfile",
            "all_descriptor_fields": ["id", "created_at", "updated_at", "profession"],
            "field_name_and_type": {"profession": "TextField"},
            "data_dynamic_fields": {},
            "regex_mongo_filter": re.compile(r'(?P<field>"(?:)":)'),
        }
        return super().setUp()

    def test_class_user(self):
        """Testing a class `User`."""
        self.assertEqual(Model.META, {})
        self.assertEqual(User.META, self.user_meta)

    def test_instance_user(self):
        """Testing a instance `User`."""
        m = User()

        self.assertEqual(m.username_html_attrs["id"], "id-username")
        self.assertEqual(m.username_html_attrs["name"], "username")

        self.assertEqual(m.model_name(), "User")
        self.assertEqual(m.full_model_name(), "test_decorator.User")

        self.assertIsNone(m.id)
        self.assertIsNone(m.created_at)
        self.assertIsNone(m.updated_at)
        self.assertIsNone(m.username)
        self.assertIsNone(m.favorite_color)

    def test_class_user_profile(self):
        """Testing a class `UserProfile`."""
        self.assertEqual(Model.META, {})
        self.assertEqual(UserProfile.META, self.user_profile_meta)

    def test_instance_user_profile(self):
        """Testing a instance `UserProfile`."""
        m = UserProfile()

        self.assertEqual(m.model_name(), "UserProfile")
        self.assertEqual(m.full_model_name(), "test_decorator.UserProfile")

        self.assertEqual(m.profession_html_attrs["id"], "id-profession")
        self.assertEqual(m.profession_html_attrs["name"], "profession")

        self.assertIsNone(m.id)
        self.assertIsNone(m.created_at)
        self.assertIsNone(m.updated_at)
        self.assertIsNone(m.profession)


if __name__ == "__main__":
    unittest.main()
