# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        if root is None:
            return 0

        global_sum = [-float('inf')]
        self.maxSum(root, global_sum)
        return global_sum[0]

    def maxSum(self, root, global_sum):
        if root is None:
            return 0

        left_sum = self.maxSum(root.left, global_sum)
        right_sum = self.maxSum(root.right, global_sum)

        left = max(0, left_sum)
        right = max(0, right_sum)

        global_sum[0] = max(global_sum[0], root.val + left + right)

        return root.val + max(left, right)
