import time
import matplotlib.pyplot as plt

from recursion import fibonacci


def fibonacci_memo(n: int, cache: dict=None) -> int:
    """Рекурсивное вычисление числа Фибоначчи с мемоизацией.
    Временная сложность: O(n)
    Глубина рекурсии: O(n)
    """
    if cache is None:
        cache = {}

    if n in cache:
        return cache[n]

    if n <= 1:
        cache[n] = n
    else:
        cache[n] = fibonacci_memo(n - 1, cache) + fibonacci_memo(n - 2, cache)

    return cache[n]


def timer(func, arr: list) -> list:
    """Измеряет время выполнения функции для заданных n."""
    times = []

    for n in arr:
        start = time.perf_counter()
        func(n)
        end = time.perf_counter()
        times.append((end - start) * 1000)

    return times


if __name__ == "__main__":
    print("Сравнение производительности рекурсии и мемоизации:")

    arr = [5, 10, 15, 20, 25, 30, 35]
    print("\nВычисляем времена выполнения (в миллисекундах):\n")

    naive_times = timer(fibonacci, arr)
    memo_times = timer(fibonacci_memo, arr)

    print("{:>5} {:>20} {:>20}".format("n", "Наивная рекурсия", "С мемоизацией"))
    print("-" * 50)
    for n, t1, t2 in zip(arr, naive_times, memo_times):
        print(f"{n:>5} {t1:>20.4f} {t2:>20.4f}")

    plt.figure(figsize=(10, 6))
    plt.plot(arr, naive_times, 'o-', label='Наивная рекурсия O(2^n)')
    plt.plot(arr, memo_times, 's-', label='Мемоизация O(n)')
    plt.xlabel("n — номер числа Фибоначчи")
    plt.ylabel("Время выполнения (мс)")
    plt.title("Сравнение рекурсивного и мемоизированного вычисления Фибоначчи")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('../results/recursion.png', dpi=300, bbox_inches='tight')
