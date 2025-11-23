from typing import Any, Optional
from hash_functions import hash_djb2


class HashTableChaining:
    """
    Хеш-таблица методом цепочек.
    В каждой ячейке хранится список пар (key, value).
    """

    def __init__(self, size: int = 16, hash_func=hash_djb2):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.hash_func = hash_func
        self.count = 0

    def _index(self, key: str) -> int:
        return self.hash_func(key) % self.size

    def insert(self, key: str, value: Any) -> None:
        index = self._index(key)
        chain = self.table[index]

        for i, (k, v) in enumerate(chain):
            if k == key:
                chain[i] = (key, value)
                return

        chain.append((key, value))
        self.count += 1

    def search(self, key: str) -> Optional[Any]:
        index = self._index(key)
        chain = self.table[index]

        for k, v in chain:
            if k == key:
                return v

        return None

    def delete(self, key: str) -> bool:
        index = self._index(key)
        chain = self.table[index]

        for i, (k, v) in enumerate(chain):
            if k == key:
                del chain[i]
                self.count -= 1
                return True

        return False
