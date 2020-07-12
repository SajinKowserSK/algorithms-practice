from models import *

testList = LinkedList()

node1 = LinkedNode("first")
node2 = LinkedNode("sec")
node3 = LinkedNode("third")

testList.setHead(node1)
node1.setNext(node2)
node2.setNext(node3)


def getNthNode(LL, n):
    counter = 1
    curr = LL.getHead()
    while curr is not None and counter < n:
        curr = curr.getNext()
        counter = counter + 1

    return curr if counter == n else None


print(getNthNode(testList, 3).getData())









