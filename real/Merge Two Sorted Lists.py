# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre_start = ListNode(-1)
        prev = pre_start

        curr1 = l1
        curr2 = l2

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                prev.next = curr1
                curr1 = curr1.next

            else:
                prev.next = curr2
                curr2 = curr2.next

            prev = prev.next

        if curr1:
            prev.next = curr1

        else:
            prev.next = curr2

        return pre_start.next
    
    def mergeTwoLists2(self, l2: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists2(l1.next, l2)
            return l1
        
        l2.next = self.mergeTwoLists2(l1, l2.next)
        return l2
    
