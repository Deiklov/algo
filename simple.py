from unittest import result


def power_linear(number: float, power: int) -> float:
    result = number
    if power == 0:
        return 1.0
    for i in range(power-1):
        result *= number
    return result


def fibo_exp(N: int) -> int:
    if N == 0:
        return 0
    if N == 1:
        return 1
    return fibo_exp(N-1)+fibo_exp(N-2)
