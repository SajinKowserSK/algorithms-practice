# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxVal = [float('-inf')]
        self.helper(root, maxVal)
        return maxVal[0]
    
    
    def helper(self, root, maxVal):
        if root is None: 
            return 0  # base case 
        else:
            
            l_sum = self.helper(root.left, maxVal)
            r_sum = self.helper(root.right, maxVal)

            # in case of negative, we want to discard this
            l_sum = max(0, l_sum)
            r_sum = max(0, r_sum)

            # imitates a path like rChild + root + lChild sums 
            maxVal[0] = max(maxVal[0], l_sum + root.val + r_sum)


            # each subroot can only take one side (left or right) to add to path 
            return root.val + max(l_sum, r_sum)

        
            
        
        