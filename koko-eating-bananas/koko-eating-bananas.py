class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        
        low, high = 1, max(piles)
        speed = high 
        while low <= high:
            mid = low + high
            mid = int(mid/2)
            
            hours = 0 
            for p in piles:
                hours += math.ceil(p / mid)
                
            if hours > h: # takes too long, need to eat faster
                low = mid + 1 
                
            else:
                high = mid - 1 
                speed = min(speed, mid)
                
        
        return speed
        