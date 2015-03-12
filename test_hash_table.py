import pytest
from hash_table import HashTable


@pytest.fixture(scope="function")
def test_table():
    test_table = HashTable(10)
    return test_table


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
