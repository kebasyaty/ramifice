"""Testing `Ramifice > QPaladinsMixin > PsswordMixin` module."""

import unittest

from pymongo import AsyncMongoClient

from ramifice import model
from ramifice.fields import PasswordField
from ramifice.migration import Monitor


@model(service_name="Accounts")
class User:
	"""Model for testing."""

	def fields(self, gettext):
		"""For add fields."""
		self.password = PasswordField()
		self.password_2 = PasswordField()


class TestPaladinPasswordMixin(unittest.IsolatedAsyncioTestCase):
	"""Testing `Ramifice > QPaladinsMixin > PsswordMixin` module."""

	async def test_pssword_methods(self):
		"""Testing PsswordMixin module."""
		# Maximum number of characters 60.
		database_name = "test_pssword_methods"

		# Delete database before test.
		# (if the test fails)
		client = AsyncMongoClient()
		await client.drop_database(database_name)
		await client.close()

		client = AsyncMongoClient()
		await Monitor(
			database_name=database_name,
			mongo_client=client,
		).migrat()
		#
		# HELLISH BURN
		# ----------------------------------------------------------------------
		m = User()
		password = "12345678"
		new_password = "new_12345678"
		password_2 = "123456789"
		new_password_2 = "new_123456789"
		m.password.value = password
		m.password_2.value = password_2
		# self.assertTrue(await m.save())
		if not await m.save():
			m.print_err()
		self.assertEqual(await User.estimated_document_count(), 1)
		self.assertTrue(await m.verify_password(password))
		self.assertFalse(await m.verify_password("123"))
		self.assertTrue(await m.verify_password(password_2, "password_2"))
		self.assertFalse(await m.verify_password("123", "password_2"))
		await m.update_password(password, new_password)
		self.assertTrue(await m.verify_password(new_password))
		await m.update_password(password_2, new_password_2, "password_2")
		self.assertTrue(await m.verify_password(new_password_2, "password_2"))
		# ----------------------------------------------------------------------
		#
		# Delete database after test.
		await client.drop_database(database_name)
		await client.close()


if __name__ == "__main__":
	unittest.main()
