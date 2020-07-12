from models import *

testList = LinkedList()

node1 = LinkedNode("first")
node2 = LinkedNode("sec")
node3 = LinkedNode("third")


testList.insert(node1)
testList.insert(node2)
testList.insert(node3)
testList.insert(LinkedNode("fourth"))


def getNthNode(LL, n):
    counter = 1
    curr = LL.getHead()
    while curr is not None and counter < n:
        curr = curr.getNext()
        counter = counter + 1

    return curr if counter == n else None


print(getNthNode(testList, 4))
print(testList.getTail().getData())










