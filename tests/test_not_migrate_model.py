"""Testing the module `ramifice.decorators.model (is_migrate_model=False)`."""

import unittest

from ramifice import model
from ramifice.fields import ChoiceTextField, TextField
from ramifice.model import Model


@model(
    service_name="Accounts",
    is_migrate_model=False,
)
class User:
    """Model for testing."""

    def fields(self):
        """For adding fields."""
        self.username = TextField()
        self.favorite_color = ChoiceTextField()


@model(
    service_name="Profiles",
    is_migrate_model=False,
)
class UserProfile:
    """Model for testing."""

    def fields(self):
        """For adding fields."""
        self.profession = TextField()


class TestPseudoModel(unittest.TestCase):
    """Testing the module `ramifice.decorators.model (is_migrate_model=False)`."""

    def setUp(self):
        """Set date for testing."""
        self.user_meta = {
            "collection_name": "Accounts_User",
            "count_all_fields": 3,
            "count_fields_no_ignored": 0,
            "data_dynamic_fields": {},
            "db_query_docs_limit": 1000,
            "field_attrs": {
                "_id": {"id": "User--id", "name": "_id"},
                "favorite_color": {
                    "id": "User--favorite-color",
                    "name": "favorite_color",
                },
                "username": {"id": "User--username", "name": "username"},
            },
            "field_name_and_type": {
                "_id": "IDField",
                "favorite_color": "ChoiceTextField",
                "username": "TextField",
            },
            "fixture_name": None,
            "full_model_name": "tests.test_not_migrate_model.User",
            "is_create_doc": False,
            "is_delete_doc": False,
            "is_migrate_model": False,
            "is_update_doc": False,
            "model_name": "User",
            "service_name": "Accounts",
        }
        self.user_profile_meta = {
            "collection_name": "Profiles_UserProfile",
            "count_all_fields": 2,
            "count_fields_no_ignored": 0,
            "data_dynamic_fields": {},
            "db_query_docs_limit": 1000,
            "field_attrs": {
                "_id": {"id": "UserProfile--id", "name": "_id"},
                "profession": {"id": "UserProfile--profession", "name": "profession"},
            },
            "field_name_and_type": {
                "_id": "IDField",
                "profession": "TextField",
            },
            "fixture_name": None,
            "full_model_name": "tests.test_not_migrate_model.UserProfile",
            "is_create_doc": False,
            "is_delete_doc": False,
            "is_migrate_model": False,
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
        self.assertEqual(User.__module__, "tests.test_not_migrate_model")

    def test_instance_user(self):
        """Testing a instance `User`."""
        m = User()

        self.assertEqual(m.model_name(), "User")
        self.assertEqual(m.full_model_name(), "tests.test_not_migrate_model.User")

        self.assertIsNone(m._id.value)
        self.assertIsNone(m.__dict__.get("created_at"))
        self.assertIsNone(m.__dict__.get("updated_at"))
        self.assertIsNone(m.username.value)
        self.assertIsNone(m.favorite_color.value)
        self.assertEqual(m.username.id, "User--username")
        self.assertEqual(m.username.name, "username")

    def test_class_user_profile(self):
        """Testing a class `UserProfile`."""
        self.assertEqual(Model.META, {})
        self.assertEqual(UserProfile.META, self.user_profile_meta)
        self.assertEqual(UserProfile.__name__, "UserProfile")
        self.assertEqual(UserProfile.__module__, "tests.test_not_migrate_model")

    def test_instance_user_profile(self):
        """Testing a instance `UserProfile`."""
        m = UserProfile()

        self.assertEqual(m.model_name(), "UserProfile")
        self.assertEqual(m.full_model_name(), "tests.test_not_migrate_model.UserProfile")

        self.assertIsNone(m._id.value)
        self.assertIsNone(m.__dict__.get("created_at"))
        self.assertIsNone(m.__dict__.get("updated_at"))
        self.assertIsNone(m.profession.value)
        self.assertEqual(m.profession.id, "UserProfile--profession")
        self.assertEqual(m.profession.name, "profession")


if __name__ == "__main__":
    unittest.main()
