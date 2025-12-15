import random
import string
from time import perf_counter
import matplotlib.pyplot as plt

from greedy_algorithms import greedy_knapsack_01, huffman_coding, print_huffman_tree


def knapsack_01(capacity, items):
    """
    Точный 0-1 рюкзак (DP).
    Сложность: O(n * capacity)
    """
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        value, weight = items[i - 1]
        for w in range(capacity + 1):
            if weight <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - weight] + value
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


def compare_knapsack():
    items = [(60, 10), (100, 20), (120, 30)]
    capacity = 50

    greedy = greedy_knapsack_01(capacity, items)
    exact = knapsack_01(capacity, items)

    print("=== Сравнение рюкзаков ===")
    print(f"Непрерывный (жадный): {greedy}")
    print(f"0-1 (точный):        {exact}")
    print()


def generate_freq(n):
    freq = {}
    for _ in range(n):
        c = random.choice(string.ascii_lowercase[:6])
        freq[c] = freq.get(c, 0) + 1
    return freq


def huffman_experiment():
    sizes = [100, 500, 1000, 3000, 5000]
    times = []

    for size in sizes:
        freq = generate_freq(size)
        start = perf_counter()
        huffman_coding(freq)
        end = perf_counter()
        times.append(end - start)

        print(f"Размер: {size:5d} | Время: {times[-1]:.6f} сек")

    plt.figure()
    plt.plot(sizes, times, marker='o')
    plt.xlabel("Размер входных данных")
    plt.ylabel("Время работы (сек)")
    plt.title("Время работы алгоритма Хаффмана")
    plt.grid()
    plt.show()


def visualize_huffman_tree():
    freq = {
        'a': 5,
        'b': 9,
        'c': 12,
        'd': 13,
        'e': 16,
        'f': 45
    }

    root, codes = huffman_coding(freq)

    print("=== Коды Хаффмана ===")
    for k, v in codes.items():
        print(f"{k}: {v}")

    print("\n=== Дерево Хаффмана ===")
    print_huffman_tree(root)
    print()


def main():
    compare_knapsack()
    visualize_huffman_tree()
    huffman_experiment()


if __name__ == "__main__":
    main()
