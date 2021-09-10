from heapq import *


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minHeap = []
        res = []
        for elem in matrix:
            heappush(minHeap, elem)

        while minHeap and len(res) < k:
            popped = heappop(minHeap)
            res.append(popped[0])
            popped.pop(0)

            if len(popped) != 0:
                heappush(minHeap, popped)

        return res[-1]

