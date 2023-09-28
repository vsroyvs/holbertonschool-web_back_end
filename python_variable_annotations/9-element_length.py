#!/usr/bin/env python3
""" Module to return a list of tuples"""
from typing import Tuple, List, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples"""
    return [(i, len(i)) for i in lst]
