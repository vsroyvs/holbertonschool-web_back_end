#!/usr/bin/env python3
"""desc"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """desc"""
    list = [task_wait_random(max_delay) for _ in range(n)]
    delay_times = [await i for i in asyncio.as_completed(list)]
    return sorted(delay_times)
