from heapq import *

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k 
        self.minHeap = []
        for elem in nums:
            heappush(self.minHeap, elem)
        

    def add(self, val: int) -> int:
        heappush(self.minHeap, val)
        
        while len(self.minHeap) > self.k:
            heappop(self.minHeap)
        
        ans = heappop(self.minHeap)
        heappush(self.minHeap, ans)
        return ans
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)