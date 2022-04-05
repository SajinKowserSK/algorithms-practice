'''
This class is used to implement the min heap which is defined in our heap lecture notes
SM Shahariar (Sajin) Kowser | 251014520
'''
import math
class Heap:
    def __init__(self, keys, n):
        self.n = n

        arr = [math.inf] + keys
        heap_idx = [0] * (self.n*2)

        for x in range(1, self.n+1):
            heap_idx[x + self.n - 1 ] = x

        for x in range(self.n-1, 0, -1):
            if arr[heap_idx[2*x]] < arr[heap_idx[2*x+1]]:
                heap_idx[x] = heap_idx[2*x]

            else:
                heap_idx[x] = heap_idx[2*x+1]

        self.arr = arr
        self.heap_idx = heap_idx

    def in_heap(self, id):
        if id in self.heap_idx:
            return True

        return False

    def min_key(self):
        return self.arr[self.heap_idx[1]]

    def min_id(self):
        return self.heap_idx[1]

    def key(self, id):
        return self.arr[id]


    def delete_min(self):
        self.arr[0] = math.inf

        self.heap_idx[self.heap_idx[1] + self.n - 1] = 0

        vertex = self.arr[self.heap_idx[1]]

        idx = math.floor((self.heap_idx[1] + self.n - 1) /2)

        while idx > 0:
            if self.arr[self.heap_idx[idx*2]] < self.arr[self.heap_idx[idx*2+1]]:
                self.heap_idx[idx] = self.heap_idx[idx*2]

            else:
                self.heap_idx[idx] = self.heap_idx[2*idx + 1]

            idx = math.floor(idx/2)

        return vertex

    # sets the key of the element with id to new_key if its current key is greater
    # than the new_key
    def decrease_key(self, id, new_key):
        if self.key(id) > new_key:
            self.arr[id] = new_key

            idx = math.floor((id + self.n-1)/2)
            while idx > 0:
                if self.arr[self.heap_idx[2*idx]] < self.arr[self.heap_idx[2*idx+1]]:
                    self.heap_idx[idx] = self.heap_idx[idx*2]

                else:
                    self.heap_idx[idx] = self.heap_idx[2*idx+1]

                idx = math.floor(idx/2)