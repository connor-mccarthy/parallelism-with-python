import asyncio
import multiprocessing
import os
import sys

directory_one_level_up = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(directory_one_level_up)

from helpers import compare_approaches  # noqa: E402

if __name__ == "__main__":
    from compute_cython import computationally_expensive_function_cython
    from compute_python import computationally_expensive_function_python
else:
    from .compute_cython import computationally_expensive_function_cython
    from .compute_python import computationally_expensive_function_python

N = 10_000_000


def no_cython():
    computationally_expensive_function_python(n=N)


def yes_cython():

    n = N
    pool = multiprocessing.Pool()
    processor_count = multiprocessing.cpu_count()
    data = []
    for n in range(1, processor_count + 1):
        result = pool.apply_async(
            computationally_expensive_function_cython,
            (
                N * (n - 1) / processor_count,
                N * n / processor_count,
            ),
        )
        data.append(result)

    pool.close()
    pool.join()


async def cython_demo() -> None:
    await compare_approaches(no_cython, yes_cython)


if __name__ == "__main__":
    asyncio.run(cython_demo())
