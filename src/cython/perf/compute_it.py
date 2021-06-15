import datetime
import math


def main() -> None:
    do_math(1)

    t0 = datetime.datetime.now()

    do_math(num=3_000_000)

    dt = datetime.datetime.now() - t0
    print("Done in {:,.2f} sec.".format(dt.total_seconds()))


def do_math(start=0, num=10) -> None:
    pos = start
    k_sq = 1000 * 1000
    while pos < num:
        pos += 1
        dist = math.sqrt((pos - k_sq) * (pos - k_sq))  # noqa: F841


if __name__ == "__main__":
    main()
