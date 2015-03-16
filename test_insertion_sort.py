import pytest
from insertion_sort import insertion_sort


@pytest.fixture(scope="function")
def test_list():
    test_list = [5, 4, 3, 6, 7, 8, 1, 2]
    test_list_sorted = [1, 2, 3, 4, 5, 6, 7, 8]
    return test_list, test_list_sorted


def test_sort(test_list):
    insertion_sort(test_list[0])
    assert test_list[0] == test_list[1]


def test_best_case(test_list):
    best_list = range(1, 9)
    insertion_sort(best_list)
    assert best_list == test_list[1]


def test_worst_case(test_list):
    worst_list = range(8, 0, -1)
    insertion_sort(worst_list)
    assert worst_list == test_list[1]
