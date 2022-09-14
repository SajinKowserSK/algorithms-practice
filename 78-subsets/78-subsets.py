class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # have to do a dfs where for every (subset, 0 <= index <= len(nums)), 
        # can recursively call again with the subset including nums[index] or not including nums[index]
        
        master, subset = [], []
        self.dfs(nums, 0, subset, master)
        return master
        
        
        
        
        
    def dfs(self, nums, i, subset, master):
        if i >= len(nums):
            master.append(subset.copy())
            
        else:
            # take the current indice into subset
            subset.append(nums[i])
            self.dfs(nums, i+1, subset, master)

            # don't take the current indice into subset
            subset.pop()
            self.dfs(nums, i+1, subset, master)
        
        
        
        
        