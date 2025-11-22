import matplotlib.pyplot as plt
from collision_analysis import measure_collisions
from hash_functions import hash_sum, hash_poly, hash_djb2


def main():
    table_size = 1000
    num_keys = 5000

    # считаем распределения
    buckets_simple = measure_collisions(hash_sum, table_size, num_keys)
    buckets_poly = measure_collisions(hash_poly, table_size, num_keys)
    buckets_djb2 = measure_collisions(hash_djb2, table_size, num_keys)

    x = range(table_size)

    plt.figure(figsize=(14, 6))

    plt.bar(x, buckets_simple, alpha=0.5, label="hash_sum")
    plt.bar(x, buckets_poly, alpha=0.5, label="hash_poly")
    plt.bar(x, buckets_djb2, alpha=0.5, label="hash_djb2")

    plt.title("Сравнение распределения коллизий разных хеш-функций")
    plt.xlabel("Бакет")
    plt.ylabel("Количество элементов")
    plt.legend()
    plt.tight_layout()
    plt.savefig('../results/collisions.png', dpi=300, bbox_inches='tight')


if __name__ == "__main__":
    main()
