def bubble(arr: list, size: int) -> list:
    for i in range(size):
        for j in range(size-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr