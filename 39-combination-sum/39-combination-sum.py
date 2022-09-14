class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        master = [] 
        subset = [] 
        currTotal = 0 
        i = 0 
        
        self.helperDFS(candidates, i, target, subset, currTotal, master)
        return master
        
        
    def helperDFS(self, candidates, i, target, subset, currTotal, master):
        if i >= len(candidates) or sum(subset) > target:
            return 
        
        if sum(subset) == target:
            master.append(subset.copy())
            return 
             
        # left includes this same one 
        subset.append(candidates[i])
        currTotal += candidates[i]
        self.helperDFS(candidates, i, target, subset, currTotal, master)

        # right does not include same one at all 
        subset.pop()
        currTotal -= candidates[i]
        self.helperDFS(candidates, i+1, target, subset, currTotal, master)
        
        
        