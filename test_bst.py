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


@pytest.fixture(scope="function")
def test_tree_delete():
    test_tree = Tree()
    test_tree.insert(10)
    test_tree.insert(2)
    test_tree.insert(14)
    test_tree.insert(15)
    test_tree.insert(16)
    test_tree.insert(13)
    test_tree.insert(12)
    test_tree.insert(3)
    test_tree.insert(4)
    test_tree.insert(1)
    test_tree.insert(0.5)

    return test_tree


@pytest.fixture(scope="function")
def test_tree_unblanced():
    test_tree = Tree()
    test_tree.insert(1)
    test_tree.insert(2)
    test_tree.insert(10)
    test_tree.insert(12)
    test_tree.insert(13)
    test_tree.insert(14)
    test_tree.insert(15)
    test_tree.insert(16)
    test_tree.insert(3)
    test_tree.insert(4)

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


def test_balance_negative_exact(test_tree_large):
    assert test_tree_large.balance() == -1


def test_balance_negative(test_tree_large):
    assert test_tree_large.balance() < 0


def test_balance_positive_exact():
    test_tree = Tree()
    test_tree.insert(5)
    test_tree.insert(4)
    assert test_tree.balance() == 1


def test_balance_positive():
    test_tree = Tree()
    test_tree.insert(5)
    test_tree.insert(4)
    assert test_tree.balance() > 0


def test_breadth_first_traversal(test_tree_large):
    expected = [5, 4, 8, 2, 10, 1, 3, 12, 14]
    actual = test_tree_large.breadth_first_traversal()
    for val in expected:
        assert val == actual.next()

    # Checks to ensure there are no untraversed values
    with pytest.raises(StopIteration):
        actual.next()


def test_in_order(test_tree_large):
    expected = [1, 2, 3, 4, 5, 8, 10, 12, 14]
    actual = test_tree_large.in_order()
    for val in expected:
        assert val == actual.next()
    with pytest.raises(StopIteration):
        actual.next()


def test_pre_order(test_tree_large):
    expected = [5, 4, 2, 1, 3, 8, 10, 12, 14]
    actual = test_tree_large.pre_order()
    for val in expected:
        assert val == actual.next()
    with pytest.raises(StopIteration):
        actual.next()


def test_post_order(test_tree_large):
    expected = [1, 3, 2, 4, 14, 12, 10, 8, 5]
    actual = test_tree_large.post_order()
    for val in expected:
        assert val == actual.next()
    with pytest.raises(StopIteration):
        actual.next()


def in_order_tester(value, tree):
    expected = [0.5, 1, 2, 3, 4, 10, 12, 13, 14, 15, 16]
    expected.remove(value)
    tree.delete(value)
    assert not tree.contains(value)
    actual = tree.in_order()
    for val in expected:
        assert val == actual.next()
    with pytest.raises(StopIteration):
        actual.next()


def test_delete_root(test_tree_delete):
    in_order_tester(10, test_tree_delete)
    assert test_tree_delete.root.key == 4


def test_delete_two_children_left(test_tree_delete):
    in_order_tester(2, test_tree_delete)
    assert test_tree_delete.root.left.key == 1


def test_delete_two_children_right(test_tree_delete):
    in_order_tester(14, test_tree_delete)
    assert test_tree_delete.root.right.key == 13


def test_delete_one_child_left(test_tree_delete):
    in_order_tester(1, test_tree_delete)
    assert test_tree_delete.root.left.left.key == 0.5


def test_delete_one_child_right(test_tree_delete):
    in_order_tester(15, test_tree_delete)
    assert test_tree_delete.root.right.right.key == 16


def test_delete_no_children(test_tree_delete):
    in_order_tester(16, test_tree_delete)
    assert test_tree_delete.root.right.right.right is None


def test_delete_not_present(test_tree):
    test_tree.delete(99)
    expected = [4, 5, 8]
    actual = test_tree.in_order()
    for val in expected:
        assert val == actual.next()
    with pytest.raises(StopIteration):
        actual.next()


def test_nuclear_option(test_tree_unblanced):
    # test_tree_unblanced.graph('unbalanced')
    test_tree_unblanced.nuclear_option()
    # test_tree_unblanced.graph('balanced')
    assert -1 <= test_tree_unblanced.balance() <= 1


def is_avl_balanced(tree):
    assert tree.root.key == 4
    assert tree.root.left.key == 3
    assert tree.root.right.key == 5


def test_avl_left_left():
    test_tree = Tree()
    test_tree.avl_insert(5)
    test_tree.avl_insert(4)
    test_tree.avl_insert(3)
    is_avl_balanced(test_tree)
    # test_tree.graph('checkll')


def test_avl_left_right():
    test_tree = Tree()
    test_tree.avl_insert(5)
    test_tree.avl_insert(3)
    test_tree.avl_insert(4)
    is_avl_balanced(test_tree)
    # test_tree.graph('checklr')


def test_avl_right_right():
    test_tree = Tree()
    test_tree.avl_insert(3)
    test_tree.avl_insert(4)
    test_tree.avl_insert(5)
    is_avl_balanced(test_tree)
    # test_tree.graph('checkrr')


def test_avl_right_left():
    test_tree = Tree()
    test_tree.avl_insert(3)
    test_tree.avl_insert(5)
    test_tree.avl_insert(4)
    is_avl_balanced(test_tree)
    # test_tree.graph('checkrl')


def test_avl_large():
    test_tree = Tree()
    test_tree.insert(4)
    test_tree.insert(2)
    test_tree.insert(6)
    test_tree.insert(1)
    test_tree.insert(3)
    test_tree.insert(5)
    test_tree.insert(15)
    test_tree.insert(7)
    test_tree.insert(16)
    test_tree.avl_insert(14)
    # test_tree.graph('6 Post AVL Balance')
    expected = [4, 2, 7, 1, 3, 6, 15, 5, 14, 16]
    actual = test_tree.breadth_first_traversal()

    for val in expected:
        assert val == actual.next()
    with pytest.raises(StopIteration):
        actual.next()
