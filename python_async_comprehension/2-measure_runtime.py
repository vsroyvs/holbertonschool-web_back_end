#!/usr/bin/env python3
"""Module that run parallel comprehensions"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """total execution time"""
    start_time = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    finish_time = time.time()
    total_runtime = finish_time - start_time
    return total_runtime
