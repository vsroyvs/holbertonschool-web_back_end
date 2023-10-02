#!/usr/bin/env python3
""" module where we measure the runtime"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """total time of execution"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    finish_time = time.time()

    total_time = finish_time - start_time
    return total_time / n
