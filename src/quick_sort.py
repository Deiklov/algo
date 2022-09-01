import sys


class QuickSort:
    def __init__(self, arr: list, size: int) -> None:
        self.arr = arr
        self.size = size
        sys.setrecursionlimit(1_000_000)

    def sort(self) -> list:
        self.quick_sort(self.arr, 0, self.size-1)
        return self.arr

    def quick_sort(self, array, start, end):
        if start >= end:
            return
        p = self.partition(array, start, end)
        self.quick_sort(array, start, p-1)
        self.quick_sort(array, p+1, end)

    def partition(self, array, start, end):
        pivot = array[start]
        low = start + 1
        high = end

        while True:
            # If the current value we're looking at is larger than the pivot
            # it's in the right place (right side of pivot) and we can move left,
            # to the next element.
            # We also need to make sure we haven't surpassed the low pointer, since that
            # indicates we have already moved all the elements to their correct side of the pivot
            while low <= high and array[high] >= pivot:
                high = high - 1

            # Opposite process of the one above
            while low <= high and array[low] <= pivot:
                low = low + 1

            # We either found a value for both high and low that is out of order
            # or low is higher than high, in which case we exit the loop
            if low <= high:
                array[low], array[high] = array[high], array[low]
                # The loop continues
            else:
                # We exit out of the loop
                break

        array[start], array[high] = array[high], array[start]

        return high
