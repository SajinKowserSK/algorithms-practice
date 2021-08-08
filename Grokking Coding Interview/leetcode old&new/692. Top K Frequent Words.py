import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        map1 = {}
        heap = []
        heapq.heapify(heap)

        map2 = {}

        for elem in words:
            map1[elem] = map1.get(elem, 0) + 1

        for elem in map1:
            heapq.heappush(heap, (-map1[elem], elem))

        final = []
        for x in range(0, k):
            popped = heapq.heappop(heap)
            final.append(popped[1])

        return final


