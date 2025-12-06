import pytest
from lab06.src.binary_search_tree import BinarySearchTree
from lab06.src.tree_traversal import inorder_recursive, preorder_recursive, postorder_recursive, inorder_iterative


@pytest.fixture
def small_tree():
    tree = BinarySearchTree()
    for v in [5, 3, 7, 2, 4, 6, 8]:
        tree.insert(v)
    return tree


def test_insert_and_size():
    tree = BinarySearchTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    assert tree.size() == 3


def test_search(small_tree):
    assert small_tree.search(7) is not None
    assert small_tree.search(999) is None


def test_delete_leaf(small_tree):
    assert small_tree.delete(2) is True
    assert small_tree.search(2) is None


def test_delete_node_with_children(small_tree):
    assert small_tree.delete(7) is True
    assert small_tree.search(7) is None
    assert small_tree.is_valid_bst()


def test_inorder_recursive(small_tree):
    assert inorder_recursive(small_tree.root) == [2, 3, 4, 5, 6, 7, 8]


def test_preorder_recursive(small_tree):
    assert preorder_recursive(small_tree.root) == [5, 3, 2, 4, 7, 6, 8]


def test_postorder_recursive(small_tree):
    assert postorder_recursive(small_tree.root) == [2, 4, 3, 6, 8, 7, 5]


def test_inorder_iterative(small_tree):
    assert inorder_iterative(small_tree) == [2, 3, 4, 5, 6, 7, 8]


def test_height(small_tree):
    assert small_tree.height() == 2
