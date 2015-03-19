from radix_sort import radix_sort, string_radix_sort
import pytest
import random


@pytest.fixture(scope='function')
def best_case_ten():
    return [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


@pytest.fixture(scope='function')
def worstish_case_ten():
    return [901234, 890123, 789012, 678901, 567890, 456789, 345678,
            234567, 123456, 100000]


@pytest.fixture(scope='function')
def simple_string():
    return ['abcd', 'abba', 'abc']


@pytest.fixture(scope="function")
def big_list():
    big_list = list()
    with open('/usr/share/dict/words', 'r') as words:
        for i, line in enumerate(words):
            if i % 1000 == 0:
                big_list.append(line)

    return big_list


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


def test_simple_string(simple_string):
    string_radix_sort(simple_string)
    assert simple_string == ['abba', 'abc', 'abcd']


def test_big_list(big_list):
    original_list = big_list[:]
    random.shuffle(big_list)
    string_radix_sort(big_list)
    assert big_list == original_list
