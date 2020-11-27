from math import sqrt
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        heap = []
        heapq.heapify(heap)

        constant = (0, 0)

        ans = []

        for x in range(0, len(points)):
            pt = tuple(points[x])

            pt_dist = self.eucDist(constant, pt)
            entry = (pt_dist, pt)
            heapq.heappush(heap, entry)

        for x in range(K):
            popped = heapq.heappop(heap)
            ans.append(list(popped[1]))

        return ans

    def eucDist(self, constant, pt):
        ans = sqrt(
            (constant[0] - pt[0]) ** 2
            +
            (constant[1] - pt[1]) ** 2
        )

        return ans

