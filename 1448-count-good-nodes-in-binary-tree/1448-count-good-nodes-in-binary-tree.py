# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # need to keep a maxCounter to see the max val up to this path 
        # as we traverse every node, check if current node is greater than the max val 
        
        if root is None:
            return 0 
        
        goodNodes = [0] 
        maxVal = [float('-inf')]
        self.helper(root, maxVal, goodNodes)
        
        return goodNodes[0]
    
    def helper(self, root, maxVal, goodNodes):
        if root:
            
            if root.val >= maxVal[0]:
                goodNodes[0] += 1 
                maxVal[0] = root.val
            
            currNodeMaxVal = maxVal[0]
            
            # go left
            self.helper(root.left, maxVal, goodNodes)
            
            # reset path max before checking right
            maxVal[0] = currNodeMaxVal
            
            self.helper(root.right, maxVal, goodNodes)
            
             