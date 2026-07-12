"""Testing selective float fields."""

from __future__ import annotations

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
        self.assertEqual(f.html_attrs["id"], "")
        self.assertEqual(f.html_attrs["label"], "")
        self.assertEqual(f.html_attrs["name"], "")
        self.assertEqual(f.html_attrs["field_type"], "ChoiceFloatField")
        self.assertFalse(f.html_attrs["disabled"])
        self.assertFalse(f.html_attrs["hide"])
        self.assertFalse(f.html_attrs["ignored"])
        self.assertIsNone(f.html_attrs["warning"])
        self.assertEqual(f.html_attrs["errors"], [])
        self.assertEqual(f.html_attrs["group"], "choice")
        self.assertIsNone(f.html_attrs["value"])
        self.assertIsNone(f.html_attrs["default"])
        self.assertEqual(f.html_attrs["placeholder"], "")
        self.assertEqual(f.html_attrs["hint"], "")
        self.assertFalse(f.html_attrs["required"])
        self.assertFalse(f.html_attrs["readonly"])
        self.assertFalse(f.html_attrs["unique"])
        self.assertFalse(f.html_attrs["multiple"])
        # Exception checking:
        with self.assertRaises(AssertionError):
            f = ChoiceFloatField(choices="not list")
        with self.assertRaises(AssertionError):
            f = ChoiceFloatField(default="2.0")
        with self.assertRaises(AssertionError):
            f = ChoiceFloatField(default=3.0, choices=[[1.0, "Title"], [2.0, "Title 2"]])
        # Methods:
        f = ChoiceFloatField()
        self.assertTrue(f.has_value())
        f = ChoiceFloatField(default=2.0, choices=[[1.0, "Title"], [2.0, "Title 2"]])
        self.assertTrue(f.has_value())
        f = ChoiceFloatField(choices=[[1.0, "Title"], [2.0, "Title 2"]])
        self.assertTrue(f.has_value())
        f.html_attrs["value"] = 2.0
        self.assertTrue(f.has_value())
        f.html_attrs["value"] = 3.0
        self.assertFalse(f.has_value())

    def test_choice_float_mult_field(self):
        """Testing `ChoiceFloatMultField`."""
        # Parameters by default:
        f = ChoiceFloatMultField()
        self.assertEqual(f.html_attrs["id"], "")
        self.assertEqual(f.html_attrs["label"], "")
        self.assertEqual(f.html_attrs["name"], "")
        self.assertEqual(f.html_attrs["field_type"], "ChoiceFloatMultField")
        self.assertFalse(f.html_attrs["disabled"])
        self.assertFalse(f.html_attrs["hide"])
        self.assertFalse(f.html_attrs["ignored"])
        self.assertIsNone(f.html_attrs["warning"])
        self.assertEqual(f.html_attrs["errors"], [])
        self.assertEqual(f.html_attrs["group"], "choice")
        self.assertIsNone(f.html_attrs["value"])
        self.assertIsNone(f.html_attrs["default"])
        self.assertEqual(f.html_attrs["placeholder"], "")
        self.assertEqual(f.html_attrs["hint"], "")
        self.assertFalse(f.html_attrs["required"])
        self.assertFalse(f.html_attrs["readonly"])
        self.assertFalse(f.html_attrs["unique"])
        self.assertTrue(f.html_attrs["multiple"])
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
            f = ChoiceFloatMultField(default=[3.0], choices=[[1.0, "Title"], [2.0, "Title 2"]])
        with self.assertRaises(AssertionError):
            f = ChoiceFloatMultField(default=[2.0, 3.0], choices=[[1.0, "Title"], [2.0, "Title 2"]])
        # Methods:
        f = ChoiceFloatMultField()
        self.assertTrue(f.has_value())
        f = ChoiceFloatMultField(default=[2.0], choices=[[1.0, "Title"], [2.0, "Title 2"]])
        self.assertTrue(f.has_value())
        f = ChoiceFloatMultField(choices=[[1.0, "Title"], [2.0, "Title 2"]])
        self.assertTrue(f.has_value())
        f.html_attrs["value"] = [2.0]
        self.assertTrue(f.has_value())
        f.html_attrs["value"] = [3.0]
        self.assertFalse(f.has_value())
        f.html_attrs["value"] = [2.0, 3.0]
        self.assertFalse(f.has_value())

    def test_choice_float_dyn_field(self):
        """Testing `ChoiceFloatDynField`."""
        # Parameters by default:
        f = ChoiceFloatDynField()
        self.assertEqual(f.html_attrs["id"], "")
        self.assertEqual(f.html_attrs["label"], "")
        self.assertEqual(f.html_attrs["name"], "")
        self.assertEqual(f.html_attrs["field_type"], "ChoiceFloatDynField")
        self.assertFalse(f.html_attrs["disabled"])
        self.assertFalse(f.html_attrs["hide"])
        self.assertFalse(f.html_attrs["ignored"])
        self.assertIsNone(f.html_attrs["warning"])
        self.assertEqual(f.html_attrs["errors"], [])
        self.assertEqual(f.html_attrs["group"], "choice")
        self.assertIsNone(f.html_attrs["value"])
        self.assertEqual(f.html_attrs["placeholder"], "")
        self.assertEqual(f.html_attrs["hint"], "")
        self.assertFalse(f.html_attrs["required"])
        self.assertFalse(f.html_attrs["readonly"])
        self.assertFalse(f.html_attrs["unique"])
        self.assertFalse(f.html_attrs["multiple"])

    def test_choice_float_mult_dyn_field(self):
        """Testing `ChoiceFloatMultDynField`."""
        # Parameters by default:
        f = ChoiceFloatMultDynField()
        self.assertEqual(f.html_attrs["id"], "")
        self.assertEqual(f.html_attrs["label"], "")
        self.assertEqual(f.html_attrs["name"], "")
        self.assertEqual(f.html_attrs["field_type"], "ChoiceFloatMultDynField")
        self.assertFalse(f.html_attrs["disabled"])
        self.assertFalse(f.html_attrs["hide"])
        self.assertFalse(f.html_attrs["ignored"])
        self.assertIsNone(f.html_attrs["warning"])
        self.assertEqual(f.html_attrs["errors"], [])
        self.assertEqual(f.html_attrs["group"], "choice")
        self.assertIsNone(f.html_attrs["value"])
        self.assertEqual(f.html_attrs["placeholder"], "")
        self.assertEqual(f.html_attrs["hint"], "")
        self.assertFalse(f.html_attrs["required"])
        self.assertFalse(f.html_attrs["readonly"])
        self.assertFalse(f.html_attrs["unique"])
        self.assertTrue(f.html_attrs["multiple"])


if __name__ == "__main__":
    unittest.main()
