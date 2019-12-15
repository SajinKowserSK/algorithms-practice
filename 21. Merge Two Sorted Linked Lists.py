# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        
        
        retL = []
        c1 = l1;
        c2 = l2;
                
        while c1 != None:
            
            retL.append(c1.val)
            c1 = c1.next
            
        while c2 != None:
            retL.append(c2.val)
            c2 = c2.next
            
        retL.sort()
        
        if len(retL) < 1:
            return l1
        
        rLL = ListNode(retL[0])
        curr = rLL
        
        for x in range (1, len(retL)):
            n = ListNode(retL[x])
            curr.next = n
            curr = curr.next
            
        return rLL
            
        