from models import *

# first check if toDelete is null
# case 1 is toDelete is head -> set head to head.next
# case 2 is toDelete is tail -> tail = prev
# case 3 is in between/middle -> make prev = curr.next
def delete(toDelete, prev, LL):
    if toDelete is None:
        return LL

    LLhead = LL.getHead()
    LLtail = LL.getTail()

    if toDelete == LLhead:
        LL.setHead(LLhead.getNext())

    if toDelete == LLtail:
        LL.setTail(prev)

    if prev is not None:
        prev.setNext(toDelete.getNext())


    return LL.show()



testList = LinkedList()

node1 = LinkedNode("first")
node2 = LinkedNode("sec")
node3 = LinkedNode("third")


testList.insert(node1)
testList.insert(node2)
testList.insert(node3)
testList.insert(LinkedNode("fourth"))

print(delete(LinkedNode("fourth"), node3, testList))


