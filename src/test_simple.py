import pytest
from junior import count_of_simple
from load_data import load_files_for_fibo_and_simple
from decimal import *
from middle import count_of_simple_arr
from middle import simple_eratosfen
from middle import simple_eratosfen_mem_opt


@pytest.mark.parametrize("files", load_files_for_fibo_and_simple('../5.Primes'))
def test_count_of_simple(files):
    input, output = files
    assert count_of_simple(input) == output

# middle


@pytest.mark.parametrize("files", load_files_for_fibo_and_simple('../5.Primes'))
def test_count_of_simple_arr(files):
    input, output = files
    assert count_of_simple_arr(input) == output


@pytest.mark.parametrize("files", load_files_for_fibo_and_simple('../5.Primes'))
def test_simple_eratosfen(files):
    input, output = files
    assert simple_eratosfen(input) == output


@pytest.mark.parametrize("files", load_files_for_fibo_and_simple('../5.Primes'))
def test_simple_eratosfen_mem_opt(files):
    input, output = files
    assert simple_eratosfen_mem_opt(input) == output


# print(simple_eratosfen_mem_opt(11))
