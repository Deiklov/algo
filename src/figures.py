from bits_count import count_set_bits, count_set_bits_cash, count_set_bits_linear


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

    return (count_set_bits_linear(int(mask)), mask)


def horse_mask(pos: int):
    bit_pos = 1 << pos
    nA = 0xFeFeFeFeFeFeFeFe
    nAB = 0xFcFcFcFcFcFcFcFc
    nH = 0x7f7f7f7f7f7f7f7f
    nGH = 0x3f3f3f3f3f3f3f3f
    # для тех что на 1-2 вертикали позиции, отвечающие за сдвиг влево обнулятся
    mask = nGH & (bit_pos << 6 | bit_pos >> 10) | nH & (bit_pos << 15 | bit_pos >> 17) | nA & (
        bit_pos << 17 | bit_pos >> 15) | nAB & (bit_pos << 10 | bit_pos >> 6)
    # adaptive for python int
    mask = mask & 0xffffffffffffffff

    return (count_set_bits_cash(int(mask)), mask)


def rook_mask(pos: int):
    number = pos//8
    alpha = pos % 8
    gorizonal_mask = 0xff
    vertical_mask = 0x101010101010101
    gorizonal_mask <<= number*8
    vertical_mask <<= alpha
    res = 1 << pos
    res ^= (gorizonal_mask | vertical_mask)
    res &= 0xffffffffffffffff
    return (count_set_bits(int(res)), res)


def bishop_mask(pos: int):
    number = pos//8
    alpha = pos % 8
    high_low_mask = 0x102040810204080
    low_high_mask = 0x8040201008040201
    if number <= alpha:
        low_high_mask >>= (alpha-number)*8
    else:
        low_high_mask <<= (number-alpha)*8

    if number <= 7-alpha:
        high_low_mask >>= ((7-alpha)-number)*8
    else:
        high_low_mask <<= (number-(7-alpha))*8

    res = 1 << pos
    res ^= (low_high_mask | high_low_mask)
    res &= 0xffffffffffffffff
    return (count_set_bits(int(res)), res)
