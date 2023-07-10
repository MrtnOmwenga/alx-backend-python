#!/usr/bin/env python3
"""
Annotate exercise
"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns tuple with sequance and int """
    return [(i, len(i)) for i in lst]
