from heapq import * 
from math import sqrt

def e(pair):
    x1, y1 = 0, 0
    x2, y2 = pair[0], pair[1]
    
    first = (x1 - x2)**2 
    sec = (y1 - y2)**2
    
    return sqrt(first+sec)
    
    

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
                
        # we need to maintain the k closest points to the origin where closest = minimal euclid distance
        # we can maintain a minHeap of size k and return that list
        # each entry in the heap will be prioritized by e.euclid distance -> entry will be (E.Dist, (x, y))
        # at the end, return each item in list format 
        
        
        h = []
        
        for point in points:
            x, y = point[0], point[1]
            
            dist = e((x, y))
            heappush(h, (-dist, (x, y)))
            
            while len(h) > k:
                heappop(h)
        
        ans = [] 
        for elem in h:
            dist, point = elem[0], list(elem[1])
            ans.append(point)
            
        return ans 
            
            
            



        