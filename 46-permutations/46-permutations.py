class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        master, curr, subsets = [], [], nums.copy()
        self.helperDFS(nums, subsets, master, curr)
        return master 
        
        
    def helperDFS(self, nums, subsets, master, curr):
        if len(curr) == len(nums):
            master.append(curr.copy())
            return 
        
        # numbers left in the choice 
        for x in range(0, len(subsets)):
            elem = subsets[x]
            curr.append(elem)
            
            # remove that number from option in subset
            subsetsCopy = subsets.copy()
            subsetsCopy.pop(x)
            
            self.helperDFS(nums, subsetsCopy, master, curr)
            curr.pop()
            