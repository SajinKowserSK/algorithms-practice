# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict 
from collections import deque 

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        dq = deque()
        dq.append((root, 0))
        
        hmap = defaultdict(list)
        
        while dq:
            node, col = dq.popleft()
            if node:
                hmap[col].append(node.val)
                dq.append((node.left, col-1))
                dq.append((node.right, col+1))
            
        cols = list(hmap.keys())
        cols.sort()
        return [hmap[col] for col in cols] 
        
        