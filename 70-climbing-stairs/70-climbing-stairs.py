from collections import defaultdict 

def defVal():
    return 0
    
class Solution:
    
    def climbStairs(self, n: int) -> int:
        cache = defaultdict(defVal)
        self.helper(n, cache)
        return cache[n]
        
        
    def helper(self, n, dp):
        
        if n < 0:
            return 
        
        if n == 0: 
            dp[n] = 1 
        
        if n in dp:
            return dp[n]
        
        self.helper(n-1, dp)
        self.helper(n-2, dp)
        dp[n] = dp[n-1] + dp[n-2]
        return dp[n]
        
        