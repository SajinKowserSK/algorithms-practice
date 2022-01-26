# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def helper(root, target):
            if root is not None:
                if root.val == target.val:
                    return True 
                
                return helper(root.left, target) or helper(root.right, target)
            
        print(root.val)
        if root.val == p or root.val == q:
            return root
            
        if (helper(root.left, p) and helper(root.right, q)) or (helper(root.left, q) and helper(root.right, p)):
            return root 
        
        if helper(root.left, p) and helper(root.left, q): # both on left branch
            return self.lowestCommonAncestor(root.left, p, q)
        
        if helper(root.right, p) and helper(root.right, q): #both on right branch 
            return self.lowestCommonAncestor(root.right, p, q)
        
        return root
        
        
        
        
        
        
  
                