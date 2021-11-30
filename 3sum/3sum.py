class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        
        nums.sort()
        
        for x in range(0, len(nums)):
            curr = nums[x]
            
            twoSum_target = -1 * curr
            
            start = x+1
            end = len(nums)-1
            
            while start < end:

                start_elem = nums[start]
                end_elem = nums[end]
                
                
                if start_elem + end_elem == twoSum_target:
                    entry = [curr, start_elem, end_elem]
                    entry.sort() 
                    entry = tuple(entry)
                    ans.add(entry)
                    
                    start+=1 
                    end -= 1 
                    
                elif start_elem + end_elem > twoSum_target:
                    end -= 1 
                    
                else:
                    start += 1 
                    
                    
        return ans 
        