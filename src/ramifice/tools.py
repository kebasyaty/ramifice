"""Global collection of auxiliary tools."""

import ipaddress
import math
import os
from typing import Any
from urllib.parse import urlparse

import phonenumbers
from bson.objectid import ObjectId
from email_validator import EmailNotValidError, validate_email

from .store import REGEX


def to_human_size(size: int) -> str:
	"""Convert number of bytes to readable format."""
	idx = int(math.floor(math.log(size) / math.log(1024)))
	size = size if size < 1024 else abs(round(size / pow(1024, idx), 2))
	order = ["bytes", "KB", "MB", "GB", "TB"][idx]
	return f"{size} {order}"


def get_file_size(path: str) -> str:
	"""Get human readable version of file size."""
	size = os.path.getsize(path)
	return to_human_size(size)


def normal_email(email: str) -> str | None:
	"""Normalizing email address."""
	normal: str | None = None
	try:
		emailinfo = validate_email(str(email), check_deliverability=False)
		normal = emailinfo.normalized
	except EmailNotValidError:
		pass
	return normal


def is_email(email: str) -> bool:
	"""Validate Email address."""
	flag = True
	try:
		validate_email(str(email), check_deliverability=True)
	except EmailNotValidError:
		flag = False
	return flag


def is_url(url: str) -> bool:
	"""Validate URL address."""
	flag = True
	result = urlparse(str(url))
	if not result.scheme or not result.netloc:
		flag = False
	return flag


def is_ip(address: str | int) -> bool:
	"""Validate IP address."""
	flag = True
	try:
		ipaddress.ip_address(str(address))
	except ValueError:
		flag = False
	return flag


def is_color(color_code: str) -> bool:
	"""Validate Color code."""
	flag = True
	if REGEX["color_code"].match(str(color_code)) is None:
		flag = False
	return flag


def is_phone(number: str) -> bool:
	"""Validate Phone number."""
	flag = True
	try:
		phone = phonenumbers.parse(str(number))
		if not phonenumbers.is_valid_number(phone):
			flag = False
	except phonenumbers.phonenumberutil.NumberParseException:
		flag = False
	return flag


def is_mongo_id(oid: Any) -> bool:
	"""Validation of the Mongodb identifier."""
	return ObjectId.is_valid(oid)


def hash_to_obj_id(hash: str) -> ObjectId | None:
	"""Get ObjectId from hash string."""
	return ObjectId(hash) if bool(hash) else None
