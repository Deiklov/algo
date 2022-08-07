import pytest
from junior import count_of_simple, fibo_exp, fibo_linear, power_linear
from load_data import load_files_for_power, load_files_for_fibo_and_simple
import sys
from decimal import *
from middle import fibo_gold, fibo_matrix, power_linear_log, power_log


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

# middle


@pytest.mark.parametrize("files", load_files_for_power('3.Power'))
def test_power_linear_log(files):
    number, power, out = files
    assert round(power_linear(number, power), 11) == out


@pytest.mark.parametrize("files", load_files_for_power('3.Power'))
def test_power_log(files):
    number, power, out = files
    res = Decimal(power_log(number, power))
    setcontext(Context(prec=11, rounding=ROUND_DOWN))
    assert "{:.11f}".format(res) == str(out)


@pytest.mark.parametrize("files", load_files_for_fibo_and_simple('4.Fibo'))
def test_check_fibo_gold(files):
    input, output = files
    assert fibo_gold(input) == output

@pytest.mark.parametrize("files", load_files_for_fibo_and_simple('4.Fibo'))
def test_check_fibo_matrix(files):
    input, output = files
    assert fibo_matrix(input) == output
