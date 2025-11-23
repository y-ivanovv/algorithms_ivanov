import pytest

from hash_functions import hash_sum, hash_poly, hash_djb2
from hash_table_chaining import HashTableChaining
from hash_table_open_addressing import HashTableLinear, HashTableDoubleHashing


@pytest.mark.parametrize("func", [hash_sum, hash_poly, hash_djb2])
def test_hash_deterministic(func):
    assert func("abc") == func("abc")


def test_chaining_insert_search():
    table = HashTableChaining(10)
    table.insert("a", 1)
    assert table.search("a") == 1


def test_chaining_update():
    table = HashTableChaining(10)
    table.insert("a", 1)
    table.insert("a", 2)
    assert table.search("a") == 2


def test_chaining_delete():
    table = HashTableChaining(10)
    table.insert("a", 1)
    table.delete("a")
    assert table.search("a") is None


def test_chaining_collisions():
    table = HashTableChaining(10)
    table.insert("ab", 1)
    table.insert("ba", 2)
    assert table.search("ab") == 1
    assert table.search("ba") == 2


def test_linear_insert_search():
    table = HashTableLinear(20)
    table.insert("a", 1)
    assert table.search("a") == 1


def test_linear_update():
    table = HashTableLinear(20)
    table.insert("a", 1)
    table.insert("a", 2)
    assert table.search("a") == 2


def test_linear_delete():
    table = HashTableLinear(20)
    table.insert("a", 1)
    table.delete("a")
    assert table.search("a") is None


def test_linear_collisions():
    table = HashTableLinear(10)
    for k in ["ab", "ba", "ca"]:
        table.insert(k, 1)

    for k in ["ab", "ba", "ca"]:
        assert table.search(k) == 1


def test_linear_overflow():
    table = HashTableLinear(5)

    for i in range(5):
        table.insert(f"k{i}", i)

    with pytest.raises(RuntimeError):
        table.insert("overflow", 123)


def test_double_insert_search():
    table = HashTableDoubleHashing(20)
    table.insert("a", 1)
    assert table.search("a") == 1


def test_double_update():
    table = HashTableDoubleHashing(20)
    table.insert("a", 1)
    table.insert("a", 2)
    assert table.search("a") == 2


def test_double_delete():
    table = HashTableDoubleHashing(20)
    table.insert("a", 1)
    table.delete("a")
    assert table.search("a") is None


def test_double_collisions():
    table = HashTableDoubleHashing(10)
    for k in ["ab", "ba", "ca"]:
        table.insert(k, 1)

    for k in ["ab", "ba", "ca"]:
        assert table.search(k) == 1


def test_double_overflow():
    table = HashTableDoubleHashing(5)

    for i in range(5):
        table.insert(f"k{i}", i)

    with pytest.raises(RuntimeError):
        table.insert("overflow", 123)
