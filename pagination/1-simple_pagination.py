#!/usr/bin/env python3
'''module to read a csv file and diplay ccording to the parameters'''
import csv
import math
from typing import List


def index_range(page: int, page_size: int):
    """return a tuple of size two containing a start index and an end index"""
    if page < 1 or page_size <= 0:
        raise ValueError("Parameters must be positive integers")
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns dataset for the given page"""
        total_items = len(self.dataset)
        total_pages = (total_items + page_size - 1) // page_size
        assert_text = "AssertionError raised with negative values"
        assert page < 0 or page_size < 0, assert_text
        assert page == 0 or page_size == 0, "AssertionError raised with 0"
        text = "AssertionError raised when page and/or page_size are not ints"
        assert type(page) is not int or type(page_size) is not int, text
        if 1 <= page <= total_pages:
            page_data = self.dataset[index_range(page, page_size)]
            return page_data
        else:
            return []
