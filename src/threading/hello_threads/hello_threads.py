import time
import threading


def main():
    threads = [
        threading.Thread(target=greeter, args=("Michael", 5), daemon=True),
        threading.Thread(target=greeter, args=("Sarah", 5), daemon=True),
        threading.Thread(target=greeter, args=("Steve", 1), daemon=True),
        threading.Thread(target=greeter, args=("Zoe", 11), daemon=True),
    ]
    [t.start() for t in threads]
    print("This is other work.")
    print(2 * 2)
    [t.join(timeout=1) for t in threads]
    print("Done.")


def greeter(name: str, times: int):
    for n in range(times):
        print(f"Hello there {name}.", n)
        time.sleep(0.5)


if __name__ == "__main__":
    main()
