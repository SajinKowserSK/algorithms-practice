
from models import * 

class QueueWithMax:
    
    def __init__(self):
        self.main = regQueue()
        self.max = regQueue()
        
    def enqueue(self, node):
        if node is None:
            return None 
        
        else:
            self.main.enqueue(node)
            
            while  self.max.head is not None and self.max.tail.data < node.data:
                self.max.dequeue()
                
            self.max.enqueue(node)
          
            
    
    def dequeue(self):
        if self.main.head is None:
            print("empty queue")
            return 
            
        else:
            result = self.main.dequeue()
            
            if self.max.head == result:
                self.max.dequeue()
                
        
    def getMax(self):
        if self.max.head is None:
            print("empty queue")
            return
            
        else:
            return self.max.head
        
        

test = QueueWithMax()

arr = [4,2,5,1]
for x in range(0, len(arr)):
    test.enqueue(LinkedNode(arr[x]))


print(test.getMax().data)
    
