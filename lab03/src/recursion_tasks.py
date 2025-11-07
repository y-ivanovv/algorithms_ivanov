import os


def binary_search_recursive(arr: list, target: int, left: int = 0, right: int = None) -> int:
    """
    Рекурсивный бинарный поиск элемента в отсортированном массиве.

    Сложность: O(log n)
    Глубина рекурсии: O(log n)
    """
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = (left + right) // 2
    guess = arr[mid]

    if guess == target:
        return mid
    elif guess > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, right)


def traverse_directory(path: str, indent: int = 0):
    """
    Рекурсивный обход файлов и папок, начиная с указанного пути.
    Выводит древовидную структуру каталога.

    Сложность: O(n), где n — количество файлов/папок
    Глубина рекурсии: равна глубине вложенности директорий
    """
    if not os.path.exists(path):
        print("Путь не найден:", path)
        return

    items = os.listdir(path)

    for item in items:
        full_path = os.path.join(path, item)
        print(" " * indent + ("📂 " if os.path.isdir(full_path) else "📄 ") + item)
        if os.path.isdir(full_path):
            traverse_directory(full_path, indent + 4)


def hanoi(n: int, source: str, target: str, auxiliary: str, moves: list = None) -> list:
    """
    Рекурсивное решение задачи Ханойских башен.
    Перемещает n дисков с source на target, используя auxiliary как вспомогательный стержень.

    Сложность: O(2^n)
    Глубина рекурсии: O(n)
    """
    if moves is None:
        moves = []

    if n == 1:
        moves.append(f"Переместить диск 1 со стержня {source} на стержень {target}")
        return moves

    hanoi(n - 1, source, target, auxiliary, moves)
    moves.append(f"Переместить диск {n} со стержня {source} на стержень {target}")
    hanoi(n - 1, source, target, auxiliary, moves)

    return moves


if __name__ == "__main__":
    print("Рекурсивный бинарный поиск:")
    data = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7
    index = binary_search_recursive(data, target)
    print(f"Искомый элемент {target} найден на позиции {index}")

    print("\nРекурсивный обход файловой системы:")
    test_path = ".."
    traverse_directory(test_path)

    print("\nХанойские башни (n = 3)")
    moves = hanoi(3, "A", "C", "B")
    for step in moves:
        print(step)
    print(f"Всего перемещений: {len(moves)} (ожидается 2^3 - 1 = 7)")
