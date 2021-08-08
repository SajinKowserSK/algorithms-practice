# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def searchBST(self, root, val):
        
        if root:
            if root.val < val and root.right:
                return self.searchBST(root.right, val)
                
            elif root.val > val and root.left:
                return self.searchBST(root.left, val)
                
            elif root.val == val:
                return root 
            
        return None 
       
        
