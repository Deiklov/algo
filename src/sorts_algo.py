def bubble(arr: list, size: int) -> list:
    for i in range(size):
        for j in range(size-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


def insertion(arr: list, size: int) -> list:
    for i in range(size):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                swap(arr, j, j-1)
    return arr


def insertion_shift(arr: list, size: int) -> list:
    for i in range(1, size):
        curr = arr[i]
        for j in range(i, 0, -1):
            if arr[j-1] > curr:
                # shift to right
                arr[j] = arr[j-1]
            else:
                # paste last elem
                arr[j] = curr
                break
        else:
            arr[j-1] = curr
    return arr


def swap(arr: list, ind1: int, ind2: int):
    temp = arr[ind1]
    arr[ind1] = arr[ind2]
    arr[ind2] = temp

    # def shell(arr: list, size: int) -> list:
    #     d = size
    #     while d > 0:
    #         for i in range(size):
    #             for j in range(i, 0, d):
    #                 if arr[j] < arr[j-d]:
    #                     temp = arr[j]
    #                     arr[j] = arr[j-d]
    #                     arr[j-d] = temp
    #         d //= 2
    #     return arr
# print(insertion_shift([7, 0, 6, 1, 3, 2, 8, 5, 4, 9], 10))
