"""Testing the module  `ramifice > translations`."""

from __future__ import annotations

import unittest

from ramifice import Translator, fields, model


@model(service_name="Accounts")
class User:
    """Model for testing."""

    email = fields.EmailField()


Translator.activate()


class TestTranslations(unittest.TestCase):
    """Testing the module  `ramifice > translations`."""

    def test_add_languages(self):
        """Testing `add_languages`."""
        Translator.add_new_languages(frozenset(("en", "ru")))

    def test_change_locale(self):
        """Testing `change_locale` method."""
        _ = Translator.ramifice_translator.gettext

        self.assertEqual(_("Document ID"), "Document ID")

        Translator.change_locale("ru")
        _ = Translator.ramifice_translator.gettext
        self.assertEqual(_("Document ID"), "Идентификатор документа")

        user = User()

        self.assertEqual(user.id_html_attrs["label"], "Идентификатор документа")
        self.assertEqual(user.id_html_attrs["placeholder"], "Он добавляется автоматически")
        self.assertEqual(user.id_html_attrs["hint"], "Он добавляется автоматически")

        self.assertEqual(user.created_at_html_attrs["label"], "Создан")
        self.assertEqual(user.created_at_html_attrs["placeholder"], "Он добавляется автоматически")
        self.assertEqual(user.created_at_html_attrs["hint"], "Он добавляется автоматически")
        self.assertEqual(user.created_at_html_attrs["warning"], ["Когда был создан документ."])

        self.assertEqual(user.updated_at_html_attrs["label"], "Обновлен")
        self.assertEqual(user.updated_at_html_attrs["placeholder"], "Он добавляется автоматически")
        self.assertEqual(user.updated_at_html_attrs["hint"], "Он добавляется автоматически")
        self.assertEqual(user.updated_at_html_attrs["warning"], ["Когда был обновлен документ."])

        self.assertEqual(user.email_html_attrs["label"], "")
        self.assertEqual(user.email_html_attrs["placeholder"], "")
        self.assertEqual(user.email_html_attrs["hint"], "")


if __name__ == "__main__":
    unittest.main()
