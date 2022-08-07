import pytest
from junior import power_linear
from load_data import load_files_for_power
from decimal import *
from middle import power_linear_log, power_log


@pytest.mark.parametrize("files", load_files_for_power('../3.Power'))
def test_check_power(files):
    number, power, out = files
    assert round(power_linear(number, power), 11) == out


# middle


@pytest.mark.parametrize("files", load_files_for_power('../3.Power'))
def test_power_linear_log(files):
    number, power, out = files
    assert round(power_linear_log(number, power), 11) == out


@pytest.mark.parametrize("files", load_files_for_power('../3.Power'))
def test_power_log(files):
    number, power, out = files
    res = Decimal(power_log(number, power))
    setcontext(Context(prec=11, rounding=ROUND_DOWN))
    assert "{:.11f}".format(res) == str(out)
