class Node:
    """Класс узла связного списка."""

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """Односвязный список с базовыми операциями."""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_start(self, value):
        """Вставка элемента в начало списка.
        Сложность: O(1)
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def insert_at_end(self, value):
        """Вставка элемента в конец списка.
        Сложность: O(1)
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete_from_start(self):
        """Удаление элемента из начала списка.
        Сложность: O(1)
        """
        if self.head is None:
            return None
        removed_value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return removed_value

    def traversal(self):
        """Обход списка и вывод всех элементов.
        Сложность: O(n)
        """
        current = self.head
        elements = []
        while current is not None:
            elements.append(current.value)
            current = current.next
        return elements

    def __len__(self):
        """Подсчёт длины списка.
        Сложность: O(n)
        """
        length = 0
        current = self.head
        while current is not None:
            length += 1
            current = current.next
        return length

    def is_empty(self):
        """Проверка, пуст ли список.
        Сложность: O(1)
        """
        return self.head is None


if __name__ == "__main__":
    # Пример работы
    ll = LinkedList()
    ll.insert_at_start(3)
    ll.insert_at_start(2)
    ll.insert_at_end(4)
    ll.insert_at_end(5)

    print("Содержимое списка:", ll.traversal())
    print("Удалён элемент:", ll.delete_from_start())
    print("После удаления:", ll.traversal())
    print("Длина списка:", len(ll))
