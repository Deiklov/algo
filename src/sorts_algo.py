
class Heapsort:
    def __init__(self, arr: list, size: int) -> None:
        self.arr = arr
        self.size = size

    def sort(self) -> list:
        for root in range(self.size//2-1, -1,-1):
            self.heapify(root, self.size)
        for j in range(self.size-1, -1,-1):
            self.swap(0, j)
            self.heapify(0, j)
        return self.arr

    def swap(self, ind1: int, ind2: int):
        self.arr[ind2], self.arr[ind1] = self.arr[ind1], self.arr[ind2]

    def heapify(self, root: int, size: int) -> None:
        L = 2*root+1
        R = 2*root+2
        X = root
        # fast swap max to root
        if L < size and self.arr[L] > self.arr[X]:
            X = L
        if R < size and self.arr[R] > self.arr[X]:
            X = R
        if X == root:
            return
        # push max to root
        self.swap(X, root)
        self.heapify(X, size)


def selection(arr: list, size: int) -> list:
    for i in range(size-1):
        ind_max = 0
        for j in range(size-i):
            if arr[j] > arr[ind_max]:
                ind_max = j
        swap(arr, size-i-1, ind_max)
    return arr


def swap(arr: list, ind1: int, ind2: int):
    arr[ind2], arr[ind1] = arr[ind1], arr[ind2]
