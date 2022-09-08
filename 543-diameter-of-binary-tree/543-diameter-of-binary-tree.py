# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter is defined by length of longest path between any two nodes in tree
        # we need to get the height of left subtree & right subtree 
        # then return the max sum of this for EVERY NODE as it won't always pass through root 
        
        if root is None: 
            return 0 
        
        ans = [0]
        self.helper(ans, root)
        return ans[0]
    
    def helper(self, ans, root):
        if root:
            # the + 1 here indicates adding back 1 from "h = # nodes - 1" to get # of nodes in path
            leftPath = self.getHeight(root.left) + 1 
            rightPath = self.getHeight(root.right) + 1 

            ans[0] = max(ans[0], leftPath + rightPath)
            self.helper(ans, root.left)
            self.helper(ans, root.right)
        
        
    def getHeight(self, root):
        # height of tree = # of nodes - 1 
        
        if root is None:
            return -1 
        
        if root.left is None and root.right is None:
            return 0 
        
        else:
            left = self.getHeight(root.left)
            right = self.getHeight(root.right)
            
            return max(left, right) + 1 
            
        
        
        