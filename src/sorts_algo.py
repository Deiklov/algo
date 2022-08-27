from enum import Flag


def bubble(arr: list, size: int) -> list:
    for i in range(size):
        for j in range(size-i-1):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)
    return arr


def bubble_with_count_exchange(arr: list, size: int) -> list:
    is_sorted = True
    for i in range(size):
        for j in range(size-i-1):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)
                is_sorted = False
        if is_sorted:
            return arr
        else:
            is_sorted = False

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


def insertion_binary_shift(arr: list, size: int) -> list:
    for i in range(1, size):
        curr = arr[i]
        # binary search for new position
        new_place_ind = binary_search(arr, 0, i-1, curr)
        # shift all elems to new pos
        for j in range(i, new_place_ind, -1):
            # shift to right
            arr[j] = arr[j-1]
        arr[new_place_ind] = curr
    return arr


def binary_search(arr: list, low: int, high: int, elem: int):
    if high <= low:
        if elem > arr[low]:
            return low+1
        else:
            return low
    mid = (low+high)//2
    # if elem == arr[mid]:
    #     return mid+1
    if elem > arr[mid]:
        return binary_search(arr, mid+1, high, elem)
    else:
        return binary_search(arr, low, mid-1, elem)


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
# print(insertion_binary_shift([7, 0, 6, 1, 3, 2, 8, 5, 4, 9], 10))
# print(binary_search([7, 0, 6, 1, 3, 2, 8, 5, 4, 9], 0,9,))
