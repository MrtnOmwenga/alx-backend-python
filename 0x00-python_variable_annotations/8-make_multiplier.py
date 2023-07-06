#!/usr/bin/env python3
from typing import Callable
"""
Return a function that multiplies a float by multiplier.
"""


def make_multiplier(multiplier: float)-> Callable[[float], float]:
    """
    Returns a function
    """

    func: Callable[[float], float] = lambda x: x * multiplier
    return func
