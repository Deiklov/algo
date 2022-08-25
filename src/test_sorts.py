from importlib.metadata import files
import pytest
from bubble import bubble, insertion

from load_data import load_array


@pytest.mark.parametrize("files", load_array('../src/sorting-tests/0.random'))
def test_bubble_sort(files):
    size, input, output = files
    assert bubble(input, size) == output


@pytest.mark.parametrize("files", load_array('../src/sorting-tests/0.random'))
def test_insertion_sort(files):
    size, input, output = files
    assert insertion(input, size) == output
