#!/usr/bin/env python3
"""
Return a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function
    """

    func: Callable[[float], float] = lambda x: x * multiplier
    return func
