from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def tree_right_view(root):
  result = []
  allnodes = lvlTraversal(root)

  for lvl in allnodes:
    result.append(lvl[-1])
  return result

def lvlTraversal(root):
    master = []
    q = []
    q.append(root)

    while q:
        lvlSize = len(q)
        currLvl = []

        for node in range(lvlSize):
            popped = q.pop(0)

            if popped.left:
                q.append(popped.left)

            if popped.right:
                q.append(popped.right)

            currLvl.append(popped)

        master.append(currLvl)

    return master

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.left.left.left = TreeNode(3)
  result = tree_right_view(root)
  print("Tree right view: ")
  for node in result:
    print(str(node.val) + " ", end='')


main()







