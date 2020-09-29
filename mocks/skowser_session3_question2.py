# assumes all operations are valid (none called on empty queue except push or empty)

class Queue:
    def __init__(self):
        self.q = []

    def push(self, item):
        self.q.append(item)

    def pop(self):
        return self.q.pop(0)

    def peek(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0

queue = Queue()
queue.push(2)
queue.push(3)
print(queue.q) # [2,3]

print(queue.peek()) # 2
print(queue.pop()) # 2
print(queue.empty()) # False


queue = Queue()
queue.push(5)
print(queue.q) # [5]

print(queue.peek()) # 5
print(queue.pop()) # 5
print(queue.empty()) # True

