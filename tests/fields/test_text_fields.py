"""Testing text fields."""

from __future__ import annotations

import unittest

from ramifice.fields import (
    ColorField,
    EmailField,
    IPField,
    PasswordField,
    PhoneField,
    SlugField,
    TextField,
    URLField,
)


class TestTextFields(unittest.TestCase):
    """Testing text fields."""

    def test_text_field(self):
        """Testing `TextField`."""
        # Parameters by default:
        f = TextField()
        self.assertEqual(f.field_attrs.id, "")
        self.assertEqual(f.field_attrs.label, "")
        self.assertEqual(f.field_attrs.name, "")
        self.assertEqual(f.field_attrs.field_type, "TextField")
        self.assertFalse(f.field_attrs.disabled)
        self.assertFalse(f.field_attrs.hide)
        self.assertFalse(f.field_attrs.ignored)
        self.assertEqual(len(f.field_attrs.warning), 0)
        self.assertEqual(f.field_attrs.errors, [])
        self.assertEqual(f.field_attrs.group, "text")
        self.assertEqual(f.field_attrs.input_type, "text")
        self.assertFalse(f.field_attrs.textarea)
        self.assertFalse(f.field_attrs.use_editor)
        self.assertIsNone(f.field_attrs.value)
        self.assertEqual(f.field_attrs.placeholder, "")
        self.assertEqual(f.field_attrs.hint, "")
        self.assertFalse(f.field_attrs.required)
        self.assertFalse(f.field_attrs.readonly)
        self.assertFalse(f.field_attrs.unique)
        self.assertEqual(f.field_attrs.max_length, 256)
        # Exception checking:
        with self.assertRaises(AssertionError):
            TextField(max_length="256")
        TextField(max_length=512)

    def test_url_field(self):
        """Testing `URLField`."""
        # Parameters by default:
        f = URLField()
        self.assertEqual(f.field_attrs.id, "")
        self.assertEqual(f.field_attrs.label, "")
        self.assertEqual(f.field_attrs.name, "")
        self.assertEqual(f.field_attrs.field_type, "URLField")
        self.assertFalse(f.field_attrs.disabled)
        self.assertFalse(f.field_attrs.hide)
        self.assertFalse(f.field_attrs.ignored)
        self.assertEqual(len(f.field_attrs.warning), 0)
        self.assertEqual(f.field_attrs.errors, [])
        self.assertEqual(f.field_attrs.group, "text")
        self.assertEqual(f.field_attrs.input_type, "url")
        self.assertIsNone(f.field_attrs.value)
        self.assertIsNone(f.field_attrs.default)
        self.assertEqual(f.field_attrs.placeholder, "")
        self.assertEqual(f.field_attrs.hint, "")
        self.assertFalse(f.field_attrs.required)
        self.assertFalse(f.field_attrs.readonly)
        self.assertFalse(f.field_attrs.unique)
        # Exception checking:
        with self.assertRaises(AssertionError):
            URLField(default="")
        with self.assertRaises(AssertionError):
            URLField(default="http://???")
        URLField(default="https://www.google.com")

    def test_slug_field(self):
        """Testing `SlugField`."""
        # Parameters by default:
        f = SlugField()
        self.assertEqual(f.field_attrs.id, "")
        self.assertEqual(f.field_attrs.label, "")
        self.assertEqual(f.field_attrs.name, "")
        self.assertEqual(f.field_attrs.field_type, "SlugField")
        self.assertFalse(f.field_attrs.disabled)
        self.assertFalse(f.field_attrs.hide)
        self.assertFalse(f.field_attrs.ignored)
        self.assertEqual(len(f.field_attrs.warning), 0)
        self.assertEqual(f.field_attrs.errors, [])
        self.assertEqual(f.field_attrs.group, "slug")
        self.assertEqual(f.field_attrs.input_type, "text")
        self.assertIsNone(f.field_attrs.value)
        self.assertEqual(f.field_attrs.placeholder, "")
        self.assertEqual(f.field_attrs.hint, "")
        self.assertFalse(f.field_attrs.required)
        self.assertFalse(f.field_attrs.readonly)
        self.assertTrue(f.field_attrs.unique)
        self.assertEqual(f.field_attrs.slug_sources, "id")

    def test_phone_field(self):
        """Testing `PhoneField`."""
        # Parameters by default:
        f = PhoneField()
        self.assertEqual(f.field_attrs.id, "")
        self.assertEqual(f.field_attrs.label, "")
        self.assertEqual(f.field_attrs.name, "")
        self.assertEqual(f.field_attrs.field_type, "PhoneField")
        self.assertFalse(f.field_attrs.disabled)
        self.assertFalse(f.field_attrs.hide)
        self.assertFalse(f.field_attrs.ignored)
        self.assertEqual(len(f.field_attrs.warning), 0)
        self.assertEqual(f.field_attrs.errors, [])
        self.assertEqual(f.field_attrs.group, "text")
        self.assertEqual(f.field_attrs.input_type, "tel")
        self.assertIsNone(f.field_attrs.value)
        self.assertIsNone(f.field_attrs.default)
        self.assertEqual(f.field_attrs.placeholder, "")
        self.assertEqual(f.field_attrs.hint, "")
        self.assertFalse(f.field_attrs.required)
        self.assertFalse(f.field_attrs.readonly)
        self.assertFalse(f.field_attrs.unique)
        # Exception checking:
        with self.assertRaises(AssertionError):
            PhoneField(default=12)
        with self.assertRaises(AssertionError):
            PhoneField(default="")
        with self.assertRaises(AssertionError):
            PhoneField(default="Алло!")
        with self.assertRaises(AssertionError):
            PhoneField(default="+4002123456")
        PhoneField(default="+447986123456")

    def test_password_field(self):
        """Testing `PasswordField`."""
        # Parameters by default:
        f = PasswordField()
        self.assertEqual(f.field_attrs.id, "")
        self.assertEqual(f.field_attrs.label, "")
        self.assertEqual(f.field_attrs.name, "")
        self.assertEqual(f.field_attrs.field_type, "PasswordField")
        self.assertFalse(f.field_attrs.disabled)
        self.assertFalse(f.field_attrs.hide)
        self.assertFalse(f.field_attrs.ignored)
        self.assertEqual(len(f.field_attrs.warning), 0)
        self.assertEqual(f.field_attrs.errors, [])
        self.assertEqual(f.field_attrs.group, "password")
        self.assertEqual(f.field_attrs.input_type, "password")
        self.assertIsNone(f.field_attrs.value)
        self.assertEqual(f.field_attrs.placeholder, "")
        self.assertEqual(f.field_attrs.hint, "")
        self.assertFalse(f.field_attrs.required)

    def test_ip_field(self):
        """Testing `IPField`."""
        # Parameters by default:
        f = IPField()
        self.assertEqual(f.field_attrs.id, "")
        self.assertEqual(f.field_attrs.label, "")
        self.assertEqual(f.field_attrs.name, "")
        self.assertEqual(f.field_attrs.field_type, "IPField")
        self.assertFalse(f.field_attrs.disabled)
        self.assertFalse(f.field_attrs.hide)
        self.assertFalse(f.field_attrs.ignored)
        self.assertEqual(len(f.field_attrs.warning), 0)
        self.assertEqual(f.field_attrs.errors, [])
        self.assertEqual(f.field_attrs.group, "text")
        self.assertEqual(f.field_attrs.input_type, "text")
        self.assertIsNone(f.field_attrs.value)
        self.assertIsNone(f.field_attrs.default)
        self.assertEqual(f.field_attrs.placeholder, "")
        self.assertEqual(f.field_attrs.hint, "")
        self.assertFalse(f.field_attrs.required)
        self.assertFalse(f.field_attrs.readonly)
        self.assertFalse(f.field_attrs.unique)
        # Exception checking:
        with self.assertRaises(AssertionError):
            IPField(default=12)
        with self.assertRaises(AssertionError):
            IPField(default="")
        with self.assertRaises(AssertionError):
            IPField(default="some address")
        with self.assertRaises(AssertionError):
            IPField(default="127.0.")
        IPField(default="127.0.0.1")

    def test_email_field(self):
        """Testing `EmailField`."""
        # Parameters by default:
        f = EmailField()
        self.assertEqual(f.field_attrs.id, "")
        self.assertEqual(f.field_attrs.label, "")
        self.assertEqual(f.field_attrs.name, "")
        self.assertEqual(f.field_attrs.field_type, "EmailField")
        self.assertFalse(f.field_attrs.disabled)
        self.assertFalse(f.field_attrs.hide)
        self.assertFalse(f.field_attrs.ignored)
        self.assertEqual(len(f.field_attrs.warning), 0)
        self.assertEqual(f.field_attrs.errors, [])
        self.assertEqual(f.field_attrs.group, "text")
        self.assertEqual(f.field_attrs.input_type, "email")
        self.assertIsNone(f.field_attrs.value)
        self.assertIsNone(f.field_attrs.default)
        self.assertEqual(f.field_attrs.placeholder, "")
        self.assertEqual(f.field_attrs.hint, "")
        self.assertFalse(f.field_attrs.required)
        self.assertFalse(f.field_attrs.readonly)
        self.assertFalse(f.field_attrs.unique)
        # Exception checking:
        with self.assertRaises(AssertionError):
            EmailField(default=12)
        with self.assertRaises(AssertionError):
            EmailField(default="")
        with self.assertRaises(AssertionError):
            EmailField(default="my+address@example.net")
        EmailField(default="kebasyaty@gmail.com")

    def test_color_field(self):
        """Testing `ColorField`."""
        # Parameters by default:
        f = ColorField()
        self.assertEqual(f.field_attrs.id, "")
        self.assertEqual(f.field_attrs.label, "")
        self.assertEqual(f.field_attrs.name, "")
        self.assertEqual(f.field_attrs.field_type, "ColorField")
        self.assertFalse(f.field_attrs.disabled)
        self.assertFalse(f.field_attrs.hide)
        self.assertFalse(f.field_attrs.ignored)
        self.assertEqual(len(f.field_attrs.warning), 0)
        self.assertEqual(f.field_attrs.errors, [])
        self.assertEqual(f.field_attrs.group, "text")
        self.assertEqual(f.field_attrs.input_type, "text")
        self.assertIsNone(f.field_attrs.value)
        self.assertEqual(f.field_attrs.default, "#000000")
        self.assertEqual(f.field_attrs.placeholder, "")
        self.assertEqual(f.field_attrs.hint, "")
        self.assertFalse(f.field_attrs.required)
        self.assertFalse(f.field_attrs.readonly)
        self.assertFalse(f.field_attrs.unique)
        # Exception checking:
        with self.assertRaises(AssertionError):
            ColorField(default=12)
        with self.assertRaises(AssertionError):
            ColorField(default="")
        with self.assertRaises(AssertionError):
            ColorField(default="color")
        ColorField(default="#000")


if __name__ == "__main__":
    unittest.main()
