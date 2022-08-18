import os
from collections import defaultdict, OrderedDict
from natsort import natsorted


def load_files_for_bits(path):
    EXTENSIONS = {'.in', '.out'}
    directory = path

    grouped_files = defaultdict(int)

    for f in os.listdir(directory):
        name, ext = os.path.splitext(os.path.join(directory, f))
        if ext in EXTENSIONS:
            grouped_files[name] += 1
    grouped_files = OrderedDict(natsorted(grouped_files.items()))

    for name in grouped_files:
        if grouped_files[name] == len(EXTENSIONS):
            with open('{}.in'.format(name), "r", encoding="utf-8") as in_file, \
                    open('{}.out'.format(name), "r", encoding="utf-8") as out_file:
                yield(int(in_file.readline()), int(out_file.readline()),int(out_file.readline()))
