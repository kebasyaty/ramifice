"""Testing selective integer fields."""

from __future__ import annotations

import unittest

from ramifice.fields import (
    ChoiceIntDynField,
    ChoiceIntField,
    ChoiceIntMultDynField,
    ChoiceIntMultField,
)


class TestChoiceIntegerFields(unittest.TestCase):
    """Testing selective integer fields."""

    def test_choice_int_field(self):
        """Testing `ChoiceIntField`."""
        # Parameters by default:
        f = ChoiceIntField()
        self.assertEqual(f.html_attrs["id"], "")
        self.assertEqual(f.html_attrs["label"], "")
        self.assertEqual(f.html_attrs["name"], "")
        self.assertEqual(f.html_attrs["field_type"], "ChoiceIntField")
        self.assertFalse(f.html_attrs["disabled"])
        self.assertFalse(f.html_attrs["hide"])
        self.assertFalse(f.html_attrs["ignored"])
        self.assertEqual(len(f.html_attrs["warning"]), 0)
        self.assertEqual(f.html_attrs["errors"], [])
        self.assertEqual(f.html_attrs["group"], "choice")
        self.assertIsNone(f.html_attrs["value"])
        self.assertIsNone(f.html_attrs["default"])
        self.assertEqual(f.html_attrs["hint"], "")
        self.assertFalse(f.html_attrs["required"])
        self.assertFalse(f.html_attrs["readonly"])
        self.assertFalse(f.html_attrs["unique"])
        self.assertFalse(f.html_attrs["multiple"])
        # Exception checking:
        with self.assertRaises(AssertionError):
            f = ChoiceIntField(choices="not list")
        with self.assertRaises(AssertionError):
            f = ChoiceIntField(default="2")
        with self.assertRaises(AssertionError):
            f = ChoiceIntField(default=3, choices=[[1, "Title"], [2, "Title 2"]])
        # Methods:
        f = ChoiceIntField()
        self.assertTrue(f.has_value())
        f = ChoiceIntField(default=2, choices=[[1, "Title"], [2, "Title 2"]])
        self.assertTrue(f.has_value())
        f = ChoiceIntField(choices=[[1, "Title"], [2, "Title 2"]])
        self.assertTrue(f.has_value())
        f.html_attrs["value"] = 2
        self.assertTrue(f.has_value())
        f.html_attrs["value"] = 3
        self.assertFalse(f.has_value())

    def test_choice_int_mult_field(self):
        """Testing `ChoiceIntMultField`."""
        # Parameters by default:
        f = ChoiceIntMultField()
        self.assertEqual(f.html_attrs["id"], "")
        self.assertEqual(f.html_attrs["label"], "")
        self.assertEqual(f.html_attrs["name"], "")
        self.assertEqual(f.html_attrs["field_type"], "ChoiceIntMultField")
        self.assertFalse(f.html_attrs["disabled"])
        self.assertFalse(f.html_attrs["hide"])
        self.assertFalse(f.html_attrs["ignored"])
        self.assertEqual(len(f.html_attrs["warning"]), 0)
        self.assertEqual(f.html_attrs["errors"], [])
        self.assertEqual(f.html_attrs["group"], "choice")
        self.assertIsNone(f.html_attrs["value"])
        self.assertIsNone(f.html_attrs["default"])
        self.assertEqual(f.html_attrs["hint"], "")
        self.assertFalse(f.html_attrs["required"])
        self.assertFalse(f.html_attrs["readonly"])
        self.assertFalse(f.html_attrs["unique"])
        self.assertTrue(f.html_attrs["multiple"])
        # Exception checking:
        with self.assertRaises(AssertionError):
            f = ChoiceIntMultField(choices="not list")
        with self.assertRaises(AssertionError):
            f = ChoiceIntMultField(choices=[])
        with self.assertRaises(AssertionError):
            f = ChoiceIntMultField(default="not list")
        with self.assertRaises(AssertionError):
            f = ChoiceIntMultField(default=[])
        with self.assertRaises(AssertionError):
            f = ChoiceIntMultField(default=[3], choices=[[1, "Title"], [2, "Title 2"]])
        with self.assertRaises(AssertionError):
            f = ChoiceIntMultField(default=[2, 3], choices=[[1, "Title"], [2, "Title 2"]])
        # Methods:
        f = ChoiceIntMultField()
        self.assertTrue(f.has_value())
        f = ChoiceIntMultField(default=[2], choices=[[1, "Title"], [2, "Title 2"]])
        self.assertTrue(f.has_value())
        f = ChoiceIntMultField(choices=[[1, "Title"], [2, "Title 2"]])
        self.assertTrue(f.has_value())
        f.html_attrs["value"] = [2]
        self.assertTrue(f.has_value())
        f.html_attrs["value"] = [3]
        self.assertFalse(f.has_value())
        f.html_attrs["value"] = [2, 3]
        self.assertFalse(f.has_value())

    def test_choice_int_dyn_field(self):
        """Testing `ChoiceIntDynField`."""
        # Parameters by default:
        f = ChoiceIntDynField()
        self.assertEqual(f.html_attrs["id"], "")
        self.assertEqual(f.html_attrs["label"], "")
        self.assertEqual(f.html_attrs["name"], "")
        self.assertEqual(f.html_attrs["field_type"], "ChoiceIntDynField")
        self.assertFalse(f.html_attrs["disabled"])
        self.assertFalse(f.html_attrs["hide"])
        self.assertFalse(f.html_attrs["ignored"])
        self.assertEqual(len(f.html_attrs["warning"]), 0)
        self.assertEqual(f.html_attrs["errors"], [])
        self.assertEqual(f.html_attrs["group"], "choice")
        self.assertIsNone(f.html_attrs["value"])
        self.assertEqual(f.html_attrs["hint"], "")
        self.assertFalse(f.html_attrs["required"])
        self.assertFalse(f.html_attrs["readonly"])
        self.assertFalse(f.html_attrs["unique"])
        self.assertFalse(f.html_attrs["multiple"])

    def test_choice_int_mult_dyn_field(self):
        """Testing `ChoiceIntMultDynField`."""
        # Parameters by default:
        f = ChoiceIntMultDynField()
        self.assertEqual(f.html_attrs["id"], "")
        self.assertEqual(f.html_attrs["label"], "")
        self.assertEqual(f.html_attrs["name"], "")
        self.assertEqual(f.html_attrs["field_type"], "ChoiceIntMultDynField")
        self.assertFalse(f.html_attrs["disabled"])
        self.assertFalse(f.html_attrs["hide"])
        self.assertFalse(f.html_attrs["ignored"])
        self.assertEqual(len(f.html_attrs["warning"]), 0)
        self.assertEqual(f.html_attrs["errors"], [])
        self.assertEqual(f.html_attrs["group"], "choice")
        self.assertIsNone(f.html_attrs["value"])
        self.assertEqual(f.html_attrs["hint"], "")
        self.assertFalse(f.html_attrs["required"])
        self.assertFalse(f.html_attrs["readonly"])
        self.assertFalse(f.html_attrs["unique"])
        self.assertTrue(f.html_attrs["multiple"])


if __name__ == "__main__":
    unittest.main()
