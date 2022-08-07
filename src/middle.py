
from math import sqrt

from matrix import Matrix
import numpy as np
import os
import psutil


def power_linear_log(number: float, power: int) -> float:
    result = number
    if power == 0:
        return 1.0
    indPower: int = 1
    while indPower*2 < power:
        indPower *= 2
        result *= result

    end = power-indPower

    for i in range(end):
        result *= number

    return result


def power_log(number: float, power: int) -> float:
    if power == 0:
        return 1.0
    p: int = 1
    d: float = number
    d1, p1 = 1, 0
    while power > 1:
        # check if mod 2 ==1
        if power % 2 == 1:
            p *= d
            # debug
            p1 += d1
        d *= d
        # debug
        d1 <<= 1
        # divide on 2
        power >>= 1
    p1 += d1
    p *= d
    print("p=", p1, "; d=", d1)
    return p


def fibo_gold(N: int) -> int:
    if N == 0:
        return 0
    if N == 1:
        return 1
    phi = (1+sqrt(5))/2
    phiminus = (1-sqrt(5))/2
    return round((pow(phi, N)-pow(phiminus, N))/sqrt(5))


def fibo_matrix(N: int) -> int:
    if N == 0:
        return 0
    if N == 1:
        return 1
    matr = Matrix([[1, 1], [1, 0]])
    matr = matr**(N-1)
    return matr.matr[0][0]


def count_of_simple_arr(N: int) -> int:
    primes: list = []

    def is_simple(N: int) -> bool:
        for i in primes:
            if N % i == 0:
                return False
        return True

    if N == 1:
        return 0
    if N == 2:
        return 1
    count_simple: int = 0
    for i in range(2, N+1):
        if is_simple(i):
            primes.append(i)
            count_simple += 1
    return count_simple


def simple_eratosfen(N: int) -> int:
    if N == 1:
        return 0
    if N == 2:
        return 1
    arr = np.full((N+1), True)
    # zero and one are not prime
    arr[0] = False
    arr[1] = False
    for i in range(2, round(sqrt(N))+1):
        for j in range(i*i, N+1, i):
            arr[j] = False
    print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)

    return np.sum(arr)


def simple_eratosfen_mem_opt(N: int) -> int:
    if N == 1:
        return 0
    if N == 2:
        return 1
    arr = np.full(shape=(N//64+1),
                  fill_value=np.iinfo(np.uintc).max, dtype=np.uintc)
    end = (N-(arr.size-1)*64)//2
    if N % 2 == 0:
        end -= 1
    # clear 0 and 1 bits
    arr[0] &= ~(1 << 0)  # set 0 to False number 1
    arr[0] |= 1 << 1  # set 1 to True number 3

    for i in range(2, round(sqrt(N))+1):
        for j in range(i*i, N+1, i):
            if j % 2 == 1:
                pos = j//2
                base = pos//32
                offset = pos-base*32
                arr[base] &= ~(1 << offset)  # set bit to zero

    # print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)
    count = 0
    for x in arr[:-1]:
        count += bin(x).count("1")
    # analyze last bytes
    for y in range(end):
        if (arr[arr.size-1] >> (y+1)) & 1:
            count += 1
    print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)
    return count+1  # include 2 in first even bit
