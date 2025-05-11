"""Queries like `find many`."""

from typing import Any

from pymongo.asynchronous.collection import AsyncCollection
from pymongo.results import DeleteResult

from .. import store
from ..tools import model_is_migrated


class ManyMixin:
    """Queries like `find many`."""
