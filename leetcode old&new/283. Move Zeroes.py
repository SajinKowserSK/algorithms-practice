# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elementsclass Solution(object):
    def moveZeroes(self, nums):
        if nums is None or len(nums) == 0:
            return None 
        
        b = 0
        curr = 0 
        
        while curr < len(nums):
            if nums[curr] != 0:
                tmp = nums[b]
                nums[b] = nums[curr] 
                nums[curr] = tmp
                b += 1 
                
            curr += 1
            
        return nums
                
