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
        
        maxNum = [float('-inf')]
        currCounter = [0]
        self.helper(root, currCounter, maxNum)
        return maxNum[0]
        
        
    def helper(self, root, currCounter, maxCounter):
        if root is None:
            maxCounter[0] = max(maxCounter[0], currCounter[0])
            
        else:
            currCounter[0] += 1 #processes current root
            rootCounter = currCounter[0]
            
            self.helper(root.left, currCounter, maxCounter)
    
            currCounter[0] = rootCounter
            
            self.helper(root.right, currCounter, maxCounter)
        
             
        