# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0 
        
        # need to get the max number of nodes from root -> leaf 
        currPath = [0]
        maxPath = [float('-inf')]
        
        self.helper(currPath, maxPath, root)
        return maxPath[0]
        
        
        
    def helper(self, currPath, maxPath, root):
        if root is None: 
            maxPath[0] = max(maxPath[0], currPath[0])
            
        else:
            currPath[0] += 1 # add one node to path counter var for processing curr node 
            nodeCounter = currPath[0]
            
            self.helper(currPath, maxPath, root.left)
            
            currPath[0] = nodeCounter # before sending to the right subtree, reset to the counter at this node 
            
            self.helper(currPath, maxPath, root.right)
            
            