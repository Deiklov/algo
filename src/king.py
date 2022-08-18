from doctest import master
import numpy as np


def king_mask(pos: int):
    bit_pos = 1 << pos
    noA = 0xfefefefefefefefe
    noB = 0x7f7f7f7f7f7f7f7f
    Kaleft = noA & bit_pos
    Karight = noB & bit_pos
    mask = (
        Kaleft << 7) | (bit_pos << 8) | (Karight << 9) | (
        Kaleft >> 1) | (Karight << 1) | (
        Kaleft >> 9) | (bit_pos >> 8) | (Karight >> 7)
    # adaptive for python int
    mask = mask & 0xffffffffffffffff

    return (countSetBits(int(mask)), mask)


def countSetBits(n: int):
    count = 0
    while (n):
        n &= (n-1)
        count += 1
    return count
