#!/usr/bin/env python3
""" Module to sum a element of list"""


def sum_list(input_list: list[float]) -> float:
    """Sum a list of floats"""
    result = sum((x for x in input_list))
    return result
