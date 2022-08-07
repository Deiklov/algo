# O(N)


def power_linear(number: float, power: int) -> float:
    result = number
    if power == 0:
        return 1.0
    for i in range(power-1):
        result *= number
    return result

# O(2^N)


def fibo_exp(N: int) -> int:
    if N == 0:
        return 0
    if N == 1:
        return 1
    return fibo_exp(N-1)+fibo_exp(N-2)

# O(N)


def fibo_linear(N: int) -> int:
    if N == 0:
        return 0
    if N == 1:
        return 1
    f1: int = 0
    f2: int = 1
    f: int
    for i in range(1, N):
        f = f1+f2
        f1 = f2
        f2 = f
    return f

# O(N^2)


def count_of_simple(N: int) -> int:
    count: int = 0
    if N == 1:
        return 0
    if N == 2:
        return 1
    # not check 1 and check our number
    for i in range(2, N+1):
        # not check 1 and not check number
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            count += 1
    return count
