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

        if head is None:
            return None

        curr = head
        prev = None

        real2c = {}

        while curr:
            copy = Node(curr.val)
            real2c[curr] = copy

            if prev != None:
                prev.next = copy

            else:
                prev = copy
                start = prev

            curr = curr.next

            if prev.next != None:
                prev = prev.next

        prev.next = None
        final = prev.next

        copy_curr = start
        curr = head

        while curr:
            random_node = curr.random
            copy_random = real2c.get(random_node, None)

            curr_node_copy = real2c[curr]

            curr_node_copy.random = copy_random

            curr = curr.next

        return start

