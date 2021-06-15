import asyncio

from helpers import blocking_async_function, blocking_sync_function, compare_approaches

SLEEP_TIME = 1
NUM_OPS = 5


def no_async() -> None:
    [blocking_sync_function(SLEEP_TIME) for _ in range(NUM_OPS)]


async def yes_async() -> None:
    await asyncio.gather(*(blocking_async_function(SLEEP_TIME) for _ in range(NUM_OPS)))


async def async_await_demo() -> None:
    await compare_approaches(no_async, yes_async, async2=True)


if __name__ == "__main__":
    asyncio.run(async_await_demo())
