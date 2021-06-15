import asyncio

from async_await_demo import async_await_demo
from cython_demo import cython_demo
from multiprocessing_demo import multiprocessing_demo
from thread_pool_executor_demo import thread_pool_executor_demo
from threading_demo import threading_demo


async def demostrate_parallel_approaches() -> None:
    # almost all of these are _not_ async, but this is an async function to accomodate the few that are
    parallel_approaches = {
        "Async await": async_await_demo,
        "Multiprocessing": multiprocessing_demo,
        "Multiprocessing with execution pools": multiprocessing_demo,
        "Threading": threading_demo,
        "Threading with execution pools": thread_pool_executor_demo,
        "Cython": cython_demo,
    }
    for k, v in parallel_approaches.items():
        print("")
        print(k)
        await v()


if __name__ == "__main__":
    asyncio.run(demostrate_parallel_approaches())
