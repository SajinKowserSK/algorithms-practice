class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # think of it like a mountain where the two sides are -inf
        # if we compare to the element to the next and its higher then the peak is over there
        # if we compare to the element and it's lower then we are going downhill and we need to go left to find peak
        if len(nums) == 1:
            return 0
        
        start, end = 0, len(nums)-1
        
        while start < end:
            mid = start + end 
            mid = int(mid/2)
            
            if nums[mid] < nums[mid+1]:
                # move right
                start = mid + 1 
                
            else:
                end = mid 
                
        return start 
        