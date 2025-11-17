import timeit
from copy import deepcopy
from generate_data import random_array, sorted_array, reversed_array, almost_sorted_array
from sorts import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort


def benchmark(sort_func, data, repeats=3):
    """
    Замеряет время выполнения сортировки.
    Каждый запуск сортирует копию исходного массива.
    """
    return timeit.timeit(lambda: sort_func(deepcopy(data)), number=repeats) / repeats


def run_benchmarks():
    sizes = [100, 1000, 5000]

    data_generators = {
        "random": random_array,
        "sorted": sorted_array,
        "reversed": reversed_array,
        "almost_sorted": almost_sorted_array,
    }

    sort_functions = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
    }

    for size in sizes:
        print(f"\n===== Размер массива: {size} =====\n")

        for data_type, generator in data_generators.items():
            print(f"-- Тип данных: {data_type} --")

            data = generator(size)

            for sort_name, sort_func in sort_functions.items():
                t = benchmark(sort_func, data)
                print(f"{sort_name:15} | {t:.6f} сек")

            print()


if __name__ == "__main__":
    run_benchmarks()
