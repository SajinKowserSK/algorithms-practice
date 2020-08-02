class Graph:
    def __init__(self, Nodes, isDirected=False):
        self.nodes = Nodes
        self.adjList = {}
        self.isDirected = isDirected

        for node in self.nodes:
            self.adjList[node] = []


    def addEdge(self, u, v):


        if v not in self.adjList[u]:
            self.adjList[u].append(v)

        if self.isDirected is not True and u not in self.adjList[v]:
            self.adjList[v].append(u)


    def showList(self):
        for node in self.nodes:

            neighbors = self.adjList[node]
            neighborVals = []

            for x in range (0, len(neighbors)):
                neighborVals.append(neighbors[x].data)

            print(str(node.data) + "->" + str(neighborVals))
        print('\n')

    def degree(self, node):
        return len(self.adjList[node.data])

    def reset(self):
        for node in self.nodes:
            node.state = "unvisited"

class Vertex:
    def __init__(self, data):
        self.data = data
        self.state = "unvisited"

class BinaryNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getVal(self):
        return self.data

    def isLeaf(self):
        return True if self.left is None and self.right is None else False

    # binary search type of insert
    def insertNode(self, data):

        if self.data == None:
            self.data = data

        else:
            if data > self.data:

                if self.right is None:
                    self.right = BinaryNode(data)

                else:
                    self.right.insertNode(data)

            elif data < self.data:

                if self.left is None:
                    self.left = BinaryNode(data)

                else:
                    self.left.insertNode(data)


def createTree(lst):
    root = BinaryNode(lst[0])
    for x in range (1, len(lst)):
        root.insertNode(lst[x])

    return root

def createLL(lst):
    retList = LinkedList()
    for x in range(0, len(lst)):
        node = LinkedNode(lst[x])
        retList.insert(node)

    retList.findTail()
    return retList

def inOrder(root):
    if root is None:
        return None

    inOrder(root.left)
    print(root.data)
    inOrder(root.right)

class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def setNext(self, node):
        self.next = node

    def setData(self, data):
        self.data = data

    def getNext(self):
        return self.next

    def getData(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        self.head = node

    def getHead(self):
        return self.head

    def setTail(self, node):
        self.tail = node


    def findTail(self):
        curr = self.head
        while curr.getNext() is not None:
            curr = curr.getNext()

        self.tail = curr
        return self.tail

    def getTail(self):
        return self.tail

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.getData())
            curr = curr.getNext()

        return ""

    def insert(self, node):
        if self.head is None:
            self.head = node

        else:
            self.findTail().setNext(node)


        self.tail = node

class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    # adds to front bc LIFO
    def push(self, item):
        self.stack.insert(0, item)

    def pop(self):
        if len(self.stack) > 0:
            front = self.stack[0]
            self.stack.remove(front)
            return front
        else:
            return None

    def peek(self):
        if len(self.stack) == 0:
            return None

        else:
            return self.stack[0]


    def size(self):
        return len(self.stack)

    def show(self):
        return self.stack

    def printStk(self):
        print(self.stack)

class circularQueue:
    def __init__(self, size):
        self.arr = []
        self.front = 0
        self.back = 0
        self.max = size
        self.len = 0

        for x in range(0, size):
            self.arr.append(None)

    def enqueue(self, n):
        if self.len == self.max:
            print("Queue is full")
            return

        self.arr[self.back] = n
        self.back = (self.back + 1) % self.max
        self.len += 1


    def dequeue(self):
        if self.len == 0:
            print("Queue is empty")
            return

        result = self.arr[self.front]
        self.arr[self.front] = None
        self.front = (self.front + 1) % self.max
        self.len -= 1
        return result

    def show(self):
        print(self.arr)


class regQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, node):
        if self.head is None:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            self.tail = node


    def dequeue(self):
        if self.head is None:
            print("Empty Queue")

        else:
            self.head = self.head.next



class Queue:
    def __init__(self):
        self.stk1 = Stack()
        self.stk2 = Stack()

    def flush(self, stkOG, stkTO):
        while not stkOG.isEmpty():
            stkTO.push(stkOG.pop())

    def enqueue(self, item):
        self.stk1.push(item)

    def dequeue(self):
        if self.stk1.isEmpty():
            return None

        self.flush(self.stk1, self.stk2)

        self.stk2.pop()
        self.flush(self.stk2, self.stk1)

    def show(self):
        lifo = self.stk1.show()

        if len(lifo) == 0:
            return []


        start = 0
        end = len(lifo)-1


        while start <= end:

            tmp = lifo[start]
            lifo[start] = lifo[end]
            lifo[end] = tmp

            start += 1
            end -= 1

        print(lifo)
        return lifo




