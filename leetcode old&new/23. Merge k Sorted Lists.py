import heapq


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        heap = []

        heapq.heapify(heap)

        for lst in lists:
            curr = lst
            while curr:
                heapq.heappush(heap, curr.val)
                curr = curr.next

        if len(heap) == 0:
            return None

        arr = []

        while heap:
            popped = heapq.heappop(heap)
            arr.append(ListNode(popped))

        head = arr[0]
        curr = head

        for x in range(1, len(arr)):
            curr.next = arr[x]
            curr = curr.next

        curr.next = None

        return head









