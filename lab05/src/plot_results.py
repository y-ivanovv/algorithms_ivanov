import matplotlib.pyplot as plt
from benchmarks import run_benchmark
from hash_table_chaining import HashTableChaining
from hash_table_open_addressing import HashTableLinear, HashTableDoubleHashing


def main():
    load_factors = [0.1, 0.5, 0.7, 0.9]
    classes = [
        ("Chaining", HashTableChaining),
        ("Linear Probing", HashTableLinear),
        ("Double Hashing", HashTableDoubleHashing),
    ]

    plt.figure(figsize=(10, 6))

    for name, cls in classes:
        times = [run_benchmark(cls, lf) for lf in load_factors]
        plt.plot(load_factors, times, marker="o", label=name)

    plt.xlabel("Коэффициент заполнения")
    plt.ylabel("Среднее время поиска")
    plt.title("Зависимость времени поиска от коэффициента заполнения")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig('../results/time.png', dpi=300, bbox_inches='tight')


if __name__ == "__main__":
    main()
