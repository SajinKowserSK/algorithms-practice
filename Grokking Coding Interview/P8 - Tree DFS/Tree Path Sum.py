# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        pSum = 0
        return self.pathSum(root, targetSum, pSum)

    def pathSum(self, root, targetSum, pSum):
        if root is not None and root.left is None and root.right is None:
            pSum += root.val
            return pSum == targetSum

        elif root is not None:
            pSum += root.val
            if self.pathSum(root.left, targetSum, pSum):
                return True

            if self.pathSum(root.right, targetSum, pSum):
                return True

            return False


