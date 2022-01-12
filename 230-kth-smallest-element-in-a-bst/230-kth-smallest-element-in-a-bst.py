# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lst = []
        self.helper(root, lst)
        return lst[k-1]
        
        
        
    def helper(self, root, lst):
        
        if root is not None:
            self.helper(root.left, lst)
            lst.append(root.val)
            self.helper(root.right, lst)
        