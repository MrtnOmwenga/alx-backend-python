#!/usr/bin/env python3
from typing import Union, Tuple
"""
Combines parameters into a tuple
"""


def to_kv(k: str, v: Union[int, float])-> Tuple[str, float]:
    """
    Returns a tuple containing a string and float
    """

    return (k, v**2)
