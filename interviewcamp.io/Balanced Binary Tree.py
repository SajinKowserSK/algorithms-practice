# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def isBalanced(self, root):

        if root is None:
            return True

        if self.isBalanced(root.left) and self.isBalanced(root.right):
            return abs(self.height(root.left) - self.height(root.right)) <= 1

        return False

    def height(self, root):

        if root is None:
            return -1

        lHeight = self.height(root.left)
        rHeight = self.height(root.right)

        return (max(lHeight, rHeight) + 1)




