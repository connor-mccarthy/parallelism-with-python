import asyncio
from concurrent.futures import Future
from concurrent.futures.process import ProcessPoolExecutor as PoolExecutor
from typing import List

from helpers import compare_approaches, computationally_expensive_function

N = 1_000_000
N_ITERS = 10


def no_multiprocessing_execution_pool() -> None:
    [computationally_expensive_function(n=N) for _ in range(N_ITERS)]


def yes_multiprocessing_execution_pool() -> None:
    with PoolExecutor() as executor:
        responses: List[Future] = [  # noqa: F841
            executor.submit(computationally_expensive_function, N)
            for _ in range(N_ITERS)
        ]


async def multiprocessing_execution_pool_demo() -> None:
    await compare_approaches(
        no_multiprocessing_execution_pool, yes_multiprocessing_execution_pool
    )


if __name__ == "__main__":
    asyncio.run(multiprocessing_execution_pool_demo())
