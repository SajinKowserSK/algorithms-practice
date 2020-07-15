# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        myMap = {} 
        
        curr1 = headA
        curr2 = headB 
        
        while curr1 is not None:
            myMap[curr1] = True 
            curr1 = curr1.next
            
        while curr2 is not None:
            if curr2 in myMap and myMap[curr2] == True:
                return curr2
            
            else:
                curr2 = curr2.next
                
        return None 
        
