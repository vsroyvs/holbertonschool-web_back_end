#!/usr/bin/env python3
""" Asynchronous coroutine """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ Returns a random delay time"""
    number_random = random.uniform(0, max_delay)
    await asyncio.sleep(number_random)
    return number_random
