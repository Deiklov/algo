import pytest
from simple import count_of_simple, fibo_exp, fibo_linear, power_linear
from load_data import load_files_for_power, load_files_for_fibo_and_simple
import sys

@pytest.mark.parametrize("files", load_files_for_power('3.Power'))
def test_check_power(files):
    number, power, out = files
    assert round(power_linear(number, power), 11) == out


@pytest.mark.parametrize("files", load_files_for_fibo_and_simple('4.Fibo'))
def test_check_fibo_exp(files):
    sys.setrecursionlimit(2000)
    input, output = files
    assert fibo_exp(input) == output


@pytest.mark.parametrize("files", load_files_for_fibo_and_simple('4.Fibo'))
def test_check_fibo_linear(files):
    input, output = files
    assert fibo_linear(input) == output


@pytest.mark.parametrize("files", load_files_for_fibo_and_simple('5.Primes'))
def test_count_of_simple(files):
    input, output = files
    assert count_of_simple(input) == output
