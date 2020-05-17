# Level: Medium
# Note: This solution uses Enums and Exceptions.
# While optional, it always looks good if you use them in an interview.
# You're given a list of Marbles. Each marble can have one of 3 colors (Red, White or Blue).'
# Arrange the marbles in order of the colors (Red -> White -> Blue).Colors are represented as follows: 0 - Red, 1 - White, 2 - Blue

class Marbel:
    def __init__(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color


def arrange(arr):
    startBoundary = 0
    endBoundary = len(arr)-1

    i = 0

    while i <= endBoundary:
        curr = arr[i]
        if curr.getColor() == 0:
            swap(i, startBoundary, arr)
            startBoundary = startBoundary + 1
            i = i + 1

        elif curr.getColor() == 2:
            swap(i, endBoundary, arr)
            endBoundary = endBoundary - 1

        elif curr.getColor() == 1:
            i = i + 1

        else:
            raise ValueError("unknown color")

    # testing purposes
    for x in range (0, len(arr)):
        print(arr[x].getColor())

    return arr


def swap(pos1, pos2, arr):
    tmp = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = tmp

    return arr

test = [Marbel(2), Marbel(0), Marbel(0), Marbel(2), Marbel(1)]
print(arrange(test))


