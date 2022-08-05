import os
from collections import defaultdict
from traceback import print_tb
import pytest
import numpy as np


def full_calc(N: int):
    # matrix = np.zeros((9*N,9*N), dtype=np.uint64)
    # print(matrix)
    sum: int = 0
    i: int = 0
    # calc N(k) for 0 to 9N sum
    while i <= N*9:
        sum += calc_lucky_ticket(N, i)**2
        i += 1
    return sum


def calc_lucky_ticket(n: int, k: int) -> int:
    if n == 1:
        return 1 if 0 <= k <= 9 else 0
    else:
        sum: int = 0
        l: int = 0
        while l <= 9:
            sum += calc_lucky_ticket(n-1, k-l)
            l += 1
        return sum


def load_files(path):
    EXTENSIONS = {'.in', '.out'}
    directory = path

    grouped_files = defaultdict(int)

    for f in os.listdir(directory):
        name, ext = os.path.splitext(os.path.join(directory, f))
        if ext in EXTENSIONS:
            grouped_files[name] += 1

    for name in grouped_files:
        if grouped_files[name] == len(EXTENSIONS):
            with open('{}.in'.format(name), "r", encoding="utf-8") as in_file, \
                    open('{}.out'.format(name), "r", encoding="utf-8") as out_file:
                yield(int(in_file.readline()), int(out_file.readline()))


@pytest.mark.parametrize("files", load_files('lucky_tickets/1.Tickets'))
def test_check_tickets(files):
    input, output = files
    assert full_calc(input) == output


print(full_calc(7))
