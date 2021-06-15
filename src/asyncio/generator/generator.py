from typing import Generator, List


def fib(n: int) -> List[int]:
    numbers = []
    current, nxt = 0, 1
    while len(numbers) < n:
        current, nxt = nxt, current + nxt
        numbers.append(current)
    return numbers


# if you're looking for a certain condition to be met (e.g. two primes > 1000) you have no idea how many to return in list

# a good approach is waiting for the consumer of the sequence to decide when it's had enough


def fib_generator() -> Generator[int, None, None]:
    current, nxt = 0, 1
    while True:
        current, nxt = nxt, current + nxt
        yield current


if __name__ == "__main__":
    result = fib_generator()
    for n in result:
        print(n, end=", ")
        if n > 10000:
            break
