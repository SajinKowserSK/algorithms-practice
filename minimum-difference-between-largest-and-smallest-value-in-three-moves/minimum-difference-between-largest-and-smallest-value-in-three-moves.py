class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0 
        
        nums.sort() 
        
        diff = float('inf')
        for i in range(4):
            diff = min(diff, nums[len(nums) - 1 - 3 + i] - nums[i])
            
        return diff
            
        
        