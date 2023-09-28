#!/usr/bin/env python3
""" Module to return a multiplier by multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """create a multiplier function"""
    def multiplier_function(x: float) -> float:
        """return the multiplier function by multiplier"""
        return multiplier * x

    return multiplier_function
