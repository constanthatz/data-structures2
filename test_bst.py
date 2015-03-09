import pytest
from bst import Tree


@pytest.fixture(scope="function")
def test_tree():
    test_tree = Tree()
    test_tree.insert(5)
    test_tree.insert(4)
    test_tree.insert(8)

    return test_tree


@pytest.fixture(scope="function")
def test_tree_large(test_tree):
    test_tree.insert(10)
    test_tree.insert(2)
    test_tree.insert(3)
    test_tree.insert(12)
    test_tree.insert(1)
    test_tree.insert(14)

    return test_tree


def test_insert_as_root():
    test_tree = Tree()
    test_tree.insert(5)
    assert test_tree.root.key == 5


def test_insert_greater():
    test_tree = Tree()
    test_tree.insert(5)
    test_tree.insert(6)
    assert test_tree.root.right.key == 6


def test_insert_less():
    test_tree = Tree()
    test_tree.insert(5)
    test_tree.insert(4)
    assert test_tree.root.left.key == 4


def test_contains(test_tree):
    assert test_tree.contains(8) is True


def test_does_not_contains(test_tree):
    assert test_tree.contains(9) is False


def test_size(test_tree):
    assert test_tree.size() == 3


def test_insert_already_present(test_tree):
    test_tree.insert(4)
    assert test_tree.size() == 3


def test_size_large(test_tree_large):
    assert test_tree_large.size() == 9


def test_size_zero(test_tree):
    test_tree = Tree()
    assert test_tree.size() == 0


def test_depth_zero():
    test_tree = Tree()
    assert test_tree.depth() == 0


def test_depth(test_tree):
    assert test_tree.depth() == 2


def test_depth_deeper(test_tree_large):
    assert test_tree_large.depth() == 5


def test_balance(test_tree):
    assert test_tree.balance() == 0


def test_balance_negative(test_tree_large):
    assert test_tree_large.balance() < 0


def test_balance_positive():
    test_tree = Tree()
    test_tree.insert(5)
    test_tree.insert(4)
    assert test_tree.balance() > 0
