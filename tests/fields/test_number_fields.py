"""Testing number fields."""

import unittest

from ramifice.fields import FloatField, IntegerField


class TestNumberFields(unittest.TestCase):
    """Testing number fields."""

    def test_integer_field(self):
        """Testing `IntegerField`."""
        # Parameters by default:
        f = IntegerField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, "IntegerField")
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertEqual(f.errors, [])
        self.assertEqual(f.group, "num")
        self.assertEqual(f.input_type, "number")
        self.assertIsNone(f.value)
        self.assertIsNone(f.default)
        self.assertEqual(f.placeholder, "")
        self.assertEqual(f.hint, "")
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertFalse(f.unique)
        self.assertIsNone(f.max_number)
        self.assertIsNone(f.min_number)
        self.assertEqual(f.step, int(1))
        # Exception checking:
        with self.assertRaises(AssertionError):
            IntegerField(input_type="")
        with self.assertRaises(AssertionError):
            IntegerField(input_type="numbe")
        with self.assertRaises(AssertionError):
            IntegerField(input_type="rang")
        IntegerField(input_type="number")
        IntegerField(input_type="range")
        with self.assertRaises(AssertionError):
            IntegerField(default="")
        with self.assertRaises(AssertionError):
            IntegerField(default=float(12))
        with self.assertRaises(AssertionError):
            IntegerField(default=12.0)
        with self.assertRaises(AssertionError):
            IntegerField(max_number=12.0)
        with self.assertRaises(AssertionError):
            IntegerField(min_number=12.0)
        with self.assertRaises(AssertionError):
            IntegerField(step=2.0)
        with self.assertRaises(AssertionError):
            IntegerField(max_number=12, min_number=12)
        with self.assertRaises(AssertionError):
            IntegerField(max_number=12, min_number=13)
        with self.assertRaises(AssertionError):
            IntegerField(default=11, max_number=13, min_number=12)
        with self.assertRaises(AssertionError):
            IntegerField(default=14, max_number=13, min_number=12)
        IntegerField(default=12)
        IntegerField(max_number=12)
        IntegerField(min_number=12)
        IntegerField(step=2)
        IntegerField(default=12, max_number=13, min_number=12)
        IntegerField(default=13, max_number=13, min_number=12)

    def test_float_field(self):
        """Testing `FloatField`."""
        # Parameters by default:
        f = FloatField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, "FloatField")
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertEqual(f.errors, [])
        self.assertEqual(f.group, "num")
        self.assertEqual(f.input_type, "number")
        self.assertIsNone(f.value)
        self.assertIsNone(f.default)
        self.assertEqual(f.placeholder, "")
        self.assertEqual(f.hint, "")
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertFalse(f.unique)
        self.assertIsNone(f.max_number)
        self.assertIsNone(f.min_number)
        self.assertEqual(f.step, float(1))
        # Exception checking:
        with self.assertRaises(AssertionError):
            FloatField(input_type="")
        with self.assertRaises(AssertionError):
            FloatField(input_type="numbe")
        with self.assertRaises(AssertionError):
            FloatField(input_type="rang")
        FloatField(input_type="number")
        FloatField(input_type="range")
        with self.assertRaises(AssertionError):
            FloatField(default="")
        with self.assertRaises(AssertionError):
            FloatField(default=int(12))
        with self.assertRaises(AssertionError):
            FloatField(default=12)
        with self.assertRaises(AssertionError):
            FloatField(max_number=12)
        with self.assertRaises(AssertionError):
            FloatField(min_number=12)
        with self.assertRaises(AssertionError):
            FloatField(step=2)
        with self.assertRaises(AssertionError):
            FloatField(max_number=12.0, min_number=12.0)
        with self.assertRaises(AssertionError):
            FloatField(max_number=12.0, min_number=13.0)
        with self.assertRaises(AssertionError):
            FloatField(default=14.0, max_number=13.0, min_number=12.0)
        with self.assertRaises(AssertionError):
            FloatField(default=11.0, max_number=13.0, min_number=12.0)
        FloatField(default=12.0)
        FloatField(max_number=12.0)
        FloatField(min_number=12.0)
        FloatField(step=2.0)
        FloatField(max_number=13.0, min_number=12.0)
        FloatField(default=12.0, max_number=13.0, min_number=12.0)
        FloatField(default=13.0, max_number=13.0, min_number=12.0)


if __name__ == "__main__":
    unittest.main()
