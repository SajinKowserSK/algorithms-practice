class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        frontier = 0 
        for x in range(0, len(nums)):
            if nums[x] == 0:
                tmp = nums[frontier]
                nums[frontier] = nums[x]
                nums[x] = tmp 
                frontier += 1 
                
        currFrontier = frontier
        for x in range(currFrontier, len(nums)):
            if nums[x] == 1:
                tmp = nums[frontier]
                nums[frontier] = nums[x]
                nums[x] = tmp 
                frontier += 1 
        
        # rest will be just 2s 
                
                
        
        
       

                
        
        """Z
        Do not return anything, modify nums in-place instead.
        """
        