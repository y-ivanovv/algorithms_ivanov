import random
import string
from hash_functions import hash_sum, hash_poly, hash_djb2


def random_string(length: int = 10) -> str:
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


def measure_collisions(hash_func, table_size: int, num_keys: int = 5000) -> list[int]:
    buckets = [0] * table_size

    for _ in range(num_keys):
        key = random_string()
        idx = hash_func(key) % table_size
        buckets[idx] += 1

    return buckets


def main():
    table_size = 1000
    num_keys = 5000

    functions = {
        "hash_sum": hash_sum,
        "hash_poly": hash_poly,
        "hash_djb2": hash_djb2,
    }

    results = {}

    for name, func in functions.items():
        print(f"\n=== {name} ===")
        buckets = measure_collisions(func, table_size, num_keys)
        results[name] = buckets

        empty = sum(1 for b in buckets if b == 0)
        max_bucket = max(buckets)
        total_collisions = sum(b - 1 for b in buckets if b > 1)

        print(f"Пустых бакетов: {empty}/{table_size}")
        print(f"Максимальная загрузка одного бакета: {max_bucket}")
        print(f"Количество коллизий: {total_collisions}")

    return results


if __name__ == "__main__":
    main()
