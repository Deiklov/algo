# calc func for 6-digits numbers
def calc_for_6digit() -> int:
    suma: int = 0
    count: int = 0
    for a1 in range(10):
        for a2 in range(10):
            for a3 in range(10):
                suma = a1+a2+a3
                for b1 in range(10):
                    for b2 in range(10):
                        for b3 in range(10):
                            if suma == b1+b2+b3:
                                count += 1
    return count


print(calc_for_6digit())