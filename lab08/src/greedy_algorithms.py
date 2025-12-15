from heapq import heappush, heappop


def interval_scheduling(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """
    Выбор максимального количества непересекающихся интервалов.
    Жадный выбор: интервал с минимальным временем окончания.

    Сложность: O(n log n) из-за сортировки.
    Корректность: раннее завершение оставляет максимум места
    для последующих интервалов.
    """
    intervals = sorted(intervals, key=lambda x: x[1])
    result = []

    current_end = -1
    for start, end in intervals:
        if start >= current_end:
            result.append((start, end))
            current_end = end

    return result


def greedy_knapsack_01(capacity: int, items: list[tuple[int, int]]) -> int:
    """
    Жадный алгоритм для 0-1 рюкзака.
    items: (value, weight)

    Жадный выбор: максимальная удельная стоимость value / weight.
    Предмет либо берется целиком, либо не берется.

    Сложность: O(n log n)
    Корректность: НЕ гарантирует оптимальное решение для 0-1 рюкзака,
    используется для демонстрации ограничения жадного подхода.
    """
    items = sorted(items, key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0
    remaining_capacity = capacity

    for value, weight in items:
        if weight <= remaining_capacity:
            total_value += value
            remaining_capacity -= weight

    return total_value


class HuffmanNode:
    def __init__(self, freq: int, char: str = None,
                 left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

    def is_leaf(self):
        return self.char is not None


def huffman_coding(freq: dict[str, int]):
    """
    Алгоритм Хаффмана.

    Сложность: O(n log n)
    Корректность: на каждом шаге объединяются
    два символа с минимальной частотой.
    """
    heap = []
    for char, f in freq.items():
        heappush(heap, HuffmanNode(f, char))

    while len(heap) > 1:
        a = heappop(heap)
        b = heappop(heap)
        merged = HuffmanNode(a.freq + b.freq, None, a, b)
        heappush(heap, merged)

    root = heap[0]
    codes = {}

    def build_codes(node, prefix=""):
        if node.is_leaf():
            codes[node.char] = prefix
            return
        build_codes(node.left, prefix + "0")
        build_codes(node.right, prefix + "1")

    build_codes(root)
    return root, codes


def print_huffman_tree(node, indent="", last=True):
    """
    Текстовая визуализация дерева Хаффмана.
    """
    if node is None:
        return

    print(indent, end="")
    if last:
        print("└── ", end="")
        indent += "    "
    else:
        print("├── ", end="")
        indent += "│   "

    if node.is_leaf():
        print(f"'{node.char}' ({node.freq})")
    else:
        print(f"* ({node.freq})")

    print_huffman_tree(node.left, indent, False)
    print_huffman_tree(node.right, indent, True)


def coin_change(amount: int, coins: list[int]) -> dict[int, int]:
    """
    Минимальное количество монет (жадно).
    Работает корректно для стандартных систем монет.

    Сложность: O(n)
    """
    result = {}
    for coin in sorted(coins, reverse=True):
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
    return result


def kruskal_mst(vertices: int, edges: list[tuple[int, int, int]]):
    """
    Алгоритм Краскала (Минимальное остовное дерево).

    Сложность: O(E log E)
    """
    parent = list(range(vertices))

    def find(v):
        while parent[v] != v:
            v = parent[v]
        return v

    def union(a, b):
        parent[find(a)] = find(b)

    edges = sorted(edges, key=lambda x: x[2])
    mst = []

    for u, v, w in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, w))

    return mst


if __name__ == "__main__":
    print("=== Interval Scheduling ===")
    intervals = [
        (1, 4),
        (3, 5),
        (0, 6),
        (5, 7),
        (3, 9),
        (5, 9),
        (6, 10),
        (8, 11)
    ]

    selected = interval_scheduling(intervals)
    print("Выбранные интервалы:", selected)
    print()

    print("=== Жадный 0-1 рюкзак ===")
    items = [
        (60, 10),
        (100, 20),
        (120, 30)
    ]
    capacity = 50

    value = greedy_knapsack_01(capacity, items)
    print("Вместимость:", capacity)
    print("Предметы (ценность, вес):", items)
    print("Жадное решение:", value)
    print()

    print("=== Кодирование Хаффмана ===")
    frequencies = {
        'a': 5,
        'b': 9,
        'c': 12,
        'd': 13,
        'e': 16,
        'f': 45
    }

    root, codes = huffman_coding(frequencies)
    print("Коды Хаффмана:")
    for char, code in codes.items():
        print(f"'{char}': {code}")

    print("\nДерево Хаффмана:")
    print_huffman_tree(root)
    print()

    print("=== Размен монет ===")
    amount = 87
    coins = [50, 10, 5, 2, 1]

    change = coin_change(amount, coins)
    print("Сумма:", amount)
    print("Монеты:", coins)
    print("Размен:", change)
    print()

    print("=== Минимальное остовное дерево (Краскал) ===")
    vertices = 4
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]

    mst = kruskal_mst(vertices, edges)
    print("Рёбра MST:")
    for u, v, w in mst:
        print(f"{u} - {v}, вес = {w}")
