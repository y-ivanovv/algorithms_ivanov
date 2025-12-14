import random
import time
import matplotlib.pyplot as plt
from heap import Heap


def measure_build_methods(n: int):
    data = list(range(n))
    random.shuffle(data)

    heap1 = Heap()
    start = time.perf_counter()
    for x in data:
        heap1.insert(x)
    t_insert = time.perf_counter() - start

    heap2 = Heap()
    start = time.perf_counter()
    heap2.build_heap(data)
    t_build = time.perf_counter() - start

    return t_insert, t_build


def experiment():
    sizes = [100, 500, 1000, 3000]
    insert_times = []
    build_times = []

    for n in sizes:
        t1, t2 = measure_build_methods(n)
        insert_times.append(t1)
        build_times.append(t2)

    plt.plot(sizes, insert_times, label="Последовательная вставка")
    plt.plot(sizes, build_times, label="build_heap")
    plt.xlabel("Размер массива")
    plt.ylabel("Время (сек)")
    plt.legend()
    plt.grid()

    plt.savefig("../results/heaps_comparison.png")
    plt.show()


if __name__ == "__main__":
    experiment()
