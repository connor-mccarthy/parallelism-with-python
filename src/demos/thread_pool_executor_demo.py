import asyncio
from concurrent.futures import Future
from concurrent.futures.thread import ThreadPoolExecutor as PoolExecutor
from typing import List

from helpers import blocking_sync_function, compare_approaches

SLEEP_TIME = 1
NUM_OPS = 4


def no_threading_execution_pool() -> None:
    [blocking_sync_function(SLEEP_TIME) for _ in range(NUM_OPS)]


def yes_threading_execution_pool() -> None:
    with PoolExecutor() as executor:
        responses: List[Future] = [  # noqa: F841
            executor.submit(blocking_sync_function, SLEEP_TIME) for _ in range(NUM_OPS)
        ]


async def thread_pool_executor_demo() -> None:
    await compare_approaches(no_threading_execution_pool, yes_threading_execution_pool)


if __name__ == "__main__":
    asyncio.run(thread_pool_executor_demo())
