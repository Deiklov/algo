from re import T
from tokenize import Single
from typing import Any
import pytest

from SingleArray import SingleArray

# val -- ind
test_add = [
    (1, 5),
    (2, 5),
    (2, 0),
]
# val -- ind
test_remove = [
    (2, 0),
    (2, 5),
    (1, 5),
]


@pytest.fixture(scope="session", autouse=True)
def single_array() -> SingleArray:
    return SingleArray()


@pytest.mark.parametrize("item,ind", test_add)
def test_single_array_add(item: Any, ind: int, single_array: SingleArray):
    old_len = single_array.len
    single_array.add(item, ind)
    assert single_array.arr[ind] == item
    assert single_array.len > old_len
    print(single_array.arr)


@pytest.mark.parametrize("ret_value,ind", test_remove)
def test_single_array_remove(ret_value: Any, ind: int, single_array: SingleArray):
    old_len = single_array.len
    assert single_array.remove(ind) == ret_value
    assert single_array.len == old_len-1
    print(single_array.arr)


@pytest.mark.parametrize("range_val", [100, 1_000, 10_000, 100_000, 1_000_000])
def test_single_array(range_val):
    arr = SingleArray()
    some_value = 20
    base_index = 0
    for i in range(range_val):
        arr.add(some_value, base_index)

    assert arr.len == range_val
