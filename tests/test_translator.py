"""Testing the module  `ramifice > translations`."""

from __future__ import annotations

import unittest

from ramifice import Model, Translator, fields, meta

_ = Translator.STUB_TRANSLATOR_FOR_ATTRIBUTES_OF_FIELDS


@meta(service_name="Accounts")
class User(Model):
    """Model for testing."""

    email = fields.EmailField(label=_("Email"))


class TestTranslations(unittest.TestCase):
    """Testing the module  `ramifice > translations`."""

    def test_add_languages(self):
        """Testing `add_languages`."""
        Translator.add_new_languages(frozenset(("en", "ru")))

    def test_change_locale(self):
        """Testing `change_locale` method."""
        _ = Translator.ramifice_translator().gettext

        self.assertEqual(_("Document ID"), "Document ID")

        _ = Translator.ramifice_translator("ru").gettext
        self.assertEqual(_("Document ID"), "Идентификатор документа")

        user = User("ru")

        self.assertEqual(user.id__html_attrs["label"], "Идентификатор документа")
        self.assertEqual(user.id__html_attrs["placeholder"], "Он добавляется автоматически")
        self.assertEqual(user.id__html_attrs["hint"], "Он добавляется автоматически")

        self.assertEqual(user.created_at__html_attrs["label"], "Создан")
        self.assertEqual(user.created_at__html_attrs["placeholder"], "Он добавляется автоматически")
        self.assertEqual(user.created_at__html_attrs["hint"], "Он добавляется автоматически")
        self.assertEqual(user.created_at__html_attrs["warning"], ["Когда был создан документ."])

        self.assertEqual(user.updated_at__html_attrs["label"], "Обновлен")
        self.assertEqual(user.updated_at__html_attrs["placeholder"], "Он добавляется автоматически")
        self.assertEqual(user.updated_at__html_attrs["hint"], "Он добавляется автоматически")
        self.assertEqual(user.updated_at__html_attrs["warning"], ["Когда был обновлен документ."])

        self.assertEqual(user.email__html_attrs["label"], "Email")
        self.assertEqual(user.email__html_attrs["placeholder"], "")
        self.assertEqual(user.email__html_attrs["hint"], "")


if __name__ == "__main__":
    unittest.main()
