import pytest
from junior import count_of_simple, fibo_exp, fibo_linear, power_linear
from load_data import load_files_for_power, load_files_for_fibo_and_simple
import sys
from decimal import *
from middle import count_of_simple_arr, fibo_gold, fibo_matrix, power_linear_log, power_log


@pytest.mark.parametrize("files", load_files_for_fibo_and_simple('../5.Primes'))
def test_count_of_simple(files):
    input, output = files
    assert count_of_simple(input) == output

# middle


@pytest.mark.parametrize("files", load_files_for_fibo_and_simple('../5.Primes'))
def test_count_of_simple_arr(files):
    input, output = files
    assert count_of_simple_arr(input) == output
