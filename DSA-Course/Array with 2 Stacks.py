class arrDoubleStack:

    def __init__(self, fixedSize):
        self.arr = []

        for x in range (0, fixedSize):
            self.arr.append(" ")

        self.s1 = 0
        self.s2 = len(self.arr)-1


    def push(self, stkNum, item):
        if stkNum != 1 and stkNum != 2:
            return "Invalid stkNum"

        else:
            if self.s1 > self.s2:
                return "stk is full"

            if stkNum == 1:
                self.arr[self.s1] = item
                self.s1 += 1

            else:
                self.arr[self.s2] = item
                self.s2 -= 1


    def peek(self, stkNum):
        if stkNum == 1 and self.s1 > 0:
            return self.arr[self.s1-1]

        if stkNum == 2 and self.s2 < len(self.arr)-1:
            return self.arr[self.s2+1]

        else:
            return "No element to peek"

    def pop(self, stkNum):
        if stkNum != 1 and stkNum != 2:
            return "Invalid stkNum"

        if stkNum == 1 and self.s1 > 0:
            result = self.peek(1)
            self.arr[self.s1-1] = " "
            self.s1 -= 1
            return result

        elif stkNum == 2 and self.s2 < len(self.arr)-1:
            result = self.peek(2)
            self.arr[self.s2+1] = " "
            self.s2 += 1
            return result

        else:
            return "Out of bounds error"

doubleStack = arrDoubleStack(5)
print(doubleStack.peek(1))

# PUSH
doubleStack.push(1,2)
doubleStack.push(1,3)
doubleStack.push(1,4)
doubleStack.push(2,3)
doubleStack.push(2,5)

# POP
# print(doubleStack.pop(1))
print(doubleStack.pop(1))
print(doubleStack.pop(2))
print(doubleStack.pop(2))
print(doubleStack.pop(2))
print(doubleStack.arr)




