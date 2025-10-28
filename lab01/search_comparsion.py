import time
import random
import matplotlib.pyplot as plt


def linear_search(arr, target):
    """Линейный поиск элемента в массиве.
    Сложность: O(N)
    """
    for i in range(len(arr)):  # O(N)
        if arr[i] == target:   # O(1)
            return i           # O(1)
    return None                # O(1)
# Общая сложность: O(N)


def binary_search(arr, target):
    """Бинарный поиск элемента в отсортированном массиве.
    Сложность: O(log N)
    """
    left = 0                  # O(1)
    right = len(arr) - 1      # O(1)
    while left <= right:      # O(log N)
        mid = (left + right) // 2  # O(1)
        guess = arr[mid]           # O(1)
        if guess < target:         # O(1)
            left = mid + 1         # O(1)
        elif guess > target:       # O(1)
            right = mid - 1        # O(1)
        else:
            return mid             # O(1)
    return None                    # O(1)
# Общая сложность: O(log N)


def timer(f, arr, target, repeats=10):
    """Измеряет среднее время выполнения функции в миллисекундах."""
    total = 0
    for _ in range(repeats):
        start = time.perf_counter()
        f(arr, target)
        end = time.perf_counter()
        total += (end - start)
    return (total / repeats) * 1000


pc_info = """
Характеристики ПК для тестирования:
- Процессор: 4 ядра
- Оперативная память: 16 ГБ
- ОС: Linux Mint
- Python: 3.13.7
"""
print(pc_info)


sizes = [1000, 5000, 10000, 50000, 100000, 500000, 1000000]
algorithms = {
    "Линейный поиск O(N)": linear_search,
    "Бинарный поиск O(log N)": binary_search
}

cases = {
    "Первый элемент": lambda arr: arr[0],
    "Последний элемент": lambda arr: arr[-1],
    "Случайный элемент": lambda arr: random.choice(arr),
    "Отсутствующий элемент": lambda arr: max(arr) + 1
}

results = {alg: [] for alg in algorithms}

print("Замеры времени выполнения:")
print("{:>10} {:>25} {:>25} {:>15}".format("Размер", "Тип элемента", "Алгоритм", "Время (мс)"))
print("-" * 80)

for size in sizes:
    arr = sorted(random.sample(range(size * 2), size))
    for case_name, get_target in cases.items():
        target = get_target(arr)
        for alg_name, alg_func in algorithms.items():
            exec_time = timer(alg_func, arr, target)
            results[alg_name].append((size, exec_time))
            print("{:>10} {:>25} {:>25} {:>15.4f}".format(size, case_name, alg_name, exec_time))

averaged_results = {}
for alg_name, data in results.items():
    by_size = {}
    for size, exec_time in data:
        by_size.setdefault(size, []).append(exec_time)
    averaged_results[alg_name] = [(size, sum(times)/len(times)) for size, times in by_size.items()]


plt.figure(figsize=(10, 6))
for alg_name, data in averaged_results.items():
    sizes_plot = [x for x, _ in data]
    times_plot = [t for _, t in data]
    plt.plot(sizes_plot, times_plot, 'o-', label=alg_name)
plt.xlabel("Размер массива (N)")
plt.ylabel("Время выполнения (мс)")
plt.title("Сравнение линейного и бинарного поиска\nСложности: O(N) и O(log N)")
plt.legend()
plt.grid(True)
plt.savefig("search_time_linear_scale.png", dpi=300, bbox_inches='tight')

plt.figure(figsize=(10, 6))
for alg_name, data in averaged_results.items():
    sizes_plot = [x for x, _ in data]
    times_plot = [t for _, t in data]
    plt.plot(sizes_plot, times_plot, 'o-', label=alg_name)
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Размер массива (N) [лог]")
plt.ylabel("Время выполнения (мс) [лог]")
plt.title("Логарифмическая шкала: подтверждение O(N) и O(log N)")
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.savefig("search_time_log_scale.png", dpi=300, bbox_inches='tight')
