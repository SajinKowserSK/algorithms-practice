from collections import deque 
from collections import defaultdict 
import operator 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq = deque() 
        dq.append((root, 0, 0)) # (node, col, row)
        master = []
        
        lvls = defaultdict(list) 
        
        while dq:
            popped = dq.popleft() 
            node, lvl, col = popped
            
            lvls[lvl].append((node.val, lvl, col))
            
            if node.left: 
                dq.append((node.left, lvl-1, col+1))
                
            if node.right:
                dq.append((node.right, lvl+1, col+1))
                
        levels = list(lvls.keys())
        levels.sort() 
        
        for key in levels:
            col = lvls[key]

            col.sort(key = operator.itemgetter(2, 0))
            col = [x[0] for x in col]
            lvls[key] = col
            
        for key in levels: 
            entry = lvls[key]
            master.append(lvls[key])
            
        
        return master
            
            
            
        