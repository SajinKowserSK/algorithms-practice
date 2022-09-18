"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        tmp = head  
        
        while tmp: # iterate until we find a child 
            if tmp.child:
                tmp_next = tmp.next # save refernece to next node 

                tmp_child = tmp.child 
                tmp_child_last = self.getLast(tmp_child)

                # insert the child chain in between tmp and tmp's next node 
                tmp_child.prev = tmp 
                tmp_child_last.next = tmp_next
                
                # update the tmp node and the next node's next/prev ptrs 
                tmp.next = tmp_child 
                
                if tmp_next:
                    tmp_next.prev = tmp_child_last 
                
                tmp.child = None 
            
            tmp = tmp.next
            
        return head 
            
            
        
        
        
    def getLast(self, head):
        tmp = head 
        while tmp and tmp.next:
            tmp = tmp.next 
        return tmp 
        