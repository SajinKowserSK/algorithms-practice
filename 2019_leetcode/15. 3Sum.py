class Solution(object):
    
    def threeSum(self, nums):          
        start = 0 
        end = len(nums)-1
        
        nums.sort()
        master = []
        
        for x in range (0, len(nums)):
            target = nums[x] * -1
            entry = []
            
            while (start < end):
                
                if start == x:
                    start = start + 1
                    
                elif end == x:
                    end = end - 1 
                    
                else:    
                    startElem = nums[start]
                    endElem = nums[end]
                    twoSum = startElem + endElem

                    if twoSum == target:
                        
                        entry.append(startElem)
                        entry.append(endElem)
                        entry.append(target * -1)
                        
                        entry.sort()
                        
                        if entry not in master:
                            master.append(entry)
                            entry = []
                            start = start + 1 
                            
                        
                    elif twoSum > target:
                        end = end - 1 
                        
                    else:
                        start = start + 1
            
            start = 0
            end = len(nums)-1
            
            
        return new_master
    
