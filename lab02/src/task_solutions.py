from collections import deque


def is_balanced_brackets(s: str) -> bool:
    """
    Проверяет, сбалансированы ли скобки в строке.
    Используется стек (list), принцип LIFO.
    Сложность: O(n) по времени, O(n) по памяти.
    """
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return not stack


def printer_queue(tasks: list):
    """
    Симулирует обработку заданий на печать.
    Используется очередь (deque), принцип FIFO.
    Сложность: O(n) по времени, O(n) по памяти.
    """
    queue = deque(tasks)
    step = 1

    while queue:
        current = queue.popleft()
        print(f"Шаг {step}: печатается '{current}'")
        step += 1


def is_palindrome(s: str) -> bool:
    """
    Проверяет, является ли строка палиндромом.
    Используется двусторонняя очередь (deque),
    чтобы эффективно сравнивать с обоих концов.
    Сложность: O(n) по времени, O(n) по памяти.
    """
    d = deque([char.lower() for char in s if char.isalnum()])

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False

    return True


if __name__ == "__main__":
    print("=== Проверка сбалансированных скобок ===")
    tests = ["{[()]}", "{[(])}", "((()))", "[({})]", "({[})"]
    for t in tests:
        print(f"{t:10} -> {is_balanced_brackets(t)}")

    print("\n=== Симуляция очереди печати ===")
    printer_queue(["Документ1", "Фото", "Отчет.pdf"])

    print("\n=== Проверка палиндромов ===")
    words = ["Аргентина манит негра", "Level", "Python", "Madam"]
    for w in words:
        print(f"{w:25} -> {is_palindrome(w)}")
