from typing import Any, Optional
from hash_functions import hash_djb2, hash_poly


deleted = object()


class HashTableLinear:
    """
    Хеш-таблица с открытой адресацией (линейное пробирование)
    """

    def __init__(self, size: int = 16, hash_func=hash_djb2):
        self.size = size
        self.table = [None] * size
        self.hash_func = hash_func
        self.count = 0

    def _index(self, key: str) -> int:
        return self.hash_func(key) % self.size

    def insert(self, key: str, value: Any) -> None:
        index = self._index(key)

        for _ in range(self.size):
            if self.table[index] is None or self.table[index] is deleted:
                self.table[index] = (key, value)
                self.count += 1
                return

            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return

            index = (index + 1) % self.size

        raise RuntimeError("HashTableLinear overflow")

    def search(self, key: str) -> Optional[Any]:
        index = self._index(key)

        for _ in range(self.size):
            if self.table[index] is None:
                return None

            if self.table[index] is not deleted and self.table[index][0] == key:
                return self.table[index][1]

            index = (index + 1) % self.size

        return None

    def delete(self, key: str) -> bool:
        index = self._index(key)

        for _ in range(self.size):
            if self.table[index] is None:
                return False

            if self.table[index] is not deleted and self.table[index][0] == key:
                self.table[index] = deleted
                self.count -= 1
                return True

            index = (index + 1) % self.size

        return False


class HashTableDoubleHashing(HashTableLinear):
    """
    Хеш-таблица с двойным хешированием.
    Наследуем частично поведение линейной, но меняем probing.
    """

    def __init__(self, size: int = 16, hash_func=hash_djb2, hash_func_2=hash_poly):
        super().__init__(size, hash_func)
        self.hash_func_2 = hash_func_2

    def _step(self, key: str) -> int:
        return self.hash_func_2(key) % (self.size - 1) + 1

    def insert(self, key: str, value: Any) -> None:
        index = self._index(key)
        step = self._step(key)

        for _ in range(self.size):
            if self.table[index] is None or self.table[index] is deleted:
                self.table[index] = (key, value)
                self.count += 1
                return

            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return

            index = (index + step) % self.size

        raise RuntimeError("HashTableDoubleHashing overflow")
