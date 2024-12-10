"""Testing a parameters with default values for text fields."""

import unittest
from ramifice.fields import fields


class TestTextFields(unittest.TestCase):
    """Testing parameters with default values."""

    def test_text_field(self):
        """Testing a parameters by default for TextField."""
        f = fields.TextField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, "TextField")
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, "text")
        self.assertEqual(f.input_type, "text")
        self.assertFalse(f.textarea)
        self.assertFalse(f.use_editor)
        self.assertEqual(f.value, '')
        self.assertEqual(f.default, '')
        self.assertEqual(f.placeholder, '')
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertFalse(f.unique)
        self.assertEqual(f.maxlength, 256)
        self.assertEqual(f.regex, '')
        self.assertEqual(f.regex_err_msg, '')

    def test_url_field(self):
        """Testing a parameters by default for URLField."""
        f = fields.URLField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, "URLField")
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, "text")
        self.assertEqual(f.input_type, "url")
        self.assertEqual(f.value, '')
        self.assertEqual(f.default, '')
        self.assertEqual(f.placeholder, '')
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertFalse(f.unique)
        self.assertEqual(f.maxlength, 2083)

    def test_slug_field(self):
        """Testing a parameters by default for SlugField."""
        f = fields.SlugField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, "SlugField")
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, "slug")
        self.assertEqual(f.input_type, "text")
        self.assertEqual(f.value, '')
        self.assertEqual(f.default, ['hash'])
        self.assertEqual(f.placeholder, '')
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertTrue(f.unique)
        self.assertIsNone(f.slug_sources)


if __name__ == '__main__':
    unittest.main()
