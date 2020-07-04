class Solution(object):
    def findPeakElement(self, nums):

        # peak elem is unique so is > left and right 
        # given any pt we must go near where it is rising 
        # if we are at a pt where elem > right but < left then go left 
        # if we are at a pt where elem < right but > left then go right 
        # if we are at trough go either way 
        
        if len(nums) == 0 or nums is None:
            return None 
        
        if len(nums) == 1:
            return 0
        
        start = 0 
        end = len(nums)-1
        
        while start <= end:
            mid = start + (end - start)/2
            mid = int(mid)
            print(mid)

            
            if mid > 0 and mid < len(nums)-1:
                if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                    return mid
                
                elif nums[mid] >= nums[mid-1] and nums[mid] <= nums[mid+1]:
                    start = mid + 1
                    
                else:
                    end = mid - 1 
                
            elif mid == 0:
                if nums[mid] > nums[mid+1]:
                    return mid
                
                else:
                    start = mid + 1 
                
            else:
                if nums[mid] > nums[mid-1]:
                    return mid
                
               
        return mid
                
            
                
        
        
