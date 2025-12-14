import random

from lab07.src.heap import Heap
from lab07.src.heapsort import heapsort
from lab07.src.priority_queue import PriorityQueue


def is_min_heap(data: list[int]) -> bool:
    """Проверка свойства min-heap"""
    n = len(data)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and data[i] > data[left]:
            return False
        if right < n and data[i] > data[right]:
            return False

    return True


def test_heap_insert_and_property():
    heap = Heap()
    values = [5, 3, 8, 1, 2, 7]

    for v in values:
        heap.insert(v)
        assert is_min_heap(heap.data)


def test_heap_extract_order():
    heap = Heap()
    values = [5, 3, 8, 1, 2]

    for v in values:
        heap.insert(v)

    extracted = [heap.extract() for _ in range(len(values))]

    assert extracted == sorted(values)


def test_heap_peek():
    heap = Heap()
    heap.insert(10)
    heap.insert(3)
    heap.insert(7)

    assert heap.peek() == 3


def test_heap_build_heap():
    data = [9, 5, 6, 2, 3]
    heap = Heap()
    heap.build_heap(data)

    assert is_min_heap(heap.data)
    assert sorted(heap.data) == sorted(data)


def test_extract_from_empty_heap():
    heap = Heap()
    assert heap.extract() is None


def test_heapsort_basic():
    data = [5, 1, 4, 2, 8]
    assert heapsort(data) == [1, 2, 4, 5, 8]


def test_heapsort_random():
    data = [random.randint(-1000, 1000) for _ in range(100)]
    assert heapsort(data) == sorted(data)


def test_heapsort_does_not_modify_original():
    data = [3, 1, 4]
    copy = data.copy()

    heapsort(data)
    assert data == copy


def test_priority_queue_basic():
    pq = PriorityQueue()

    pq.enqueue("low", 5)
    pq.enqueue("medium", 3)
    pq.enqueue("high", 1)

    assert pq.dequeue() == "high"
    assert pq.dequeue() == "medium"
    assert pq.dequeue() == "low"


def test_priority_queue_with_equal_priorities():
    pq = PriorityQueue()

    pq.enqueue("a", 1)
    pq.enqueue("b", 1)
    pq.enqueue("c", 1)

    result = {pq.dequeue(), pq.dequeue(), pq.dequeue()}
    assert result == {"a", "b", "c"}


def test_priority_queue_empty():
    pq = PriorityQueue()
    assert pq.dequeue() is None
