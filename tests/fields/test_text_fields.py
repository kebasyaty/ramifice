"""Testing a parameters with default values for text fields."""

import unittest
from ramifice.fields import (
    TextField, URLField, SlugField, PhoneField,
    PasswordField, IPField, HashField, EmailField, ColorField)


class TestTextFields(unittest.TestCase):
    """Testing parameters with default values."""

    def test_text_field(self):
        """Testing `TextField`."""
        # Parameters by default:
        f = TextField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, 'TextField')
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, 'text')
        self.assertEqual(f.input_type, 'text')
        self.assertFalse(f.textarea)
        self.assertFalse(f.use_editor)
        self.assertIsNone(f.value)
        self.assertIsNone(f.default)
        self.assertEqual(f.placeholder, "")
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertFalse(f.unique)
        self.assertEqual(f.maxlength, 256)
        self.assertEqual(f.regex, "")

    def test_url_field(self):
        """Testing `URLField`."""
        # Parameters by default:
        f = URLField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, "URLField")
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, 'text')
        self.assertEqual(f.input_type, 'url')
        self.assertIsNone(f.value)
        self.assertIsNone(f.default)
        self.assertEqual(f.placeholder, "")
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertFalse(f.unique)
        self.assertEqual(f.maxlength, 2083)

    def test_slug_field(self):
        """Testing `SlugField`."""
        # Parameters by default:
        f = SlugField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, 'SlugField')
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, 'slug')
        self.assertEqual(f.input_type, 'text')
        self.assertIsNone(f.value)
        self.assertEqual(f.placeholder, "")
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertTrue(f.unique)
        self.assertEqual(f.slug_sources, ['hash'])

    def test_phone_field(self):
        """Testing `PhoneField`."""
        # Parameters by default:
        f = PhoneField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, 'PhoneField')
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, 'text')
        self.assertEqual(f.input_type, 'tel')
        self.assertIsNone(f.value)
        self.assertIsNone(f.default)
        self.assertEqual(f.placeholder, "")
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertFalse(f.unique)
        self.assertEqual(f.regex, "")

    def test_password_field(self):
        """Testing `PasswordField`."""
        # Parameters by default:
        f = PasswordField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, 'PasswordField')
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, 'password')
        self.assertEqual(f.input_type, 'password')
        self.assertIsNone(f.value)
        self.assertEqual(f.placeholder, "")
        self.assertFalse(f.required)
        self.assertEqual(f.regex, "")

    def test_ip_field(self):
        """Testing `IPField`."""
        # Parameters by default:
        f = IPField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, 'IPField')
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, 'text')
        self.assertEqual(f.input_type, 'text')
        self.assertIsNone(f.value)
        self.assertIsNone(f.default)
        self.assertEqual(f.placeholder, "")
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertFalse(f.unique)

    def test_hash_field(self):
        """Testing `HashField`."""
        # Parameters by default:
        f = HashField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, 'HashField')
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, 'hash')
        self.assertEqual(f.input_type, 'text')
        self.assertIsNone(f.value)
        self.assertEqual(f.placeholder, "")
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertFalse(f.unique)
        self.assertEqual(f.maxlength, 24)
        # Methods:
        self.assertIsNone(f.object_id())

    def test_email_field(self):
        """Testing `EmailField`."""
        # Parameters by default:
        f = EmailField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, 'EmailField')
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, 'text')
        self.assertEqual(f.input_type, 'email')
        self.assertIsNone(f.value)
        self.assertIsNone(f.default)
        self.assertEqual(f.placeholder, "")
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertFalse(f.unique)

    def test_color_field(self):
        """Testing `ColorField`."""
        # Parameters by default:
        f = ColorField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, 'ColorField')
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, 'text')
        self.assertEqual(f.input_type, 'text')
        self.assertIsNone(f.value)
        self.assertEqual(f.default, '#000000')
        self.assertEqual(f.placeholder, '')
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertFalse(f.unique)


if __name__ == '__main__':
    unittest.main()
