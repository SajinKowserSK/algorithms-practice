# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None: # Empty input or single node 
            return head 
        
        start = head 
        right = self.getMid(start)
        
        tmp = right.next # reference before splitting 
        right.next = None 
        right = tmp # second half of list 
        
        leftHalf = self.sortList(start)
        rightHalf = self.sortList(right)
        
        return self.merge(leftHalf, rightHalf)
    
    def getMid(self, head):
        slow, fast = head, head.next 
        
        while fast and fast.next: # fast moves twice as fast as slow, so when slow is at the end, fast will be at half 
            slow = slow.next
            fast = fast.next.next 
            
        return slow 
    
    
    def merge(self, l1, l2):
        dummy = tail = ListNode()
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
                
            else:
                tail.next = l2
                l2 = l2.next
                
            tail = tail.next # set up for next connection
                
        # if any of the halves were bigger
        # connect, because these are already sorted 
        
        if l1:
            tail.next = l1
            
        if l2:
            tail.next = l2 
            
        return dummy.next # reference to sorted head 

            
        
            
    
        
        
        
            
        