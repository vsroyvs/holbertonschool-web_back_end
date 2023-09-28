#!/usr/bin/env python3
""" Module to sum a element of list (float and int)"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum a list of floats and ints"""
    return sum(mxd_lst)
