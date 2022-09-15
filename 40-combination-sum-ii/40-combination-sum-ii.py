class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        master, subset, i = [], [], 0
        candidates.sort()
        self.dfsHelper(candidates, i, 0, target, subset, master)
        return master
        
    def dfsHelper(self, candidates, i, total, target, subset, master):
        if total == target:
            master.append(subset.copy())
            return 
        
        if total > target or i >= len(candidates):
            return 
        
        curr = candidates[i]
        
        # case 1: include nums[i]
        subset.append(curr)
        self.dfsHelper(candidates, i+1, total + curr, target, subset, master)
        
        # case 2: don't include nums[i]
        subset.pop()
        while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
            i += 1 
            
        self.dfsHelper(candidates, i+1, total, target, subset, master)
            
            
        