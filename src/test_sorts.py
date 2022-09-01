import pytest
from sorts_algo import *

from load_data import *

path = '../src/sorting-tests/0.random'


@pytest.mark.parametrize("files", load_array(path))
def test_merge_sort(files):
    size, input, output = files
    assert mergeSort(input) == output
