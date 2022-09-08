# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True 
        
        if root:
            if self.sameTree(root, subRoot):
                return True 

            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
    def sameTree(self, p, q):
        if p is None and q is None:
            return True 
        
        if p is not None and q is not None:
            return (p.val == q.val and self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right))
        
        else:
            return False 
        