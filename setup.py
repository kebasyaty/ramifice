"""Stub for PIP."""

from __future__ import annotations

MSG = (
    "Ramifice no supports building via setup.py, "
    "use python -m pip install <path/to/ramifice> instead. If "
    "this is an editable install (-e) please upgrade to pip>=21.3 first: "
    "python -m pip install --upgrade pip"
)

raise RuntimeError(MSG)
