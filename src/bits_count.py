def count_set_bits(n: int):
    count = 0
    while (n > 0):
        n &= (n-1)
        count += 1
    return count


def count_set_bits_linear(n: int) -> int:
    count = 0
    while (n > 0):
        if n & 1 == 1:
            count += 1
        n >>= 1
    return count


def count_set_bits_cash(n: int) -> int:
    count = 0
    if not hasattr(count_set_bits_cash, "bits"):
        bits = []
        for i in range(256):
            bits.append(count_set_bits(i))
        count_set_bits_cash.bits = bits
    while (n > 0):
        count += count_set_bits_cash.bits[n & 0b11111111]
        n >>= 8
    return count
