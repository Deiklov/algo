import pytest
from junior import fibo_exp, fibo_linear
from load_data import load_files_for_fibo_and_simple
import sys
from decimal import *
from middle import fibo_gold, fibo_matrix


@pytest.mark.parametrize("files", load_files_for_fibo_and_simple('../4.Fibo'))
def test_check_fibo_exp(files):
    sys.setrecursionlimit(2000)
    input, output = files
    assert fibo_exp(input) == output


@pytest.mark.parametrize("files", load_files_for_fibo_and_simple('../4.Fibo'))
def test_check_fibo_linear(files):
    input, output = files
    assert fibo_linear(input) == output


# middle

@pytest.mark.parametrize("files", load_files_for_fibo_and_simple('../4.Fibo'))
def test_check_fibo_gold(files):
    input, output = files
    assert fibo_gold(input) == output


@pytest.mark.parametrize("files", load_files_for_fibo_and_simple('../4.Fibo'))
def test_check_fibo_matrix(files):
    input, output = files
    assert fibo_matrix(input) == output
