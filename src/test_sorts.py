import pytest
from bucket_sort import bucketSort
from counting_sort import *
import numpy as np
from load_data import *
from radix_sort import radixSort

path = '../src/sorting-tests/3.revers'


@pytest.mark.parametrize("data", [np.random.randint(1000, size=1_000_000).tolist()])
def test_counting_sort(data: np.ndarray):
    sorted_data = countingSort(data)
    data.sort()
    assert sorted_data == data


@pytest.mark.parametrize("data", [np.random.randint(1000, size=1_000_000).tolist()])
def test_radix_sort(data: np.ndarray):
    sorted_data = radixSort(data)
    data.sort()
    assert sorted_data == data


@pytest.mark.parametrize("data", [np.random.randint(1000, size=1_00_000).tolist()])
def test_bucket_sort(data: np.ndarray):
    # print(data)
    sorted_data = bucketSort(data)
    data.sort()
    assert sorted_data == data
