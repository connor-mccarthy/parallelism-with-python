import datetime
import math
import multiprocessing
import threading


# threading can't speed this up because it's bound by computation
def main() -> None:
    do_math(1)

    t0 = datetime.datetime.now()

    n_processors = multiprocessing.cpu_count()
    threads = [
        threading.Thread(target=do_math, args=(get_args(n, n_processors)), daemon=True)
        for n in range(1, n_processors + 1)
    ]

    [thread.start() for thread in threads]
    [thread.join() for thread in threads]

    dt = datetime.datetime.now() - t0
    print("Done in {:,.2f} sec.".format(dt.total_seconds()))


def get_args(n: int, n_processors: int):
    return (30_000_000 * (n + 1) / n_processors), (30_000_000 * n / n_processors)


def do_math(start=0, num=10):
    pos = start
    k_sq = 1_000 * 1_000
    while pos < num:
        pos += 1
        math.sqrt((pos - k_sq) * (pos - k_sq))


if __name__ == "__main__":
    main()
