#!/usr/bin/env python3
"""module to create a asynck function"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """return a asyncio.Task"""
    return asyncio.create_task(wait_random(max_delay))
