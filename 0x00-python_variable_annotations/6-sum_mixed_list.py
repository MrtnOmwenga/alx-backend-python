#!/usr/bin/env python3
"""
Sum elements of a list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns a float
    """

    return float(sum(mxd_lst))
