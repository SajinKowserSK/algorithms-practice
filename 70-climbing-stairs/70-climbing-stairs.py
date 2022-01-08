class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {} 
        
        def dfs(n):
            if n in dp:
                return dp[n]
            
            if n == 0:
                return 1 
            
            if n < 0:
                return 0 
            dp[n-1] = dfs(n-1)
            dp[n-2] = dfs(n-2)
            dp[n] = dp[n-1] + dp[n-2]
            
            return dp[n]
        
        return dfs(n)
        