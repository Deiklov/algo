from random import sample
import pytest
from bucket_sort import bucket_sort
from counting_sort import *
import numpy as np
from load_data import *
from radix_sort import radixSort

path = '../src/sorting-tests/3.revers'


@pytest.mark.parametrize("data", [np.random.randint(1000, size=1_000_000).tolist()])
def test_counting_sort(data: np.ndarray):
    assert countingSort(data) == data.sort()

@pytest.mark.parametrize("data", [np.random.randint(1000, size=1_000_000).tolist()])
def test_radix_sort(data: np.ndarray):
    assert radixSort(data) == data.sort()

@pytest.mark.parametrize("data", [np.random.randint(1000, size=1_000).tolist()])
def test_bucket_sort(data: np.ndarray):
    assert bucket_sort(data) == data.sort()
