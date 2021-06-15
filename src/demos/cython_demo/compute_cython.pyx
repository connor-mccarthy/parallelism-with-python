from libc import math

def computationally_expensive_function_cython(n: cython.int = 1_000_000) -> None:
    start = 1
    pos = start
    k_sq = 1000 * 1000
    while pos < n:
        pos += 1
        math.sqrt((pos - k_sq) * (pos - k_sq))
