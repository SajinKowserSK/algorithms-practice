"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        map2Node = {}

        curr = head

        pre = Node(-1)
        prev = pre

        while curr:
            copy = Node(curr.val)
            map2Node[curr] = copy

            if prev == pre:
                prev = copy
                pre.next = prev

            else:
                prev.next = copy
                prev = prev.next

            curr = curr.next

        prev.next = None

        curr = head
        while curr:
            copy = map2Node[curr]

            if curr.random not in map2Node:
                random_copy = None

            else:
                random_copy = map2Node[curr.random]

            copy.random = random_copy

            curr = curr.next

        return pre.next


