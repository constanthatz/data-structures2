from merge_sort import merge_sort
from recursive_merge_sort import merge_sort as rec_merge_sort
import pytest
import random


@pytest.fixture(scope='function')
def empty_list():
    return []


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


def test_empty(empty_list):
    assert merge_sort(empty_list) == []


def test_even_best_list(even_best_list):
    assert merge_sort(even_best_list) == even_best_list


def test_even_worst_list(even_worst_list):
    assert merge_sort(even_worst_list) == even_worst_list[::-1]


def test_odd_best_list(odd_best_list):
    assert merge_sort(odd_best_list) == odd_best_list


def test_odd_worst_list(odd_worst_list):
    assert merge_sort(odd_worst_list) == odd_worst_list[::-1]


def test_random_list(random_list):
    the_list = [-3, -2, -1, 0, 1, 2, 3, 4]
    assert merge_sort(random_list) == the_list


# def test_recursive_empty(empty_list):
#     assert rec_merge_sort(empty_list) == []


# def test_recursive_even_best_list(even_best_list):
#     assert rec_merge_sort(even_best_list) == even_best_list


# def test_recursive_even_worst_list(even_worst_list):
#     assert rec_merge_sort(even_worst_list) == even_worst_list[::-1]


# def test_recursive_odd_best_list(odd_best_list):
#     assert rec_merge_sort(odd_best_list) == odd_best_list


# def test_recursive_odd_worst_list(odd_worst_list):
#     assert rec_merge_sort(odd_worst_list) == odd_worst_list[::-1]


# def test_recursive_random_list(random_list):
#     the_list = [-3, -2, -1, 0, 1, 2, 3, 4]
#     assert rec_merge_sort(random_list) == the_list

