from typing import Optional
from binary_search_tree import TreeNode, BinarySearchTree


def inorder_recursive(node: Optional[TreeNode], result: list[int] = None) -> list[int]:
    """
    Рекурсивный in-order обход (левый-корень-правый)
    Сложность: O(n)
    """
    if result is None:
        result = []

    if node is not None:
        inorder_recursive(node.left, result)
        result.append(node.value)
        inorder_recursive(node.right, result)

    return result


def preorder_recursive(node: Optional[TreeNode], result: list[int] = None) -> list[int]:
    """
    Рекурсивный pre-order обход (корень-левый-правый)
    Сложность: O(n)
    """
    if result is None:
        result = []

    if node is not None:
        result.append(node.value)
        preorder_recursive(node.left, result)
        preorder_recursive(node.right, result)

    return result


def postorder_recursive(node: Optional[TreeNode], result: list[int] = None) -> list[int]:
    """
    Рекурсивный post-order обход (левый-правый-корень)
    Сложность: O(n)
    """
    if result is None:
        result = []

    if node is not None:
        postorder_recursive(node.left, result)
        postorder_recursive(node.right, result)
        result.append(node.value)

    return result


def inorder_iterative(tree: BinarySearchTree) -> list[int]:
    """
    Итеративный in-order обход с использованием стека
    Сложность: O(n)
    """
    result = []
    stack = []
    current_node = tree.root

    while current_node is not None or stack:
        while current_node is not None:
            stack.append(current_node)
            current_node = current_node.left

        current_node = stack.pop()
        result.append(current_node.value)

        current_node = current_node.right

    return result
