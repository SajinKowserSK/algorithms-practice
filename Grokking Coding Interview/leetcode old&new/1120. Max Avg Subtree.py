# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        tmap = {}
        self.traverse(root, tmap)
        print(tmap)

        max_val = float("-inf")

        for key in tmap:
            vals = tmap[key]
            curr_avg = vals[0]
            max_val = max(max_val, curr_avg)

        return max_val

    def traverse(self, root, tmap):
        if root is None:
            return (0, 0)

        l = self.traverse(root.left, tmap)
        r = self.traverse(root.right, tmap)

        sum_val = (l[0] * l[1] + r[0] * r[1] + root.val)
        len_vals = (l[1] + r[1] + 1)
        avg_val = float(sum_val / len_vals)

        tmap[root] = (avg_val, len_vals)
        return tmap[root]