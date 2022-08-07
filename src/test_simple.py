import pytest
from junior import count_of_simple
from load_data import load_files_for_fibo_and_simple
from decimal import *
from middle import count_of_simple_arr


@pytest.mark.parametrize("files", load_files_for_fibo_and_simple('../5.Primes'))
def test_count_of_simple(files):
    input, output = files
    assert count_of_simple(input) == output

# middle


@pytest.mark.parametrize("files", load_files_for_fibo_and_simple('../5.Primes'))
def test_count_of_simple_arr(files):
    input, output = files
    assert count_of_simple_arr(input) == output
