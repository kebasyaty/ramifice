# Ramifice - ORM-pseudo-like API MongoDB for Python language.
# Copyright (c) 2024 Gennady Kostyunin
# SPDX-License-Identifier: MIT
#
# Copyright 2024-present MongoDB, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Custom Exceptions for Ramifice."""

from __future__ import annotations


class RamificeException(Exception):
    """Root Exception for Ramifice."""

    def __init__(self, *args, **kwargs) -> None:
        """Root Exception for Ramifice."""
        super().__init__(*args, **kwargs)


class FileHasNoExtensionError(RamificeException):
    """Exception raised if the file has no extension."""

    def __init__(self, message: str = "File has no extension!") -> None:
        """Exception raised if the file has no extension.

        Args:
            message: explanation of the error
        """
        self.message = message
        super().__init__(self.message)


class DoesNotMatchRegexError(RamificeException):
    """Exception raised if does not match the regular expression."""

    def __init__(self, regex_str: str) -> None:
        """Exception raised if does not match the regular expression.

        Args:
            regex_str: regular expression in string representation
        """
        self.message = f"Does not match the regular expression: {regex_str}"
        super().__init__(self.message)


class NoModelsForMigrationError(RamificeException):
    """Exception raised if no Models for migration."""

    def __init__(self) -> None:
        """Exception raised if no Models for migration."""
        self.message = "No Models for Migration!"
        super().__init__(self.message)


class PanicError(RamificeException):
    """Exception raised for cases of which should not be."""

    def __init__(self, message: str) -> None:
        """Exception raised for cases of which should not be.

        Args:
            message: explanation of the error
        """
        self.message = message
        super().__init__(self.message)


class OldPassNotMatchError(RamificeException):
    """Exception is raised when trying to update the password.

    Hint: If old password does not match.
    """

    def __init__(self) -> None:
        """Exception is raised when trying to update the password.

        Hint: If old password does not match.
        """
        self.message = "Old password does not match!"
        super().__init__(self.message)


class ForbiddenDeleteDocError(RamificeException):
    """Exception is raised when trying to delete the document."""

    def __init__(self, message: str) -> None:
        """Exception is raised when trying to delete the document.

        Args:
            message: explanation of the error
        """
        self.message = message
        super().__init__(self.message)


class NotPossibleAddUnitError(RamificeException):
    """Exception is raised when not possible to add Unit."""

    def __init__(self, message: str) -> None:
        """Exception is raised when not possible to add Unit.

        Args:
            message: explanation of the error
        """
        self.message = message
        super().__init__(self.message)


class NotPossibleDeleteUnitError(RamificeException):
    """Exception is raised when not possible to delete Unit."""

    def __init__(self, message: str) -> None:
        """Exception is raised when not possible to delete Unit.

        Args:
            message: explanation of the error
        """
        self.message = message
        super().__init__(self.message)


class AttributeCannotBeDeleteError(RamificeException):
    """Exception is raised if the attribute cannot be delete."""

    def __init__(self, attribute_name: str) -> None:
        """Exception is raised if the attribute cannot be delete."""
        self.message = f"The attribute `{attribute_name}` cannot be delete!"
        super().__init__(self.message)
