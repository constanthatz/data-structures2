from radix_sort import radix_sort
import pytest
import random


@pytest.fixture(scope='function')
def best_case_ten():
    return [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


@pytest.fixture(scope='function')
def worstish_case_ten():
    return [901234, 890123, 789012, 678901, 567890, 456789, 345678,
            234567, 123456, 100000]


def test_best_case_ten(best_case_ten):
    radix_sort(best_case_ten)
    assert best_case_ten == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_worstish_case_ten(worstish_case_ten):
    radix_sort(worstish_case_ten)
    assert worstish_case_ten == [100000, 123456, 234567,
                                 345678, 456789, 567890,
                                 678901, 789012, 890123,
                                 901234
                                 ]
