class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        master = []
        
        # have to sort, TC here is not an issue as entire algo is O(N x 2**N)
        nums.sort()
        self.dfsHelper(nums, master, [], 0)
        return master 
        
    def dfsHelper(self, nums, master, subset, i):
        if i == len(nums):
            master.append(subset.copy())
            return 
        
            
        # case where we include nums[i]
        subset.append(nums[i])
        self.dfsHelper(nums, master, subset, i+1)

        # case where we don't include nums[i]
        subset.pop()
        while i < len(nums)-1 and nums[i] == nums[i+1]: # iterate to non dup elem
            i += 1 

        self.dfsHelper(nums, master, subset, i+1)
            
            
       
        
        
        

        
        
        
        
            
        
        