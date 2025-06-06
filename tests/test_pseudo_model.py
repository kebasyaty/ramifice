"""Testing the module `ramifice.decor_model (is_migrat_model=False)`."""

import pprint
import unittest

from src.ramifice import model
from src.ramifice.fields import ChoiceTextDynField, TextField
from src.ramifice.model import Model


@model(
    service_name="Accounts",
    is_migrat_model=False,
)
class User:
    """Model for testing."""

    def fields(self, gettext):
        self.username = TextField()
        self.favorite_color = ChoiceTextDynField()


@model(
    service_name="Profiles",
    is_migrat_model=False,
)
class UserProfile:
    """Model for testing."""

    def fields(self, gettext):
        self.profession = TextField()


class TestPseudoModel(unittest.TestCase):
    """Testing the module `ramifice.decor_model (is_migrat_model=False)`."""

    def setUp(self):
        self.user_meta = {
            "collection_name": "Accounts_User",
            "count_all_fields": 5,
            "count_fields_for_migrating": 5,
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
            "fixture_name": None,
            "full_model_name": "tests.test_pseudo_model.User",
            "is_create_doc": False,
            "is_delete_doc": False,
            "is_migrat_model": False,
            "is_update_doc": False,
            "model_name": "User",
            "service_name": "Accounts",
        }
        self.user_profile_meta = {
            "collection_name": "Profiles_UserProfile",
            "count_all_fields": 4,
            "count_fields_for_migrating": 4,
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
            "fixture_name": None,
            "full_model_name": "tests.test_pseudo_model.UserProfile",
            "is_create_doc": False,
            "is_delete_doc": False,
            "is_migrat_model": False,
            "is_update_doc": False,
            "model_name": "UserProfile",
            "service_name": "Profiles",
        }
        return super().setUp()

    def test_class_user(self):
        """Testing a class `User`."""
        self.assertEqual(Model.META, {})
        self.assertEqual(User.META, self.user_meta)
        self.assertEqual(User.__name__, "User")
        self.assertEqual(User.__module__, "tests.test_pseudo_model")

    def test_instance_user(self):
        """Testing a instance `User`."""
        m = User()

        self.assertEqual(m.model_name(), "User")
        self.assertEqual(m.full_model_name(), "tests.test_pseudo_model.User")

        self.assertIsNone(m._id.value)
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
        self.assertEqual(UserProfile.__module__, "tests.test_pseudo_model")

    def test_instance_user_profile(self):
        """Testing a instance `UserProfile`."""
        m = UserProfile()

        self.assertEqual(m.model_name(), "UserProfile")
        self.assertEqual(m.full_model_name(), "tests.test_pseudo_model.UserProfile")

        self.assertIsNone(m._id.value)
        self.assertIsNone(m.created_at.value)
        self.assertIsNone(m.updated_at.value)
        self.assertIsNone(m.profession.value)
        self.assertEqual(m.profession.id, "UserProfile--profession")
        self.assertEqual(m.profession.name, "profession")


if __name__ == "__main__":
    unittest.main()
