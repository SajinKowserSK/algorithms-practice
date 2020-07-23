from models import *




test2 = regQueue()
node1 = LinkedNode(1)
node2=LinkedNode(2)
test2.enqueue(node1)
test2.enqueue(node2)
print(test2.head.data)
print(test2.tail.data)
test2.dequeue()
print(test2.head.data)
print(test2.tail.data)







