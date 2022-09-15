class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        master = []
        nums.sort()
        self.dfsHelper(nums, master, [], "", 0, set())
        return master 
        
    def dfsHelper(self, nums, master, curr, strRep, i, seen):
        if strRep in seen:
            return
        
        if i >= len(nums):
            master.append(curr.copy())
            seen.add(strRep)
            return 
        
        else:
            # left will include the element 
            curr.append(nums[i])
            self.dfsHelper(nums, master, curr, strRep + str(nums[i]), i+1, seen)


            # right will not 
            curr.pop()
            self.dfsHelper(nums, master, curr, strRep, i+1, seen)
        
        
        

        
        
        
        
            
        
        