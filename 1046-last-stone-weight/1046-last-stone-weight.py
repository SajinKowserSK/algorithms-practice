from heapq import *

class maxHeap: 
    def __init__(self):
        self.h = [] 
        
    def getLen(self):
        return len(self.h)
        
    def hpush(self, val):
        heappush(self.h, -val)
        
    def hpop(self):
        ans = heappop(self.h)
        ans = ans * -1 
        return ans 
        

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # need to maintain a priority queue by stone weight
        # use a maxHeap to keep size of the max stone
        
        heap = maxHeap()
        
        for stone in stones:
            heap.hpush(stone)
            
        # have the max heap now 
        
        while heap.getLen() > 1:
            y = heap.hpop()
            x = heap.hpop()
            
            # do nothing if they are both same as they wont be added into quue 
            if x != y:
                diff = y - x 
                heap.hpush(diff)
                
        if heap.getLen() == 0:
            return 0 
        
        ans = heap.hpop()
        return ans 
                
                
            

        