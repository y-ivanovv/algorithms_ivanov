from typing import Optional


class Heap:
    """
    Универсальная куча (Min-Heap или Max-Heap)
    Реализация на основе массива
    """

    def __init__(self, is_min: bool = True):
        self.data: list[int] = []
        self.is_min: bool = is_min

    def _compare(self, a: int, b: int) -> bool:
        """Сравнение с учетом типа кучи"""
        return a < b if self.is_min else a > b

    def _sift_up(self, index: int):
        """
        Всплытие элемента
        Сложность: O(log n)
        """
        while index > 0:
            parent = (index - 1) // 2
            if self._compare(self.data[index], self.data[parent]):
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break

    def _sift_down(self, index: int):
        """
        Погружение элемента
        Сложность: O(log n)
        """
        size = len(self.data)

        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            best = index

            if left < size and self._compare(self.data[left], self.data[best]):
                best = left
            if right < size and self._compare(self.data[right], self.data[best]):
                best = right

            if best != index:
                self.data[index], self.data[best] = self.data[best], self.data[index]
                index = best
            else:
                break

    def insert(self, value: int):
        """
        Вставка элемента
        Сложность: O(log n)
        """
        self.data.append(value)
        self._sift_up(len(self.data) - 1)

    def extract(self) -> Optional[int]:
        """
        Извлечение корня
        Сложность: O(log n)
        """
        if not self.data:
            return None

        root = self.data[0]
        last = self.data.pop()

        if self.data:
            self.data[0] = last
            self._sift_down(0)

        return root

    def peek(self) -> Optional[int]:
        """
        Просмотр корня
        Сложность: O(1)
        """
        return self.data[0] if self.data else None

    def build_heap(self, array: list[int]):
        """
        Построение кучи из массива
        Сложность: O(n)
        """
        self.data = array[:]
        for i in range(len(self.data) // 2 - 1, -1, -1):
            self._sift_down(i)

    def __len__(self):
        return len(self.data)
