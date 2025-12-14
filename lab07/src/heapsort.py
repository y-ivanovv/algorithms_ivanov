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


def heapsort_inplace(arr: list[int]):
    """
    In-place Heapsort (Max-Heap)
    Сложность: O(n log n)
    Память: O(1)
    """
    n = len(arr)

    def sift_down(start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break

            if child + 1 <= end and arr[child] < arr[child + 1]:
                child += 1

            if arr[root] < arr[child]:
                arr[root], arr[child] = arr[child], arr[root]
                root = child
            else:
                break

    for i in range(n // 2 - 1, -1, -1):
        sift_down(i, n - 1)

    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(0, end - 1)
