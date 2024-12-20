"""Testing text fields."""

import unittest
from ramifice.fields import (
    TextField, URLField, SlugField, PhoneField,
    PasswordField, IPField, HashField, EmailField, ColorField)


class TestTextFields(unittest.TestCase):
    """Testing text fields."""

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
        # Additional check:
        with self.assertRaises(AssertionError):
            TextField(default=12)
        with self.assertRaises(AssertionError):
            TextField(maxlength='256')
        with self.assertRaises(AssertionError):
            TextField(default="")
        with self.assertRaises(AssertionError):
            TextField(default='Hello!', maxlength=3)
        TextField(default='Hello!')
        TextField(maxlength=512)

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
        # Additional check:
        with self.assertRaises(AssertionError):
            URLField(default="")
        with self.assertRaises(AssertionError):
            URLField(default='http://???')
        URLField(default='https://www.google.com')

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
        # Additional check:
        with self.assertRaises(AssertionError):
            PhoneField(default=12)
        with self.assertRaises(AssertionError):
            PhoneField(default="")
        with self.assertRaises(AssertionError):
            PhoneField(default='Алло!')
        with self.assertRaises(AssertionError):
            PhoneField(default='+4002123456')
        PhoneField(default='+447986123456')

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
        # Additional check:
        with self.assertRaises(AssertionError):
            IPField(default=12)
        with self.assertRaises(AssertionError):
            IPField(default="")
        with self.assertRaises(AssertionError):
            IPField(default='some address')
        with self.assertRaises(AssertionError):
            IPField(default='127.0.')
        IPField(default='127.0.0.1')

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
        # Additional check:
        with self.assertRaises(AssertionError):
            EmailField(default=12)
        with self.assertRaises(AssertionError):
            EmailField(default="")
        with self.assertRaises(AssertionError):
            EmailField(default='my+address@example.net')
        EmailField(default='kebasyaty@gmail.com')

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
        # Additional check:
        with self.assertRaises(AssertionError):
            ColorField(default=12)
        with self.assertRaises(AssertionError):
            ColorField(default='color')
        ColorField(default='#000')


if __name__ == '__main__':
    unittest.main()
