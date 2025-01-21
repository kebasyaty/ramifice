"""Testing selective float fields."""

import unittest

from ramifice.fields import (
    ChoiceFloatDynField,
    ChoiceFloatField,
    ChoiceFloatMultDynField,
    ChoiceFloatMultField,
)


class TestChoiceFloatFields(unittest.TestCase):
    """Testing selective float fields."""

    def test_choice_float_field(self):
        """Testing `ChoiceFloatField`."""
        # Parameters by default:
        f = ChoiceFloatField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, "ChoiceFloatField")
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, "choice")
        self.assertIsNone(f.value)
        self.assertIsNone(f.default)
        self.assertEqual(f.placeholder, "")
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertFalse(f.unique)
        self.assertFalse(f.multiple)
        # Exception checking:
        with self.assertRaises(AssertionError):
            f = ChoiceFloatField(choices="not list")
        with self.assertRaises(AssertionError):
            f = ChoiceFloatField(default="2.0")
        with self.assertRaises(AssertionError):
            f = ChoiceFloatField(
                default=3.0, choices=[(1.0, "Title"), (2.0, "Title 2")]
            )
        # Methods:
        f = ChoiceFloatField()
        json_str = '{"id": "", "label": "", "name": "", "field_type": "ChoiceFloatField", "disabled": false, "hide": false, "ignored": false, "hint": "", "warning": null, "errors": null, "group": "choice", "placeholder": "", "required": false, "readonly": false, "unique": false, "multiple": false, "value": null, "default": null, "choices": null}'
        self.assertEqual(f.to_json(), json_str)
        self.assertTrue(f.has_value())
        f = ChoiceFloatField(default=2.0, choices=[(1.0, "Title"), (2.0, "Title 2")])
        self.assertTrue(f.has_value())
        f = ChoiceFloatField(choices=[(1.0, "Title"), (2.0, "Title 2")])
        self.assertTrue(f.has_value())
        f.value = 2.0
        self.assertTrue(f.has_value())
        f.value = 3.0
        self.assertFalse(f.has_value())

    def test_choice_float_mult_field(self):
        """Testing `ChoiceFloatMultField`."""
        # Parameters by default:
        f = ChoiceFloatMultField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, "ChoiceFloatMultField")
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, "choice")
        self.assertIsNone(f.value)
        self.assertIsNone(f.default)
        self.assertEqual(f.placeholder, "")
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertFalse(f.unique)
        self.assertTrue(f.multiple)
        # Exception checking:
        with self.assertRaises(AssertionError):
            f = ChoiceFloatMultField(choices="not list")
        with self.assertRaises(AssertionError):
            f = ChoiceFloatMultField(choices=[])
        with self.assertRaises(AssertionError):
            f = ChoiceFloatMultField(default="not list")
        with self.assertRaises(AssertionError):
            f = ChoiceFloatMultField(default=[])
        with self.assertRaises(AssertionError):
            f = ChoiceFloatMultField(
                default=[3.0], choices=[(1.0, "Title"), (2.0, "Title 2")]
            )
        with self.assertRaises(AssertionError):
            f = ChoiceFloatMultField(
                default=[2.0, 3.0], choices=[(1.0, "Title"), (2.0, "Title 2")]
            )
        # Methods:
        f = ChoiceFloatMultField()
        json_str = '{"id": "", "label": "", "name": "", "field_type": "ChoiceFloatMultField", "disabled": false, "hide": false, "ignored": false, "hint": "", "warning": null, "errors": null, "group": "choice", "placeholder": "", "required": false, "readonly": false, "unique": false, "multiple": true, "value": null, "default": null, "choices": null}'
        self.assertEqual(f.to_json(), json_str)
        self.assertTrue(f.has_value())
        f = ChoiceFloatMultField(
            default=[2.0], choices=[(1.0, "Title"), (2.0, "Title 2")]
        )
        self.assertTrue(f.has_value())
        f = ChoiceFloatMultField(choices=[(1.0, "Title"), (2.0, "Title 2")])
        self.assertTrue(f.has_value())
        f.value = [2.0]
        self.assertTrue(f.has_value())
        f.value = [3.0]
        self.assertFalse(f.has_value())
        f.value = [2.0, 3.0]
        self.assertFalse(f.has_value())

    def test_choice_float_dyn_field(self):
        """Testing `ChoiceFloatDynField`."""
        # Parameters by default:
        f = ChoiceFloatDynField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, "ChoiceFloatDynField")
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, "choice")
        self.assertIsNone(f.value)
        self.assertEqual(f.placeholder, "")
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertFalse(f.unique)
        self.assertFalse(f.multiple)
        # Methods:
        json_str = '{"id": "", "label": "", "name": "", "field_type": "ChoiceFloatDynField", "disabled": false, "hide": false, "ignored": false, "hint": "", "warning": null, "errors": null, "group": "choice", "placeholder": "", "required": false, "readonly": false, "unique": false, "multiple": false, "value": null, "choices": null}'
        self.assertEqual(f.to_json(), json_str)

    def test_choice_float_mult_dyn_field(self):
        """Testing `ChoiceFloatMultDynField`."""
        # Parameters by default:
        f = ChoiceFloatMultDynField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, "ChoiceFloatMultDynField")
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, "choice")
        self.assertIsNone(f.value)
        self.assertEqual(f.placeholder, "")
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertFalse(f.unique)
        self.assertTrue(f.multiple)
        # Methods:
        json_str = '{"id": "", "label": "", "name": "", "field_type": "ChoiceFloatMultDynField", "disabled": false, "hide": false, "ignored": false, "hint": "", "warning": null, "errors": null, "group": "choice", "placeholder": "", "required": false, "readonly": false, "unique": false, "multiple": true, "value": null, "choices": null}'
        self.assertEqual(f.to_json(), json_str)


if __name__ == "__main__":
    unittest.main()
