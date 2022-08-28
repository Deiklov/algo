from importlib.metadata import files
import pytest
from sorts_algo import *

from load_data import *


# @pytest.mark.parametrize("files", load_array('../src/sorting-tests/0.random'))
# def test_bubble_sort(files):
#     size, input, output = files
#     assert bubble(input, size) == output


# @pytest.mark.parametrize("files", load_array('../src/sorting-tests/0.random'))
# def test_bubble_with_count_exchange(files):
#     size, input, output = files
#     assert bubble_with_count_exchange(input, size) == output


# @pytest.mark.parametrize("files", load_array('../src/sorting-tests/0.random'))
# def test_insertion_sort(files):
#     size, input, output = files
#     assert insertion(input, size) == output

# @pytest.mark.parametrize("files", load_array('../src/sorting-tests/0.random'))
# def test_insertion_shift_sort(files):
#     size, input, output = files
#     assert insertion_shift(input, size) == output


# @pytest.mark.parametrize("files", load_array('../src/sorting-tests/0.random'))
# def test_insertion_binary_shift_sort(files):
#     size, input, output = files
#     assert insertion_binary_shift(input, size) == output

@pytest.mark.parametrize("files", load_array('../src/sorting-tests/0.random'))
def test_shell_sort(files):
    size, input, output = files
    assert shell_sort(input, size) == output