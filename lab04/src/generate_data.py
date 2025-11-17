import random
from math import ceil


def random_array(n: int) -> list[int]:
    return [random.randint(0, n * 10) for _ in range(n)]


def sorted_array(n: int) -> list[int]:
    return list(range(n))


def reversed_array(n: int) -> list[int]:
    return list(range(n, 0, -1))


def almost_sorted_array(n: int) -> list[int]:
    arr = list(range(n))
    length = len(arr)
    k = 0.05
    disorder = ceil(length * k)

    for i in range(disorder):
        arr[length - 1 - i], arr[i] = arr[i], arr[length - 1 - i]

    return arr
