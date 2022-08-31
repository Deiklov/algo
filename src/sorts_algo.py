

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

