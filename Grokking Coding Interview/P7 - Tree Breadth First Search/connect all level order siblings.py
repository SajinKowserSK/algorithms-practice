from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # tree traversal using 'next' pointer
  def print_tree(self):
    print("Traversal using 'next' pointer: ", end='')
    current = self
    while current:
      print(str(current.val) + " ", end='')
      current = current.next


def connect_all_siblings(root):
  if root is None:
    return None

  allnodes = lvlTraversal(root)

  for x in range(0, len(allnodes)):
    lvl = allnodes[x]

    for node in range(0, len(lvl) - 1):
        curr_node = lvl[node]
        next_node = lvl[node + 1]

        curr_node.next = next_node

    if x != len(allnodes)-1:
      lvl[-1].next = allnodes[x+1][0]

    else:
      lvl[-1].next = None

  return



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
  connect_all_siblings(root)
  root.print_tree()


main()
