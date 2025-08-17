"""Testing the module `ramifice.utils.constants`."""

import re
import unittest

from ramifice.utils.constants import (
    DATABASE_NAME,
    DEBUG,
    MEDIA_ROOT,
    MEDIA_URL,
    MONGO_CLIENT,
    MONGO_DATABASE,
    REGEX,
    STATIC_ROOT,
    STATIC_URL,
    SUPER_COLLECTION_NAME,
)


class TestConstants(unittest.TestCase):
    """Testing the module `ramifice.utils.constants`."""

    def test_values_by_default(self):
        """Testing a values by default."""
        self.assertTrue(DEBUG)
        self.assertIsNone(MONGO_CLIENT)
        self.assertIsNone(MONGO_DATABASE)
        self.assertIsNone(DATABASE_NAME)
        self.assertEqual(SUPER_COLLECTION_NAME, "SUPER_COLLECTION")
        self.assertEqual(MEDIA_ROOT, "public/media")
        self.assertEqual(MEDIA_URL, "/media")
        self.assertEqual(STATIC_ROOT, "public/static")
        self.assertEqual(STATIC_URL, "/static")
        regex = {
            "database_name": re.compile(r"^[a-zA-Z][-_a-zA-Z0-9]{0,59}$"),
            "service_name": re.compile(r"^[A-Z][a-zA-Z0-9]{0,24}$"),
            "model_name": re.compile(r"^[A-Z][a-zA-Z0-9]{0,24}$"),
            "color_code": re.compile(
                r"^(?:#|0x)(?:[a-f0-9]{3}|[a-f0-9]{6}|[a-f0-9]{8})\b|(?:rgb|hsl)a?\([^\)]*\)$",
                re.IGNORECASE,
            ),
            "password": re.compile(
                r'^[-._!"`\'#%&,:;<>=@{}~\$\(\)\*\+\/\\\?\[\]\^\|a-zA-Z0-9]{8,256}$',
            ),
        }
        self.assertEqual(REGEX, regex)

    def test_regex_database_name(self):
        """Testing a regular expression for `database_name`."""
        p = REGEX["database_name"]
        # Negative:
        self.assertIsNone(p.match(""))
        self.assertIsNone(p.match("Database Name"))
        self.assertIsNone(p.match(" DatabaseName"))
        self.assertIsNone(p.match("5DatabaseName"))
        self.assertIsNone(p.match("_DatabaseName"))
        self.assertIsNone(p.match("-DatabaseName"))
        # > 60 characters
        self.assertIsNone(p.match("LoremIpsumDolorSitAmetConsecteturAdipiscingElitIntegerLacinia"))
        # Positive:
        self.assertIsNotNone(p.match("D"))
        self.assertIsNotNone(p.match("d"))
        self.assertIsNotNone(p.match("test"))
        self.assertIsNotNone(p.match("DatabaseName"))
        self.assertIsNotNone(p.match("Database_Name"))
        self.assertIsNotNone(p.match("Database-Name"))
        self.assertIsNotNone(p.match("databaseName"))
        self.assertIsNotNone(p.match("database_name"))
        self.assertIsNotNone(p.match("database-name"))
        self.assertIsNotNone(p.match("x4N83BGV26b3Npg2"))
        self.assertIsNotNone(p.match("X4N83BGV26b3Npg2"))
        self.assertIsNotNone(p.match("test_X4N83BGV26b3Npg2"))

    def test_regex_service_name(self):
        """Testing a regular expression for `service_name`."""
        p = REGEX["service_name"]
        # Negative:
        self.assertIsNone(p.match(""))
        self.assertIsNone(p.match("Auto parts"))
        self.assertIsNone(p.match("Auto Parts"))
        self.assertIsNone(p.match("autoparts"))
        self.assertIsNone(p.match("Auto_parts"))
        self.assertIsNone(p.match("Auto-parts"))
        self.assertIsNone(p.match("360AutoParts"))
        # > 25 characters
        self.assertIsNone(p.match("Loremipsumdolorsitametcons"))
        # Positive:
        self.assertIsNotNone(p.match("AutoParts"))
        self.assertIsNotNone(p.match("Autoparts"))
        self.assertIsNotNone(p.match("AutoParts360"))

    def test_regex_model_name(self):
        """Testing a regular expression for `model_name`."""
        p = REGEX["model_name"]
        # Negative:
        self.assertIsNone(p.match(""))
        self.assertIsNone(p.match("360"))
        self.assertIsNone(p.match("accounts"))
        self.assertIsNone(p.match("Model Name"))
        self.assertIsNone(p.match("360ModelName"))

        # > 25 characters
        self.assertIsNone(p.match("Loremipsumdolorsitametcons"))
        # Positive:
        self.assertIsNotNone(p.match("Accounts"))
        self.assertIsNotNone(p.match("ACCOUNTS"))
        self.assertIsNotNone(p.match("ModelName"))
        self.assertIsNotNone(p.match("ModelName360"))
        self.assertIsNotNone(p.match("MODELNAME360"))

    def test_regex_color_code(self):
        """Testing a regular expression for `color_code`."""
        p = REGEX["color_code"]
        # Negative:
        self.assertIsNone(p.match(""))
        self.assertIsNone(p.match("#f2ewq"))
        self.assertIsNone(p.match("red"))
        self.assertIsNone(p.match("green"))
        self.assertIsNone(p.match("blue"))
        self.assertIsNone(p.match("yellow"))
        self.assertIsNone(p.match("orange"))
        self.assertIsNone(p.match("purple"))
        self.assertIsNone(p.match("white"))
        self.assertIsNone(p.match("black"))
        self.assertIsNone(p.match("grey"))
        # Positive:
        self.assertIsNotNone(p.match("#fff"))
        self.assertIsNotNone(p.match("#f2f2f2"))
        self.assertIsNotNone(p.match("#F2F2F2"))
        self.assertIsNotNone(p.match("#00000000"))
        self.assertIsNotNone(p.match("rgb(255,0,24)"))
        self.assertIsNotNone(p.match("rgb(255, 0, 24)"))
        self.assertIsNotNone(p.match("rgba(255, 0, 24, .5)"))
        self.assertIsNotNone(p.match("rgba(#fff, .5)"))
        self.assertIsNotNone(p.match("rgba(#fff,.5)"))
        self.assertIsNotNone(p.match("rgba(#FFF, .5)"))
        self.assertIsNotNone(p.match("rgba(#FFF,.5)"))
        self.assertIsNotNone(p.match("hsl(120, 100%, 50%)"))
        self.assertIsNotNone(p.match("hsl(120,100%,50%)"))
        self.assertIsNotNone(p.match("hsla(170, 23%, 25%, 0.2)"))
        self.assertIsNotNone(p.match("hsla(170,23%,25%,0.2)"))
        self.assertIsNotNone(p.match("0x00ffff"))
        self.assertIsNotNone(p.match("0x00FFFF"))

    def test_regex_password(self):
        """Testing a regular expression for `password`."""
        p = REGEX["password"]
        digits = "0123456789"  # noqa: FURB156
        ascii_lowercase = "abcdefghijklmnopqrstuvwxyz"  # noqa: FURB156
        ascii_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # noqa: FURB156
        special_symbols = "-._!\"`'#%&,:;<>=@{}~$()*+/\\?[]^|"
        # Negative:
        self.assertIsNone(p.match(""))
        self.assertIsNone(p.match(" "))
        self.assertIsNone(p.match("пока-пока"))
        self.assertIsNone(p.match("再見-再見-再見"))
        self.assertIsNone(p.match("1234567"))  # < 8 characters
        self.assertIsNone(p.match(("12345678" * 32) + "1"))  # > 256 characters
        # Positive:
        self.assertIsNotNone(p.match(digits))
        self.assertIsNotNone(p.match(ascii_lowercase))
        self.assertIsNotNone(p.match(ascii_uppercase))
        self.assertIsNotNone(p.match(special_symbols))
        self.assertIsNotNone(p.match(digits + ascii_lowercase + ascii_uppercase + special_symbols))
        self.assertIsNotNone(p.match("12345678"))  # == 8 characters
        self.assertIsNotNone(p.match("12345678" * 32))  # == 256 characters
        self.assertIsNotNone(p.match("9M,4%6]3ht7r{l59"))
        self.assertIsNotNone(p.match("2XT~m:L!Hz_723J("))
        self.assertIsNotNone(p.match("d6'P30}e'#f^g3t5"))


if __name__ == "__main__":
    unittest.main()
