from heapq import * 

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = nums
        heapify(h)
        
        while len(h) > k:
            heappop(h)
            
        return h[0]
        
        
        