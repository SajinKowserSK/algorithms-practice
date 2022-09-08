from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return [] 
        
        rights = []
        dq = deque()
        dq.append(root)
        
        while dq:
            for _ in range(0, len(dq)):
                popped = dq.popleft()
                if popped.left:
                    dq.append(popped.left)
                    
                if popped.right:
                    dq.append(popped.right)
                    
            # the most recent popped value will be the right side view
            rights.append(popped.val)
            
        return rights
        
        