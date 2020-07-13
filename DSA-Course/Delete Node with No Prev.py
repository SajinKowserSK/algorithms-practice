from models import *

# new trick to delete node in O(1) time
# caveat is not actually deleting node but copying the next node over and deleting next node
# another caveat is cannot do it to tail because None val can't be copied over


def deleteConstantTime(toDelete, LL):
    if toDelete is None:
        return LL

    LLhead = LL.getHead()

    if toDelete == LLhead:
        LLhead.data = LLhead.getNext().getData()
        LL = delete(toDelete.getNext(), toDelete, LL)

    else:
        toDelete.data = toDelete.getNext().data
        LL = delete(toDelete.getNext(), toDelete, LL)

    return LL.show()


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


    return LL


testList = LinkedList()

node1 = LinkedNode("first")
node2 = LinkedNode("sec")
node3 = LinkedNode("third")


testList.insert(node1)
testList.insert(node2)
testList.insert(node3)
testList.insert(LinkedNode("fourth"))

print(deleteConstantTime(node3, testList))


