# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val == p.val or root.val == q.val:
            return root 
        
        if root.left is None and root.right is None:
            return None 
        
        left, right = None, None
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
            
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)
            
        if left and right:
            return root 
        
        if left:
            return left
        
        else:
            return right 
        