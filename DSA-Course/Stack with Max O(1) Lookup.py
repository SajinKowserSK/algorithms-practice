from models import Stack

class StackWithMax:
    def __init__(self):
        self.og = Stack()
        self.max = Stack()

    def push(self, item):
        if self.og.size() == 0:
            self.og.push(item)
            self.max.push(item)

        else:
            if item >= self.max.peek():
                self.max.push(item)

            self.og.push(item)

    def pop(self):
        if self.og.size == 0:
            print("Empty stack error")

        else:
            result = self.og.pop()
            if result == self.max.peek():
                self.max.pop()

            return result

    def show(self):
        print(self.og.show())

    def getMax(self):
        print(str(self.max.peek()))


testStk = StackWithMax()
# insert 1, 3, 2, check max, pop 2, check max, pop 3, check max

testStk.push(1)
testStk.push(3)
testStk.push(2)


testStk.pop()
testStk.show()
testStk.getMax()

testStk.pop()
testStk.show()
testStk.getMax()

