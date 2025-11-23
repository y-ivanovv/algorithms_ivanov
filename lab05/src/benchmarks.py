import random
import string
from time import perf_counter

from hash_table_chaining import HashTableChaining
from hash_table_open_addressing import HashTableLinear, HashTableDoubleHashing


def random_key(length: int = 8) -> str:
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def run_benchmark(table_class, load_factor: float, table_size: int = 7919):
    table = table_class(table_size)

    target_count = int(table_size * load_factor)

    keys = [random_key() for _ in range(target_count)]

    for key in keys:
        table.insert(key, 123)

    test_keys = random.sample(keys, min(200, len(keys)))

    start = perf_counter()
    for key in test_keys:
        table.search(key)
    end = perf_counter()

    return (end - start) / len(test_keys)


def main():
    load_factors = [0.1, 0.5, 0.7, 0.9]
    classes = [
        ("Chaining", HashTableChaining),
        ("Linear Probing", HashTableLinear),
        ("Double Hashing", HashTableDoubleHashing),
    ]

    for name, cls in classes:
        print(f"\n{name}")
        for lf in load_factors:
            t = run_benchmark(cls, lf)
            print(f"  load={lf:.1f} → time={t:.8f}s")


if __name__ == "__main__":
    main()
