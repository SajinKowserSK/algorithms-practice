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

        # have to iterate through and do 3 main things
        # 1) copy the node + place it in the hashmap
        # 2) create a start ptr for reference to the copied list's head
        # 3) continously update prev
        while curr:
            copy = Node(curr.val)
            real2c[curr] = copy

            if prev != None:
                prev.next = copy

            else:
                prev = copy
                start = prev # very very important step, have to create "start" ptr

            curr = curr.next

            if prev.next != None:
                prev = prev.next

        prev.next = None
        curr = head

        while curr:
            random_node = curr.random
            copy_random = real2c.get(random_node, None)

            curr_node_copy = real2c[curr]

            curr_node_copy.random = copy_random

            curr = curr.next

        return start

