import pytest
from sorts_algo import *

from load_data import *

path = '../src/sorting-tests/0.random'


@pytest.mark.parametrize("files", load_array(path))
def test_selection_sort(files):
    size, input, output = files
    assert selection(input, size) == output