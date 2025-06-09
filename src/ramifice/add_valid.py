"""Additional validation of fields."""

from abc import ABCMeta


class AddValidMixin(metaclass=ABCMeta):
	"""Additional validation of fields."""

	async def add_validation(self) -> dict[str, str]:
		"""For additional validation of fields."""
		error_map: dict[str, str] = {}
		return error_map
