class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0 
        
        
        dp = [amount + 1] * (amount + 1) # dp list from 0 to amount 
        dp[0] = 0 #to make 0 amt, you need 0 coins 
        
        for a in range(1, amount+1):
            for c in coins:
                if a >= c and (a-c) >= 0:
                    dp[a] = min(dp[a], dp[a-c] + 1)
                    
        return -1 if dp[-1] == amount + 1 else dp[-1]
                    
                    