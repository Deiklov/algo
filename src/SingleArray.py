from typing import Any

# index > len


class SingleArray:
    def __init__(self) -> None:
        self.arr = []
        self.len = 0

    def add(self, item: Any, index: int) -> None:
        # index<len
        if index < self.len:
            new_len = self.len+1
            new_arr = [0]*new_len
            # copy first part before new element
            for i in range(index):
                new_arr[i] = self.arr[i]
            new_arr[index] = item
            # copy second part
            for i in range(index+1, new_len):
                new_arr[i] = self.arr[i-1]
            self.len = new_len
            self.arr = new_arr
        elif index >= self.len:
            new_len = index+1
            new_arr = [0]*new_len
            # copy full array
            for i in range(self.len):
                new_arr[i] = self.arr[i]
            new_arr[index] = item
            self.len = new_len
            self.arr = new_arr

    def remove(self, index: int) -> Any:
        assert index < self.len
        elem = self.arr[index]
        new_len = self.len-1
        new_arr = [0]*new_len
        for i in range(index):
            new_arr[i] = self.arr[i]
        for i in range(index+1, self.len):
            new_arr[i-1] = self.arr[i]
        self.arr = new_arr
        self.len = new_len
        return elem
