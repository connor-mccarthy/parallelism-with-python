import asyncio
import math
import time
from typing import Callable, List

import colorama
from colorama import Fore
from typing_extensions import Literal

colorama.init(autoreset=True)


def computationally_expensive_function(n=1_000_000) -> None:
    start = 1
    pos = start
    k_sq = 1000 * 1000
    while pos < n:
        pos += 1
        math.sqrt((pos - k_sq) * (pos - k_sq))


async def blocking_async_function(sleep_time: float) -> Literal[1]:
    await asyncio.sleep(sleep_time)
    return 1


def blocking_sync_function(sleep_time: float) -> Literal[1]:
    time.sleep(sleep_time)
    return 1


def blocking_sync_function_with_list(sleep_time: float, data: List) -> None:
    time.sleep(sleep_time)
    data.append(1)


async def compare_approaches(
    func1: Callable,
    func2: Callable,
    async1=False,
    async2=False,
) -> None:
    print(Fore.RED + "   Slower approach:", end=" ")
    slow = await timer(func1, is_async=async1)
    print(Fore.GREEN + "   Faster approach:", end=" ")
    fast = await timer(func2, is_async=async2)
    print(Fore.BLUE + f"   Speed improvement {round(slow/fast, 2)}x")


async def timer(func: Callable, is_async=False, *args, **kwargs) -> float:
    start_time = time.perf_counter()
    await func(*args, **kwargs) if is_async else func(*args, **kwargs)
    end_time = time.perf_counter()
    run_time = end_time - start_time
    print(f"Finished '{func.__qualname__}' in {round(run_time, 4)}s", flush=True)
    return run_time
