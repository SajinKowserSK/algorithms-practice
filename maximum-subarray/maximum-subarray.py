class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        final = float('-inf')
        currMax = nums[0]
        
        final = max(final, currMax)
        
        for x in range(1, len(nums)):
            currMax = max(nums[x], currMax + nums[x])
            final = max(final, currMax)
            
                
        return final
                
                
        