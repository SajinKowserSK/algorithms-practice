from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_successor(root, key):

  q = []
  q.append(root)
  allnodes = []

  while q:
    lvlSize = len(q)

    for node in range(lvlSize):
      popped = q.pop(0)

      if popped.left:
        q.append(popped.left)

      if popped.right:
        q.append(popped.right)

      allnodes.append(popped)


  for x in range(0, len(allnodes)-1):
    value = allnodes[x].val
    if value == key:
      return allnodes[x+1]

  return None


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  result = find_successor(root, 12)
  if result:
    print(result.val)
  result = find_successor(root, 9)
  if result:
    print(result.val)


main()
