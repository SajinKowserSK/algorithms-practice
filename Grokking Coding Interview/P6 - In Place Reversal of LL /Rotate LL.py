# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head is None:
            return None

        if head.next is None:
            return head

        curr = head
        prev, tail = None, None
        count = 0

        while curr:
            tail = curr
            curr = curr.next
            count += 1

        k = k % count

        while k > 0:
            rev_head = self.reverse(head)
            prev = rev_head.next
            head = self.reverse(rev_head)  # reversed back

            prev.next = None
            tail.next = head
            head = tail
            tail = prev

            k -= 1

        return head

    def reverse(self, head):
        curr = head
        prev = None
        while curr:
            nextN = curr.next
            curr.next = prev
            prev = curr
            curr = nextN

        return prev



