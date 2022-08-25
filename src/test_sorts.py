from importlib.metadata import files
import pytest
from bubble import bubble

from load_data import load_array


@pytest.mark.parametrize("files", load_array('../src/sorting-tests/0.random'))
def test_bubble_sort(files):
    size, input, output = files
    assert bubble(input, size) == output
