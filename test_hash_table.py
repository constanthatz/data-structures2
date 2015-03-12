import pytest
from hash_table import HashTable
import random

@pytest.fixture(scope="function")
def test_table():
    test_table = HashTable(10)
    return test_table


@pytest.fixture(scope="function")
def big_list():
    with open('/usr/share/dict/words', 'r') as words:
        big_list = words.readlines()
    return big_list


def test_init(test_table):
    assert test_table.size == 10
    assert test_table.table
    assert len(test_table.table) == 10


def test_hash(test_table):
    assert test_table.hash("test") == 8


def test_set(test_table):
    test_table.set("test", 10)
    assert test_table.table[8] == [("test", 10)]


def test_set_bad_value(test_table):
    with pytest.raises(TypeError):
        test_table.set(2, 10)


def test_get(test_table):
    test_table.set("test", 10)
    assert test_table.get("test") == 10


def test_get_not_found(test_table):
    with pytest.raises(ValueError):
        test_table.get("test")


def test_big_list(big_list):
    table = HashTable(1024)
    for item in big_list:
        table.set(item, item)
    for item in random.sample(big_list, 1000):
        assert table.get(item) == item
