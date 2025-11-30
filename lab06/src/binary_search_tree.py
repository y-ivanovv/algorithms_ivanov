from typing import Optional


class TreeNode:
    """Узел бинарного дерева поиска"""

    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self) -> str:
        return (f"Значение узла: {self.value}, Родитель узла: {self.parent}, "
                f"Левый потомок: {self.left}, Правый потомок:{self.right}")

    def __repr__(self) -> str:
        return self.__str__()


class BinarySearchTree:
    """Бинарное дерево поиска"""

    def __init__(self):
        self.root = None
        self._size = 0

    def insert(self, value: int) -> TreeNode:
        """
        Вставка элемента в дерево
        Сложность: в среднем O(log n), в худшем O(n)
        """
        new_node = TreeNode(value)

        if self.root is None:
            self.root = new_node
            self._size += 1
            return new_node

        current = self.root
        parent = None

        while current is not None:
            parent = current
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return current

        new_node.parent = parent
        if value < parent.value:
            parent.left = new_node
        elif value > parent.value:
            parent.right = new_node

        self._size += 1
        return new_node

    def search(self, value: int) -> Optional[TreeNode]:
        """
        Поиск элемента в дереве
        Сложность: в среднем O(log n), в худшем O(n)
        """
        return self._search_from_node(self.root, value)

    def _search_from_node(self, node: TreeNode, value: int) -> Optional[TreeNode]:
        """Рекурсивный вспомогательный метод для поиска"""
        if node is None or node.value == value:
            return node

        if value < node.value:
            return self._search_from_node(node.left, value)
        else:
            return self._search_from_node(node.right, value)

    def delete(self, value: int) -> bool:
        """
        Удаление элемента из дерева
        Сложность: в среднем O(log n), в худшем O(n)
        """
        node = self.search(value)
        if node is None:
            return False

        self._delete_node(node)
        self._size -= 1
        return True

    def _delete_node(self, node: TreeNode):
        """Вспомогательный метод для удаления узла"""
        if node.left is None and node.right is None:
            self._transplant(node, None)
        elif node.left is None:
            self._transplant(node, node.right)
        elif node.right is None:
            self._transplant(node, node.left)
        else:
            successor = self.find_min(node.right)

            if successor.parent != node:
                self._transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor

            self._transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor

    def _transplant(self, u: Optional[TreeNode], v: Optional[TreeNode]):
        """Заменяет поддерево с корнем u на поддерево с корнем v"""
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if v is not None:
            v.parent = u.parent

    def find_min(self, node: Optional[TreeNode] = None) -> Optional[TreeNode]:
        """
        Поиск минимального элемента в поддереве
        Сложность: O(h), где h - высота поддерева
        """
        if node is None:
            node = self.root
            if node is None:
                return None

        current = node
        while current.left is not None:
            current = current.left
        return current

    def find_max(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Поиск максимального элемента в поддереве
        Сложность: O(h), где h - высота поддерева
        """
        if node is None:
            node = self.root
            if node is None:
                return None

        current = node
        while current.right is not None:
            current = current.right
        return current

    def is_valid_bst(self) -> bool:
        """
        Проверка, является ли дерево корректным BST
        Сложность: O(n)
        """
        return self._is_valid_node(self.root, -10**10, 10**10)

    def _is_valid_node(self, node: Optional[TreeNode], min_val: int, max_val: int) -> bool:
        """Рекурсивная проверка валидности BST"""
        if node is None:
            return True

        if not (min_val < node.value < max_val):
            return False

        return (self._is_valid_node(node.left, min_val, node.value) and
                self._is_valid_node(node.right, node.value, max_val))

    def height(self, node: Optional[TreeNode] = None) -> int:
        """
        Вычисление высоты дерева/поддерева
        Сложность: O(n)
        """
        if node is None:
            node = self.root
            if node is None:
                return -1

        return self._height_of_node(node)

    def _height_of_node(self, node: Optional[TreeNode]) -> int:
        """Рекурсивное вычисление высоты"""
        if node is None:
            return -1

        left_height = self._height_of_node(node.left)
        right_height = self._height_of_node(node.right)

        return max(left_height, right_height) + 1

    def size(self) -> int:
        """Возвращает количество элементов в дереве"""
        return self._size

    def is_empty(self) -> bool:
        """Проверяет, пусто ли дерево"""
        return self.root is None

    def clear(self):
        """Очищает дерево"""
        self.root = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def __contains__(self, item: int) -> bool:
        return self.search(item) is not None
