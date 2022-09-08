# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True 
        
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        
        return (abs(left - right) <= 1) and self.isBalanced(root.left) and self.isBalanced(root.right)
        
    
    def getHeight(self, root):
        if root is None:
            return -1 # No Nodes - 1 = -1 
        
        l = self.getHeight(root.left)
        r = self.getHeight(root.right)
        
        return max(l, r) + 1
        