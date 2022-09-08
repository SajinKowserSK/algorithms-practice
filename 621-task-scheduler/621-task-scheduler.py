from collections import Counter
import heapq 
from collections import deque 

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        occ = Counter(tasks)
        occ = list(occ.values())
        
        maxHeap = [[-x, 0] for x in occ] # (freq, time)
        dq = deque() 
        heapify(maxHeap)
        
        time = 0 
        while maxHeap or dq: 
            time += 1 
            if maxHeap:
                popped = heappop(maxHeap)

                popped[0] += 1 # reduce freq by 1 
                popped[1] = time + n # the time it will be available again 

                if popped[0] != 0:
                    dq.append(popped)

            if dq and dq[0][1] == time:
                dqPop = dq.popleft()
                heappush(maxHeap, dqPop)
                
                
        return time 
        
        
        