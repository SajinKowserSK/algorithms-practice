class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0 
        
        # fill out a dp table with max 
        # amount of coins to create an amount from 0 -> amount (inclusive)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0 #base case 
        
        
        # fill up dp table, start at 1 and go to amount inclusive 
        for a in range(1, amount + 1):
            for c in coins:
                if (a-c) >= 0: # the coin is not too big and can sum to amt            
                    
                    # recurrence relation 
                    dp[a] = min(dp[a], 1 + dp[a-c])
                  
        # amount makeable with given coins and not set to default amount 
        if dp[-1] != amount + 1:
            return dp[-1]
        
        return -1 
                    
                    
                    
                    