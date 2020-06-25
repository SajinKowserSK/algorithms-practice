# Medium
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        
        if root:
            if root.val < val:
                
                if root.right:
                    self.insertIntoBST(root.right, val)
                
                else:
                    root.right = TreeNode(val, None, None)
                
            else:
                if root.left:       
                    self.insertIntoBST(root.left, val)
                else:
                    root.left = TreeNode(val, None, None)
                
        else:
            root = TreeNode(val, None, None)
            
        return root 
                
        