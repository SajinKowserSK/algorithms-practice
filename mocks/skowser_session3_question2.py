class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

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


class Queue:
    def __init__(self):
        self.stk1 = Stack()
        self.stk2 = Stack()

    def flush(self, stkOG, stkTO):
        while not stkOG.isEmpty():
            stkTO.push(stkOG.pop())

    def push(self, item):
        self.stk1.push(item)

    def peek(self):
        if self.stk1.isEmpty():
            return None

        self.flush(self.stk1, self.stk2)

        peek = self.stk2.peek()
        self.flush(self.stk2, self.stk1)
        return peek


    def pop(self):
        if self.stk1.isEmpty():
            return None

        self.flush(self.stk1, self.stk2)

        popped = self.stk2.pop()
        self.flush(self.stk2, self.stk1)
        return popped

    def empty(self):
        return self.stk1.isEmpty()

queue = Queue()
queue.push(2)
queue.push(3)

print(queue.peek()) # 2
print(queue.pop()) # 2
print(queue.empty()) # False


queue = Queue()
queue.push(5)

print(queue.peek()) # 5
print(queue.pop()) # 5
print(queue.empty()) # True
