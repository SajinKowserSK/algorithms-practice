class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # +1 there for OOB / comparing empty string char 
        
        dp = [[0 for col in range(len(text2)+1)] for row in range(len(text1)+1)]
        
        for row in range(len(text1)-1, -1, -1):
            for col in range(len(text2)-1,-1,-1):   
                if text1[row] == text2[col]:
                    dp[row][col] = 1 + dp[row+1][col+1] # go diagonal 
                    
                else:
                    dp[row][col] = max(dp[row][col+1], dp[row+1][col]) # go right or down 
                    
        return dp[0][0] 
        