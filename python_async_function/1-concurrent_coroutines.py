#!/usr/bin/env python3
""" module where we can execute multiples coroutines in parallel"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ List of floats, length n times"""
    list = [wait_random(max_delay) for _ in n]
    delay_times = [await i for i in asyncio.as_completed(list)]
    return sorted(delay_times)
