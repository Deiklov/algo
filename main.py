import pytest
from simple import fibo_exp, power_linear
from load_data import load_files_for_power, load_files_for_fibo_and_simple


@pytest.mark.parametrize("files", load_files_for_power('3.Power'))
def test_check_power(files):
    number, power, out = files
    assert round(power_linear(number, power), 11) == out


@pytest.mark.parametrize("files", load_files_for_fibo_and_simple('4.Fibo'))
def test_check_fibo(files):
    input, output = files
    assert fibo_exp(input) == output