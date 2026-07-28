"""Testing the `fixtures` example."""

from __future__ import annotations

import unittest
from datetime import date

from pymongo import AsyncMongoClient

from ramifice import (
    Migration,
    Model,
    Translator,
    fields,
    meta,
    to_human_size,
)
from ramifice.config import Config

_ = Translator.STUB_TRANSLATOR_FOR_ATTRIBUTES_OF_FIELD


@meta(
    service_name="Admin",
    fixture_name="SiteParameters",  # config/fixtures/SiteParameters.yml
    is_create_doc=False,  # Site parameters should be in a single document.
    is_delete_doc=False,
)
class SiteParameters(Model):
    """Site Parameters Model."""

    logo = fields.ImageField(
        label=_("Logo"),
        default="public/media/default/no-photo.png",
        # Available 4 sizes from lg to xs or None.
        # Hint: By default = None
        thumbnails={"lg": 512, "md": 256, "sm": 128, "xs": 64},
        # The maximum size of the original image in bytes.
        # Hint: By default = 2 MB
        max_size=524288,  # 0.5 MB = 524288 Bytes (in binary)
        warning=[
            _("Maximum size: {}").format(to_human_size(524288)),
        ],
    )
    copyright = fields.FileField(
        label=_("File of copyright"),
        default="public/media/default/no_doc.odt",
    )
    brand = fields.TextField(
        label=_("Brand Name"),
        is_require=True,
    )
    slogan = fields.TextField(
        label=_("Slogan"),
        is_require=True,
    )
    about_site = fields.TextField(
        label=_("About the site"),
    )
    email_feedback = fields.EmailField(
        label=_("Email feedback"),
        is_require=True,
    )
    start_date = fields.DateField(
        label=_("Brand foundation date"),
    )
    is_active = fields.BooleanField(
        label=_("Site is active?"),
        default=True,
    )


class TestFixturesExample(unittest.IsolatedAsyncioTestCase):
    """Testing the `fixtures` example."""

    async def test_fixtures_example(self):
        """Testing the `fixtures` example."""
        # Maximum number of characters 60.
        database_name = "fixtures_example"

        client = AsyncMongoClient(host=Config.MONGO_HOST)

        # Delete database before test.
        # (if the test fails)
        await client.drop_database(database_name)
        await client.close()
        #
        # ----------------------------------------------------------------------
        client = AsyncMongoClient(host=Config.MONGO_HOST)
        await Migration(
            database_name=database_name,
            mongo_client=client,
        ).migrate()

        self.assertEqual(await SiteParameters.estimated_document_count(), 1)

        # Get Site Parameters
        site_params: SiteParameters | None = await SiteParameters.find_one_to_instance_model({"brand": "Brand Name"})
        self.assertIsNotNone(site_params)
        self.assertTrue(isinstance(site_params.logo, dict))
        self.assertTrue(isinstance(site_params.copyright, dict))
        self.assertEqual(site_params.brand, "Brand Name")
        self.assertEqual(site_params.slogan, "We are the best!")
        self.assertIsNone(site_params.about_site)
        self.assertEqual(site_params.email_feedback, "John_Smith@gmail.com")
        self.assertEqual(site_params.start_date, date(2000, 1, 25))
        self.assertTrue(site_params.is_active)
        # ----------------------------------------------------------------------
        #
        # Delete database after test.
        await client.drop_database(database_name)
        await client.close()


if __name__ == "__main__":
    unittest.main()
