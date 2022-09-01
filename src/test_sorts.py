import pytest
from gen_file import gen_rand_file
from merge_sort import *

from load_data import *
from quick_sort import QuickSort

path = '../src/sorting-tests/3.revers'


@pytest.mark.parametrize("files", load_array(path))
def test_merge_sort(files):
    size, input, output = files
    assert mergeSort(input) == output


@pytest.mark.parametrize("files", load_array(path))
def test_quick_sort(files):
    size, input, output = files
    assert QuickSort(input, size).sort() == output


def test_gen_file():
    gen_rand_file(1_00_000, 10)
    assert True