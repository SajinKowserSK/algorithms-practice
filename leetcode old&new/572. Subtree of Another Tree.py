# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        stop = [False]
        self.traverse(s, t, stop)
        return True if stop[0] else False

    def traverse(self, root, sub, stop):
        if root is None and sub is None:
            return True

        if root is None or sub is None:
            return False

        if self.equals(root, sub):
            stop[0] = True
            return True

        if stop[0] != True:
            self.traverse(root.left, sub, stop)
            self.traverse(root.right, sub, stop)

    def equals(self, root, sub):
        if root is None and sub is None:
            return True

        if root is None or sub is None:
            return False

        return root.val == sub.val and self.equals(root.left, sub.left) and self.equals(root.right, sub.right)






