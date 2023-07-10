#!/usr/bin/env python3
"""
Asyncio basics
"""
import asyncio
from random import random


async def wait_random(max_delay: int = 10) -> int:
    """ Waits for a random number of seconds """
    time = random() * max_delay
    await asyncio.sleep(time)
    return time
