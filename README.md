<div align="center">
  <h1>Parallelism with Python</h1>
  <h2>Multithreading, multiprocessing, execution pools, asyncio, and Cython</h2>

<p align="center">

<a href="https://github.com/connor-mccarthy/parallelism-with-python/workflows/build/badge.svg">
    <img src="https://github.com/connor-mccarthy/parallelism-with-python/workflows/build/badge.svg" alt="Python Workflow" />
</a>
<a href="https://img.shields.io/badge/python-3.7.10-blue.svg">
    <img src="https://img.shields.io/badge/python-3.7.10-blue.svg" alt="Python 3.7.10" />
</a>
<a href="https://img.shields.io/badge/code%20style-black-000000.svg">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black" >
</a>
</div>

I went exploring parallelism in Python.

Below are some comparisons benchmarking performance of different parallel programming approaches for solving arbitrary I/O and compute tasks. The tasks vary between approaches (i.e. between async/await and multiprocessing) and are not directly comparable.

Results:

```
Async await
   Slower approach: Finished 'no_async' in 5.0055s
   Faster approach: Finished 'yes_async' in 1.0057s
   Speed improvement 4.98x

Multiprocessing
   Slower approach: Finished 'no_multiprocessing' in 2.1139s
   Faster approach: Finished 'yes_multiprocessing' in 0.1232s
   Speed improvement 17.16x

Multiprocessing with execution pools
   Slower approach: Finished 'no_multiprocessing' in 2.1328s
   Faster approach: Finished 'yes_multiprocessing' in 0.1227s
   Speed improvement 17.39x

Threading
   Slower approach: Finished 'no_threading' in 4.0146s
   Faster approach: Finished 'yes_threading' in 1.0011s
   Speed improvement 4.01x

Threading with execution pools
   Slower approach: Finished 'no_threading_execution_pool' in 4.0097s
   Faster approach: Finished 'yes_threading_execution_pool' in 1.0066s
   Speed improvement 3.98x
```

Note: The speed improvement multipliers will typically be even larger for larger amounts of work, as the "spin-up" time of each approach will make up a smaller fraction of the total work/waiting time. This is a blunt benchmark.

To reproduce:

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/demos/main.py
```
