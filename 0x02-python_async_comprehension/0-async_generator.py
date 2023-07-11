#!/usr/bin/env python3
"""
The coroutine will loop 10 times, each
time asynchronously wait 1 second, then
yield a random number between 0 and 10.
"""
import asyncio
from typing import Generator, AsyncGenerator
from random import random


async def async_generator() -> AsyncGenerator[float, None]:
    """ Returns an async generator """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random() * 10
