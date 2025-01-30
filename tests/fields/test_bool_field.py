"""Testing boolean field."""

import unittest

from ramifice.fields import BooleanField


class TestBooleanField(unittest.TestCase):
    """Testing boolean field"""

    def test_boolean_field(self):
        """Testing `BooleanField`."""
        # Parameters by default:
        f = BooleanField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, "BooleanField")
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, "bool")
        self.assertEqual(f.input_type, "checkbox")
        self.assertIsNone(f.value)
        self.assertFalse(f.default)
        # Exception checking:
        with self.assertRaises(AssertionError):
            BooleanField(default=0)
        with self.assertRaises(AssertionError):
            BooleanField(default="False")
        BooleanField(default=True)
        # Methods:
        json_str = '{"id": "", "label": "", "name": "", "field_type": "BooleanField", "disabled": false, "hide": false, "ignored": false, "hint": "", "warning": null, "errors": null, "group": "bool", "input_type": "checkbox", "value": null, "default": false}'
        self.assertEqual(f.to_json(), json_str)


if __name__ == "__main__":
    unittest.main()
