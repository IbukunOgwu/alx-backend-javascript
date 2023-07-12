#!/usr/bin/env python3
"""Creates or generates an async generator"""
import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """Each of the time, awaits 1 second before it gives a random number
        between 0 and 10"""
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
