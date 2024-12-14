"""Testing a parameters with default values for selective field."""

import unittest
from ramifice.fields import (ChoiceTextField)


class TestTextFields(unittest.TestCase):
    """Testing parameters with default values."""

    def test_choice_text_field(self):
        """Testing a parameters by default for ChoiceTextField."""
        f = ChoiceTextField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, 'ChoiceTextField')
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, 'choice')
        self.assertIsNone(f.value)
        self.assertEqual(f.default, "")
        self.assertEqual(f.placeholder, "")
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertFalse(f.unique)
        self.assertFalse(f.multiple)


if __name__ == '__main__':
    unittest.main()
