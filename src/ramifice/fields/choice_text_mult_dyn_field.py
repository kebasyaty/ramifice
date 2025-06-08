"""Field of Model.

Type of selective text field with dynamic addition of elements.
"""

from ..mixins import JsonMixin
from .general.choice_group import ChoiceGroup
from .general.field import Field


class ChoiceTextMultDynField(Field, ChoiceGroup, JsonMixin):
	"""Field of Model.

	Type of selective text field with dynamic addition of elements.
	For simulate relationship Many-to-Many.
	"""

	def __init__(  # noqa: D107
		self,
		label: str = "",
		disabled: bool = False,
		hide: bool = False,
		ignored: bool = False,
		hint: str = "",
		warning: list[str] | None = None,
		required: bool = False,
		readonly: bool = False,
	):
		Field.__init__(
			self,
			label=label,
			disabled=disabled,
			hide=hide,
			ignored=ignored,
			hint=hint,
			warning=warning,
			field_type="ChoiceTextMultDynField",
			group="choice",
		)
		ChoiceGroup.__init__(
			self,
			required=required,
			readonly=readonly,
			multiple=True,
		)
		JsonMixin.__init__(self)

		self.value: list[str] | None = None
		self.choices: dict[str, str] | None = None

	def has_value(self) -> bool:
		"""Does the field value match the possible options in choices."""
		value = self.value
		if value is not None:
			choices = self.choices
			if len(value) == 0 or not bool(choices):
				return False
			value_list = choices.values()  # type: ignore[union-attr]
			for item in value:
				if item not in value_list:
					return False
		return True
