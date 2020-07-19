class listNode: 
    def __init__(self, val):
        self.val = val
        self.next = None 
        
    def setNext(self, node):
        self.next = node 



node1 = listNode(1)
node2 = listNode(2)
node3 = listNode(3)
node4 = listNode(4)


node1.next = node2
node2.next = node3 
node3.next = node4

def findMid(head):
    cF = head
    cS = head 
    
    while cF is not None and cF.next is not None:
        cF = cF.next.next 
        cS= cS.next 
        
    return cS.val

print(findMid(node1))
    
