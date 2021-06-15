# Course summary

> Asynchrony, in computer programming, refers to the occurence of events independent of the main program flow and ways to deal with such events

## Topics

1. Why async and when?
2. async and await (asyncio)

- Python keywords in the asyncio module

3. Multi-threaded parallelism

- Sometimes productive, but sometimes not productive because of the GIL
- Python has two types of parallelism: threaded-based parallelism and process-based parallelism. This is because of the GIL.
- Threaded-bsaed parallelism is great for awaiting a database or file-system, but multi-processing is best for spreading out computational work.

4. Thread safety

- Need to think about thread safety when writing multi-threaded code
- Need to prevent race-conditions that will allow code to see invalid data or corrupt data structures
- Need to prevent deadlocks from freezing up program

5. Multi-process parallelism
6. Execution pools

- Execution pools help unify multi-threading and multi-processing so that we don't need to worry about their APIs.

7. Extending async patterns

- Showing how libraries can extend asynchrony to make great things happen

8. Async web frameworks

- Django, flask, pyramid do not support any form of asynchrony on the web

9. Parallelism in C with Cython

- Cython bridges the gap between C and Python to unlock C's parallelism in the python interpreter

## Asynchronity in Python

Do more at once:

- Asyncio
  - Introduced in Python 3.4
  - Async and await keywords introduced in Python 3.5
  - Basic idea: waiting on something? then go do something else
- Threading
  - Threads are harder to coordinate and to deal with error handling, but are an option for doing more at once
  - In some programming languages, threads can be used to do things faster, but in Python the GIL makes this not possible

Do more faster:

- Multiprocessing
  - The GIL is a process-level thing, we can still spawn off subprocesses to take advantage of computational cores to accomplish some work faster
- C / Cython
  - C can be used to do multi-threaded things (and do more at once, but less emphasis there)

Libraries to help do these things easier:

- Trio
- Unsync

## The GIL in Python

- Global Interpreter Lock
- The GIL is a thread-safety feature for memory management that allows the reference counting (how Python primarily manages memory) is faster and easier --> this makes single-threaded Python faster than it would otherwise be
- The GIL means only one thread (or step) of execution can run at the same time --> Python processes instructions one at a time, no matter where they come from
