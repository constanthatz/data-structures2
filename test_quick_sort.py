from quick_sort import quicksort
import pytest
import random


@pytest.fixture(scope='function')
def even_best_list():
    return [-3, -2, -1, 0, 1, 2, 3, 4]


@pytest.fixture(scope='function')
def even_worst_list():
    return [4, 3, 2, 1, 0, -1, -2, -3]


@pytest.fixture(scope='function')
def odd_best_list():
    return [-2, -1, 0, 1, 2, 3, 4]


@pytest.fixture(scope='function')
def odd_worst_list():
    return [4, 3, 2, 1, 0, -1, -2]


@pytest.fixture(scope='function')
def random_list():
    the_list = [-3, -2, -1, 0, 1, 2, 3, 4]
    return random.sample(the_list, len(the_list))


def test_empty():
    assert quicksort([]) == []


def test_even_best_list(even_best_list):
    assert quicksort(even_best_list) == even_best_list


def test_even_worst_list(even_worst_list):
    import pdb; pdb.set_trace()
    assert quicksort(even_worst_list) == even_worst_list[::-1]


def test_odd_best_list(odd_best_list):
    assert quicksort(odd_best_list) == odd_best_list


def test_odd_worst_list(odd_worst_list):
    assert quicksort(odd_worst_list) == odd_worst_list[::-1]


def test_random_list(random_list):
    the_list = [-3, -2, -1, 0, 1, 2, 3, 4]
    assert quicksort(random_list) == the_list
