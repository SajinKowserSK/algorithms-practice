from collections import deque 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return [] 
        
        lvls = [] 
        dq = deque()
        dq.append(root)
        
        while dq: 
            currLvl = [] 
            
            # only iterate however many nodes are in this level
            # don't do for node in dq: as the dq will change size as we add children
            for _ in range(0, len(dq)):
                popped = dq.popleft()
                currLvl.append(popped.val)
                
                if popped.left is not None:
                    dq.append(popped.left)
                    
                if popped.right is not None:
                    dq.append(popped.right)
                    
            lvls.append(currLvl)
            
        return lvls
                
                
        
        