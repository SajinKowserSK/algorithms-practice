from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    # level order traversal using 'next' pointer
    def print_level_order(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                print(str(current.val) + " ", end='')
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
            print()


def connect_level_order_siblings(root):
    allnodes = lvlTraversal(root)

    for lvl in allnodes:
        for node in range(0, len(lvl) - 1):
            curr_node = lvl[node]
            next_node = lvl[node + 1]

            curr_node.next = next_node

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
    connect_level_order_siblings(root)

    print("Level order traversal using 'next' pointer: ")
    root.print_level_order()


main()
