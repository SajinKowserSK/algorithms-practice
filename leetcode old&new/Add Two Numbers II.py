# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    
    def addTwoNumbers(self, l1, l2):
        
        # null checks
        if l1 is None:
            return l2
        
        elif l2 is None:
            return l1
        
        num1 = ""
        num2 = ""
        
        while l1 is not None:
            num1+=str(l1.val)
            l1 = l1.next
            
        while l2 is not None:
            num2 += str(l2.val)
            l2 = l2.next
            
        result = str(int(num1) + int(num2))
        
        
        retNode = ListNode(result[0])
        ptr = retNode
        
        for x in range (1, len(result)):
            ptr.next = ListNode(result[x])
            ptr = ptr.next
            
        
            
        return retNode
            
            
        
