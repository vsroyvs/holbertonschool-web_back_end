#!/usr/bin/env python3
'''module to calculate start index and end index'''


def index_range(page: int, page_size: int):
    """eturn a tuple of size two containing a start index and an end index"""
    if page < 1 or page_size <= 0:
        raise ValueError("Parameters must be positive integers")
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
