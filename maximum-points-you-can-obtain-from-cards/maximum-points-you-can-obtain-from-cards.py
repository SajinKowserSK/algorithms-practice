class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        final = 0 
        currSum = 0 
        
        n = len(cardPoints)
        
        right = n - k 
        
        for y in range(right, n):
            currSum += cardPoints[y]
            
        final = currSum # now final is the rightmost k elements 
        left = 0 
            
        for y in range(k):
            currSum -= cardPoints[right]
            right += 1 
            currSum += cardPoints[left]
            left += 1 
            
            final = max(final, currSum)
            
            
   
        return final 
        
        
            
            
        