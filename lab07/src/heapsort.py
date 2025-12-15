from lab07.src.heap import Heap


def heapsort(array: list[int]) -> list[int]:
    """
    Сортировка кучей (через дополнительную память)
    Сложность: O(n log n)
    """
    heap = Heap(is_min=True)
    heap.build_heap(array)

    result = []
    while len(heap) > 0:
        result.append(heap.extract())

    return result
