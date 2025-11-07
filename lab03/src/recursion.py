def factorial(n: int) -> int:
    """
    Рекурсивное вычисление факториала числа n.
    n! = n * (n-1) * (n-2) * ... * 1

    Базовый случай: factorial(0) = 1
    Рекурсивный шаг: factorial(n) = n * factorial(n-1)

    Временная сложность: O(n)
    Глубина рекурсии: O(n)
    """
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    """
    Рекурсивное вычисление n-го числа Фибоначчи.
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)

    Базовые случаи:
      F(0) = 0
      F(1) = 1
    Рекурсивный шаг:
      F(n) = F(n-1) + F(n-2)

    Временная сложность: O(2^n)
      (каждый вызов порождает два новых вызова)
    Глубина рекурсии: O(n)
    """
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def fast_power(a: int, n: int) -> int:
    """
    Быстрое возведение числа a в степень n (через деление степени на два).

    Идея:
      - a^0 = 1
      - если n чётное:  a^n = (a^(n/2))^2
      - если n нечётное: a^n = a * a^(n-1)

    Временная сложность: O(log n)
    Глубина рекурсии: O(log n)
    """
    if n == 0:
        return 1

    if n % 2 == 0:
        half = fast_power(a, n // 2)
        return half * half

    return a * fast_power(a, n - 1)


if __name__ == "__main__":
    print("Базовые рекурсивные функции:\n")

    n = 5
    print(f"{n}! = {factorial(n)}")

    n = 8
    print(f"{n}-е число Фибоначчи = {fibonacci(n)}")

    a, n = 2, 10
    print(f"{a}^{n} = {fast_power(a, n)}")
