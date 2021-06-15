import asyncio
from threading import Thread
from typing import List

from typing_extensions import Literal

from helpers import blocking_sync_function_with_list, compare_approaches

SLEEP_TIME = 1
NUM_OPS = 4

DataList = List[Literal[1]]


def no_threading() -> None:
    data: DataList = []
    [blocking_sync_function_with_list(SLEEP_TIME, data) for _ in range(NUM_OPS)]


def yes_threading() -> None:
    data: DataList = []
    threads = [
        Thread(
            target=blocking_sync_function_with_list,
            args=(
                SLEEP_TIME,
                data,
            ),
            daemon=True,
        )
        for _ in range(NUM_OPS)
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


async def threading_demo() -> None:
    await compare_approaches(no_threading, yes_threading)


if __name__ == "__main__":
    asyncio.run(threading_demo())
