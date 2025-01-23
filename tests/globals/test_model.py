"""Testing the module `ramifice.model`."""

import unittest

from ramifice import Model
from ramifice.fields import DateTimeField, HashField, TextField


class User(Model):
    """For testing a instance `Model`."""

    def __init__(self, *args, **kwargs):
        self.__username = TextField()
        #
        super().__init__(*args, **kwargs)

    @property
    def username(self):
        """Username"""
        return self.__username


class TestModel(unittest.TestCase):
    """Testing the module `ramifice.model`."""

    def test_class_model(self):
        """Testing a class `Model`."""
        self.assertFalse(bool(Model.META))
        self.assertEqual(Model.__name__, "Model")
        self.assertEqual(Model.__module__, "ramifice.model")
        self.assertIsNotNone(Model.__dict__.get("model_name"))
        self.assertIsNotNone(Model.__dict__.get("full_model_name"))

    def test_instance_model(self):
        """Testing a instance `Model`."""
        m = User()
        #
        self.assertEqual(m.model_name(), "User")
        self.assertEqual(m.full_model_name(), "test_model__User")
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
        # Methods:
        json_str = '{"username": {"id": "", "label": "", "name": "", "field_type": "TextField", "disabled": false, "hide": false, "ignored": false, "hint": "", "warning": null, "errors": null, "group": "text", "input_type": "text", "value": null, "placeholder": "", "required": false, "readonly": false, "unique": false, "default": null, "textarea": false, "use_editor": false, "maxlength": 256}, "hash": {"id": "", "label": "Document ID", "name": "", "field_type": "HashField", "disabled": true, "hide": true, "ignored": true, "hint": "", "warning": null, "errors": null, "group": "hash", "input_type": "text", "value": null, "placeholder": "", "required": false, "readonly": false, "unique": false}, "created_at": {"id": "", "label": "Created at", "name": "", "field_type": "DateTimeField", "disabled": true, "hide": true, "ignored": false, "hint": "", "warning": ["When the document was created."], "errors": null, "group": "date", "input_type": "datetime", "value": null, "placeholder": "", "required": false, "readonly": false, "unique": false, "max_date": null, "min_date": null, "default": null}, "updated_at": {"id": "", "label": "Updated at", "name": "", "field_type": "DateTimeField", "disabled": true, "hide": true, "ignored": false, "hint": "", "warning": ["When the document was updated."], "errors": null, "group": "date", "input_type": "datetime", "value": null, "placeholder": "", "required": false, "readonly": false, "unique": false, "max_date": null, "min_date": null, "default": null}}'
        self.assertEqual(m.to_json(), json_str)
        json_str = (
            '{"username": null, "hash": null, "created_at": null, "updated_at": null}'
        )
        self.assertEqual(m.to_json_only_value(), json_str)
