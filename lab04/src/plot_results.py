import matplotlib.pyplot as plt
from performance_test import benchmark
from generate_data import random_array, sorted_array, reversed_array, almost_sorted_array
from sorts import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort


def measure_times(sort_functions, data_generators, sizes):
    """
    Возвращает словарь вида:
    results[sort_name][data_type] = [(n, time), ...]
    """
    results = {}

    for sort_name in sort_functions:
        results[sort_name] = {}

        for data_type in data_generators:
            results[sort_name][data_type] = []

            for n in sizes:
                data = data_generators[data_type](n)

                t = benchmark(sort_functions[sort_name], data)
                results[sort_name][data_type].append((n, t))

    return results


def plot_for_data_type(results, data_type, sizes):
    """
    График: время от размера массива для одного типа данных.
    """
    plt.figure(figsize=(10, 6))

    for sort_name, data_variants in results.items():
        times = [t for (_, t) in data_variants[data_type]]
        plt.plot(sizes, times, marker="o", label=sort_name)

    plt.title(f"Сравнение алгоритмов сортировки ({data_type})")
    plt.xlabel("Размер массива")
    plt.ylabel("Время (сек)")
    plt.legend()
    plt.grid(True)
    plt.savefig('../results/sort.png', dpi=300, bbox_inches='tight')


def plot_for_fixed_size(results, data_type_list, fixed_size):
    """
    График: время для разных типов данных при одном фиксированном размере.
    """
    plt.figure(figsize=(10, 6))

    algorithms = list(results.keys())
    x = range(len(algorithms))

    for data_type in data_type_list:
        times = [
            next((t for (n, t) in results[alg][data_type] if n == fixed_size), None)
            for alg in algorithms
        ]

        plt.plot(x, times, marker="o", label=data_type)

    plt.xticks(x, algorithms, rotation=45)
    plt.title(f"Сравнение типов данных (n={fixed_size})")
    plt.xlabel("Алгоритм сортировки")
    plt.ylabel("Время (сек)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig('../results/data.png', dpi=300, bbox_inches='tight')


def main():
    sizes = [100, 1000, 5000]

    sort_functions = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
    }

    data_generators = {
        "random": random_array,
        "sorted": sorted_array,
        "reversed": reversed_array,
        "almost_sorted": almost_sorted_array,
    }

    print("Замеряем время выполнения сортировок...")
    results = measure_times(sort_functions, data_generators, sizes)

    for data_type in data_generators:
        plot_for_data_type(results, data_type, sizes)

    plot_for_fixed_size(results, list(data_generators.keys()), fixed_size=1000)


if __name__ == "__main__":
    main()
