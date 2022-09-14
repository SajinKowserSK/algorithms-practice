class Solution:
    def isHappy(self, n: int) -> bool:
        cache = set()
        return self.helper(n, cache)
    
    def helper(self, n, cache):
        if n in cache:
            return False 
        
        if n == 1: 
            return True 
        
        cache.add(n)
        intstr = str(n)
        curr = 0
        for char in intstr:
            curr += int(char) ** 2 
            
        return self.helper(curr, cache)
            
        