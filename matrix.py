from typing_extensions import Self


class Matrix:
    matr: Self

    def __init__(self, list: list) -> None:
        self.matr = list

    def mult(self, list: Self) -> Self:
        return Matrix([[sum(a*b for a, b in zip(X_row, Y_col)) for Y_col in zip(*list.matr)] for X_row in self.matr])

    def __pow__(self, power: int):
        number = Matrix(self.matr)
        if power == 0:
            return 1.0
        p: Matrix = Matrix([[1, 0], [0, 1]])  # eye matrix
        d: Matrix = number
        while power > 1:
            # check if mod 2 ==1
            if power % 2 == 1:
                p = p.mult(d)
            d = d.mult(d)
            # divide on 2
            power >>= 1
        p = p.mult(d)
        return p
