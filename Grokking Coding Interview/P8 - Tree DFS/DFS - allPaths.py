# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        allpaths, lst = [], []

        if root is None:
            return allpaths

        pSum = 0
        self.helper(root, targetSum, pSum, lst, allpaths)
        return allpaths

    def helper(self, root, targetSum, pSum, lst, allpaths):
        if root is not None and root.left is None and root.right is None:
            pSum += root.val
            lst.append(root.val)

            if pSum == targetSum:
                allpaths.append(lst.copy())

            pSum -= root.val
            lst.pop(-1)

        elif root is not None:
            pSum += root.val
            lst.append(root.val)

            self.helper(root.left, targetSum, pSum, lst, allpaths)
            self.helper(root.right, targetSum, pSum, lst, allpaths)

            pSum -= root.val
            lst.pop(-1)