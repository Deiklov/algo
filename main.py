import os
from collections import defaultdict
import pytest
import numpy as np

# used this posts https://habr.com/ru/post/266479/
def full_calc(N: int) -> int:
    matrix = np.zeros((10*N, N), dtype=np.uint64)
    # define first column with values for 1 digit
    for i in range(10):
        matrix[i, 0] = 1

    for i in range(1, N):
        for j in range(10*N):
            curr_ind = j
            # down by column
            while curr_ind+10 > j and curr_ind >= 0:
                matrix[j, i] += matrix[curr_ind, i-1]
                curr_ind -= 1

    data = np.square(matrix[:, -1])

    return np.sum(data, dtype=np.uint)


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
