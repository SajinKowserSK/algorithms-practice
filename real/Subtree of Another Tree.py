def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

    def isEqual(s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False

        return s.val == t.val and isEqual(s.left,t.left) and isEqual(s.right, t.right)

    def traverse(s,t):
        return s and (isEqual(s,t) or traverse(s.left,t) or traverse(s.right,t))

    return traverse(s,t)
