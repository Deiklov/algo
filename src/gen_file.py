from random import randint, random


def gen_rand_file(N: int, T: int):
    with open("data.txt", 'w') as file:
        for i in range(N):
            file.write(f'{randint(1, T)}\n')
