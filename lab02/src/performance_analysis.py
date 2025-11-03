import timeit
import matplotlib.pyplot as plt


pc_info = """
Характеристики ПК для тестирования:
- Процессор: 4 ядра
- Оперативная память: 16 ГБ
- ОС: Linux Mint
- Python: 3.13.7
"""


def measure_insert_start_list(n: int) -> float:
    """Измерение времени вставки n элементов в начало списка (list).
    Каждая операция insert(0, x) имеет сложность O(n).
    """
    setup_code = f"arr = list(range({n}))"
    test_code = "for _ in range(len(arr)): arr.pop(0)"
    return timeit.timeit(stmt=test_code, setup=setup_code, number=1)


def measure_insert_start_linkedlist(n: int) -> float:
    """Измерение времени вставки n элементов в начало связного списка (LinkedList).
    Каждая операция insert_at_start() имеет сложность O(1).
    """
    setup_code = "from linked_list import LinkedList\nll = LinkedList()"
    test_code = f"for i in range({n}): ll.insert_at_start(i)"
    return timeit.timeit(stmt=test_code, setup=setup_code, number=1)


def measure_queue_list(n: int) -> float:
    """Имитация очереди на list.
    Операции pop(0) имеют сложность O(n).
    """
    setup_code = f"arr = list(range({n}))"
    test_code = "for _ in range(len(arr)): arr.pop(0)"
    return timeit.timeit(stmt=test_code, setup=setup_code, number=1)


def measure_queue_deque(n: int) -> float:
    """Имитация очереди на deque.
    Операции popleft() выполняются за O(1).
    """
    setup_code = f"from collections import deque\nq = deque(range({n}))"
    test_code = "for _ in range(len(q)): q.popleft()"
    return timeit.timeit(stmt=test_code, setup=setup_code, number=1)


def run_experiments():
    """Запуск всех тестов и построение графиков."""
    sizes = [100, 500, 1000, 5000, 10000]

    list_insert_times = []
    linked_insert_times = []
    list_queue_times = []
    deque_queue_times = []

    for n in sizes:
        print(f"Тестируем размер: {n}")
        list_insert_times.append(measure_insert_start_list(n))
        linked_insert_times.append(measure_insert_start_linkedlist(n))
        list_queue_times.append(measure_queue_list(n))
        deque_queue_times.append(measure_queue_deque(n))

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, list_insert_times, 'o-', label='list.insert(0, x) — O(n)')
    plt.plot(sizes, linked_insert_times, 'o-', label='LinkedList.insert_at_start() — O(1)')
    plt.xlabel('Количество элементов (n)')
    plt.ylabel('Время выполнения (сек)')
    plt.title('Сравнение вставки в начало: list vs LinkedList')
    plt.legend()
    plt.grid(True)
    plt.savefig('../results/insert_comparison.png', dpi=300, bbox_inches='tight')

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, list_queue_times, 'o-', label='list.pop(0) — O(n)')
    plt.plot(sizes, deque_queue_times, 'o-', label='deque.popleft() — O(1)')
    plt.xlabel('Количество элементов (n)')
    plt.ylabel('Время выполнения (сек)')
    plt.title('Сравнение производительности очереди: list vs deque')
    plt.legend()
    plt.grid(True)
    plt.savefig('../results/queue_comparison.png', dpi=300, bbox_inches='tight')

    print("\nГрафики сохранены:")
    print("- insert_comparison.png")
    print("- queue_comparison.png")


if __name__ == "__main__":
    run_experiments()
    print(pc_info)
