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
            for _ in range(len(dq)):
                popped = dq.popleft()
                currLvl.append(popped.val)
                
                if popped.left:
                    dq.append(popped.left)
                    
                if popped.right:
                    dq.append(popped.right)
                    
                    
            lvls.append(currLvl)
            
        return lvls
                
        