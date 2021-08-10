class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_minimum_depth(root):
  q = []
  master = []

  q.append(root)

  while q:
    lvlSize = len(q)
    currLvl = []

    for node in range(lvlSize):
      popped = q.pop(0)
      if popped.left is None and popped.right is None: # leaf node
        return len(master) + 1  # master is all the levels above + 1 is this level

      if popped.left:
        q.append(popped.left)

      if popped.right:
        q.append(popped.right)

      currLvl.append(popped.val)

    master.append(currLvl)

  return len(master)


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
