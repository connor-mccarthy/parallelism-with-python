import asyncio
import multiprocessing

from helpers import compare_approaches, computationally_expensive_function

N = 10_000_000


def no_multiprocessing():
    computationally_expensive_function(n=N)


def yes_multiprocessing():
    n = N
    pool = multiprocessing.Pool()
    processor_count = multiprocessing.cpu_count()
    data = []
    for n in range(1, processor_count + 1):
        result = pool.apply_async(
            computationally_expensive_function,
            (
                N * (n - 1) / processor_count,
                N * n / processor_count,
            ),
        )
        data.append(result)

    pool.close()
    pool.join()


async def multiprocessing_demo() -> None:
    await compare_approaches(no_multiprocessing, yes_multiprocessing)


if __name__ == "__main__":
    asyncio.run(multiprocessing_demo())
