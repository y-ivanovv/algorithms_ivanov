import random
import time
import matplotlib.pyplot as plt
from binary_search_tree import BinarySearchTree


def measure_search(tree, values, repeats):
    """
    Измеряет время поиска элементов в дереве.
    """
    t0 = time.perf_counter()
    for _ in range(repeats):
        for v in values:
            tree.search(v)
    return time.perf_counter() - t0


def build_balanced_tree(n):
    values = list(range(n))
    random.shuffle(values)

    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)

    return tree, values


def build_degenerate_tree(n):
    values = list(range(n))

    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)

    return tree, values


def experiment_compare_bst():
    sizes = [100, 300, 900]
    balanced_times = []
    degenerate_times = []
    balanced_heights = []
    degenerate_heights = []

    for n in sizes:
        print(f"\n=== Тест размера {n} ===")

        bal_tree, bal_values = build_balanced_tree(n)
        sample = random.sample(bal_values, min(20, len(bal_values)))

        t_bal = measure_search(bal_tree, sample, repeats=1000)
        h_bal = bal_tree.height()
        balanced_times.append(t_bal)
        balanced_heights.append(h_bal)

        print(f"Сбалансированное:  поиск 1000 раз = {t_bal:.6f} сек, высота = {h_bal}")

        deg_tree, deg_values = build_degenerate_tree(n)
        sample2 = random.sample(deg_values, min(20, len(deg_values)))

        t_deg = measure_search(deg_tree, sample2, repeats=1000)
        h_deg = deg_tree.height()
        degenerate_times.append(t_deg)
        degenerate_heights.append(h_deg)

        print(f"Вырожденное:      поиск 1000 раз = {t_deg:.6f} сек, высота = {h_deg}")

    plt.figure(figsize=(10, 5))
    plt.plot(sizes, balanced_times, marker="o", label="Сбалансированное дерево")
    plt.plot(sizes, degenerate_times, marker="o", label="Вырожденное дерево")
    plt.xlabel("Размер дерева")
    plt.ylabel("Время поиска (сек)")
    plt.title("Время поиска в зависимости от размера дерева")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig('../results/time_comparison.png', dpi=300, bbox_inches='tight')

    plt.figure(figsize=(10, 5))
    plt.plot(sizes, balanced_heights, marker="o", label="Сбалансированное дерево")
    plt.plot(sizes, degenerate_heights, marker="o", label="Вырожденное дерево")
    plt.xlabel("Размер дерева")
    plt.ylabel("Высота дерева")
    plt.title("Рост высоты BST: сравнение")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig('../results/height_comparison.png', dpi=300, bbox_inches='tight')


if __name__ == "__main__":
    experiment_compare_bst()
