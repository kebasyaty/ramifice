"""Testing the module `ramifice.meta`."""

import unittest

from ramifice import Model, meta
from ramifice.fields import ChoiceTextDynField, TextField


@meta(service_name="Accounts")
class User(Model):
    """Class for testing."""

    def __init__(self):
        self.username = TextField()
        self.favorite_color = ChoiceTextDynField()
        #
        super().__init__()

    def __str__(self):
        return str(self.username.value)


@meta(service_name="Profiles")
class UserProfile(Model):
    """Class for testing."""

    def __init__(self):
        self.profession = TextField()
        #
        super().__init__()

    def __str__(self):
        return str(self.profession.value)


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
            "full_model_name": "tests.test_meta.User",
            "collection_name": "Accounts_User",
            "field_name_and_type_list": {
                "username": "TextField",
                "favorite_color": "ChoiceTextDynField",
                "created_at": "DateTimeField",
                "updated_at": "DateTimeField",
            },
            "field_name_params_list": {
                "username": {"type": "TextField", "group": "text"},
                "favorite_color": {"type": "ChoiceTextDynField", "group": "choice"},
                "created_at": {"type": "DateTimeField", "group": "date"},
                "updated_at": {"type": "DateTimeField", "group": "date"},
            },
            "field_attrs": {
                "username": {"id": "User--username", "name": "username"},
                "favorite_color": {
                    "id": "User--favorite-color",
                    "name": "favorite_color",
                },
                "_id": {"id": "User---id", "name": "_id"},
                "created_at": {"id": "User--created-at", "name": "created_at"},
                "updated_at": {"id": "User--updated-at", "name": "updated_at"},
            },
            "data_dynamic_fields": {},
            "count_all_fields": 5,
            "count_fields_for_migrating": 4,
        }
        self.user_profile_meta = {
            "service_name": "Profiles",
            "fixture_name": None,
            "db_query_docs_limit": 1000,
            "is_migrat_model": True,
            "is_create_doc": True,
            "is_update_doc": True,
            "is_delete_doc": True,
            "model_name": "UserProfile",
            "full_model_name": "tests.test_meta.UserProfile",
            "collection_name": "Profiles_UserProfile",
            "field_name_and_type_list": {
                "profession": "TextField",
                "created_at": "DateTimeField",
                "updated_at": "DateTimeField",
            },
            "field_name_params_list": {
                "profession": {"type": "TextField", "group": "text"},
                "created_at": {"type": "DateTimeField", "group": "date"},
                "updated_at": {"type": "DateTimeField", "group": "date"},
            },
            "field_attrs": {
                "profession": {"id": "UserProfile--profession", "name": "profession"},
                "_id": {"id": "UserProfile---id", "name": "_id"},
                "created_at": {"id": "UserProfile--created-at", "name": "created_at"},
                "updated_at": {"id": "UserProfile--updated-at", "name": "updated_at"},
            },
            "data_dynamic_fields": {},
            "count_all_fields": 4,
            "count_fields_for_migrating": 3,
        }
        return super().setUp()

    def test_class_user(self):
        """Testing a class `User`."""
        self.assertFalse(bool(Model.META))
        self.assertEqual(User.META, self.user_meta)
        self.assertEqual(User.__name__, "User")
        self.assertEqual(User.__module__, "tests.test_meta")

    def test_instance_user(self):
        """Testing a instance `User`."""
        m = User()
        #
        self.assertEqual(str(m), "None")
        #
        self.assertEqual(m.model_name(), "User")
        self.assertEqual(m.full_model_name(), "tests.test_meta.User")
        #
        self.assertIsNone(m._id.value)
        self.assertIsNone(m.created_at.value)
        self.assertIsNone(m.updated_at.value)
        self.assertIsNone(m.username.value)
        self.assertIsNone(m.favorite_color.value)
        self.assertEqual(m.username.id, "User--username")
        self.assertEqual(m.username.name, "username")

    def test_class_user_profile(self):
        """Testing a class `UserProfile`."""
        self.assertFalse(bool(Model.META))
        self.assertEqual(UserProfile.META, self.user_profile_meta)
        self.assertEqual(UserProfile.__name__, "UserProfile")
        self.assertEqual(UserProfile.__module__, "tests.test_meta")

    def test_instance_user_profile(self):
        """Testing a instance `UserProfile`."""
        m = UserProfile()
        #
        self.assertEqual(str(m), "None")
        #
        self.assertEqual(m.model_name(), "UserProfile")
        self.assertEqual(m.full_model_name(), "tests.test_meta.UserProfile")
        #
        self.assertIsNone(m._id.value)
        self.assertIsNone(m.created_at.value)
        self.assertIsNone(m.updated_at.value)
        self.assertIsNone(m.profession.value)
        self.assertEqual(m.profession.id, "UserProfile--profession")
        self.assertEqual(m.profession.name, "profession")


if __name__ == "__main__":
    unittest.main()
