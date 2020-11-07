# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0

        ans = [0]

        self.post_order(root, ans)
        return ans[0]

    def post_order(self, root, lst):
        if root is not None:
            l_height = self.height(root.left) + 1
            r_height = self.height(root.right) + 1

            lst[0] = max(lst[0], l_height + r_height)

            self.post_order(root.left, lst)
            self.post_order(root.right, lst)

    def height(self, root):
        if root is None:
            return -1

        l_height = self.height(root.left)
        r_height = self.height(root.right)

        return max(l_height, r_height) + 1
