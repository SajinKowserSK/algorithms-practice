from models import *

def sortLL(LL):
    zeros = LinkedList()
    ones = LinkedList()
    twos = LinkedList()

    curr = LL.getHead()

    while curr is not None:
        curr1 = LinkedNode(curr.getData())
        if curr.getData() == 0:
            zeros.insert(curr1)


        elif curr.getData() == 1:
            ones.insert(curr1)


        else:
            twos.insert(curr1)


        curr = curr.getNext()

    zeros.insert(ones.getHead())
    zeros.insert(twos.getHead())


    return zeros.show()

testList = createLL([2,1,1,2,2,2,1])
print(sortLL(testList))


