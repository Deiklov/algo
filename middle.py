# O(N)


from math import log2, ceil, sqrt
from traceback import print_tb
from unittest import result

from matrix import Matrix


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
