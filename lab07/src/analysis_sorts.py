import random
import time
import matplotlib.pyplot as plt

from lab04.src.sorts import quick_sort, merge_sort
from heapsort import heapsort


def measure_time(sort_func, data: list[int]) -> float:
    start = time.perf_counter()
    sort_func(data)
    return time.perf_counter() - start


def compare_sorts():
    sizes = [100, 300, 500, 1000, 2000]

    quick_times = []
    merge_times = []
    heap_times = []

    for n in sizes:
        data = [random.randint(0, 100000) for _ in range(n)]

        quick_times.append(measure_time(quick_sort, data))
        merge_times.append(measure_time(merge_sort, data))
        heap_times.append(measure_time(heapsort, data))

        print(f"n={n}: "
              f"Quick={quick_times[-1]:.6f}s, "
              f"Merge={merge_times[-1]:.6f}s, "
              f"Heap={heap_times[-1]:.6f}s")

    plt.figure()
    plt.plot(sizes, quick_times, marker='o', label='QuickSort')
    plt.plot(sizes, merge_times, marker='o', label='MergeSort')
    plt.plot(sizes, heap_times, marker='o', label='HeapSort')

    plt.xlabel("Количество элементов")
    plt.ylabel("Время сортировки (сек)")
    plt.title("Сравнение алгоритмов сортировки")
    plt.legend()
    plt.grid()

    plt.savefig("../results/sorting_comparison.png")
    plt.show()


if __name__ == "__main__":
    compare_sorts()
