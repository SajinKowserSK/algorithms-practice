from models import *

test = circularQueue(4)
for x in range(0, 4):
    test.enqueue(x)
    test.show()

test.dequeue()

test.show()
test.enqueue(5)
test.show()
test.dequeue()
test.show()