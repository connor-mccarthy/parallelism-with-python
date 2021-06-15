# Why do we need additional libraries?

- Executing an async functino outside of an existing event loop is troublesome (think: passing event loops through deep nesting of async)
- `asyncio.Futures` is not thread safe
- `concurrent.Future`s cannot be directly awaited
- `Future.result()` is a blocking operation within an event loop
- `asyncio.Future.result()` will throw an exception if the future is not done (think: resolved)
- async functions always execute in the asyncio loop (not thread or process backed)
- Cancellation and timeouts are tricky in threads and processes
- Thread local storage doesn't work for asyncio concurrency
- Testing concurrent code can be very tricky

## `unsync` library

- Solves the problem of mixed-mode parallelism: wanting to use asyncio, multithreading, and multiprocessing at the same time or in different parts of your application
- Uses an `@unsync` decorator to abstract away from the event loop, with built-in support for multi-threading and multi-processing
