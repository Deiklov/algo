from typing import Any
import pytest

from VectorArray import VectorArray

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
def vector_array() -> VectorArray:
    return VectorArray()


@pytest.mark.parametrize("item,ind", test_add)
def test_vector_array_add(item: Any, ind: int, vector_array: VectorArray):
    old_len = vector_array.len
    vector_array.add(item, ind)
    assert vector_array.arr[ind] == item
    assert vector_array.len > old_len
    print(vector_array.arr)


@pytest.mark.parametrize("ret_value,ind", test_remove)
def test_vector_array_remove(ret_value: Any, ind: int, vector_array: VectorArray):
    old_len = vector_array.len
    assert vector_array.remove(ind) == ret_value
    assert vector_array.len == old_len-1
    print(vector_array.arr)


@pytest.mark.parametrize("range_val", [100, 1_000, 10_000, 100_000, 1_000_000])
def test_vector_array(range_val):
    arr = VectorArray()
    some_value = 20
    base_index = 0
    for i in range(range_val):
        arr.add(some_value, base_index)

    assert arr.len == range_val
