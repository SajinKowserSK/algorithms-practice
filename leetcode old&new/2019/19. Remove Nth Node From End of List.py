class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        slow = head
        fast = head

        for x in range(0, n):
            fast = fast.next

        prev = None
        slow_head = slow

        while fast != None:
            prev = slow
            slow = slow.next
            fast = fast.next

        if prev != None:
            prev.next = slow.next
            return slow_head

        return prev