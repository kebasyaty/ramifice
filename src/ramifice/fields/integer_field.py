"""Field of Model for enter (int) number."""

from ..mixins import JsonMixin
from ..store import DEBUG
from .general.field import Field
from .general.number_group import NumberGroup


class IntegerField(Field, NumberGroup, JsonMixin):
	"""Field of Model for enter (int) number."""

	def __init__(  # noqa: D107
		self,
		label: str = "",
		disabled: bool = False,
		hide: bool = False,
		ignored: bool = False,
		hint: str = "",
		warning: list[str] | None = None,
		default: int | None = None,
		placeholder: str = "",
		required: bool = False,
		readonly: bool = False,
		unique: bool = False,
		max_number: int | None = None,
		min_number: int | None = None,
		step: int = 1,
		input_type: str = "number",  # number | range
	):
		if DEBUG:
			if input_type not in ["number", "range"]:
				raise AssertionError(
					"Parameter `input_type` - Invalid input type! "
					+ "The permissible value of `number` or `range`."
				)
			if max_number is not None and not isinstance(max_number, int):
				raise AssertionError("Parameter `max_number` - Not а number `int` type!")
			if min_number is not None and not isinstance(min_number, int):
				raise AssertionError("Parameter `min_number` - Not а number `int` type!")
			if not isinstance(step, int):
				raise AssertionError("Parameter `step` - Not а number `int` type!")
			if max_number is not None and min_number is not None and max_number <= min_number:
				raise AssertionError(
					"The `max_number` parameter should be more than the `min_number`!"
				)
			if default is not None:
				if not isinstance(default, int):
					raise AssertionError("Parameter `default` - Not а number `int` type!")
				if max_number is not None and default > max_number:
					raise AssertionError("Parameter `default` is more `max_number`!")
				if max_number is not None and default < min_number:  # type: ignore
					raise AssertionError("Parameter `default` is less `min_number`!")

		Field.__init__(
			self,
			label=label,
			disabled=disabled,
			hide=hide,
			ignored=ignored,
			hint=hint,
			warning=warning,
			field_type="IntegerField",
			group="num",
		)
		NumberGroup.__init__(
			self,
			placeholder=placeholder,
			required=required,
			readonly=readonly,
			unique=unique,
		)
		JsonMixin.__init__(self)

		self.input_type: str = input_type
		self.value: int | None = None
		self.default = default
		self.max_number = max_number
		self.min_number = min_number
		self.step = step
