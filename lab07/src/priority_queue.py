from typing import Any

from lab07.src.heap import Heap


class PriorityQueue:
    """
    Приоритетная очередь на основе Min-Heap
    """

    def __init__(self):
        self.heap = Heap(is_min=True)

    def enqueue(self, item: Any, priority: int):
        """
        Добавление элемента
        Сложность: O(log n)
        """
        self.heap.insert((priority, item))

    def dequeue(self):
        """
        Извлечение элемента с наивысшим приоритетом
        Сложность: O(log n)
        """
        value = self.heap.extract()
        return value[1] if value else None

    def is_empty(self) -> bool:
        return len(self.heap) == 0
