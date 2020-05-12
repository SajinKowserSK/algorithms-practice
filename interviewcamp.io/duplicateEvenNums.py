# given an array, duplicate it's even elements
# Do in O(n) time and O(1) space
# Assume list has enough space to hold correct solution, all unused spaces = -1
# [1,2,3,4] -> [1,2,2,3,4,4]

def cloneEvenNums(givenArr):

    if len(givenArr) == 0:
        return givenArr

    endIndex = len(givenArr)-1
    lastNumindex = findLastNum(givenArr)
    print(lastNumindex)


    for x in range(lastNumindex, -1, -1):
        currNum = givenArr[x]

        if currNum % 2 == 0:
            givenArr[endIndex] = currNum
            endIndex = endIndex - 1
            givenArr[endIndex] = currNum
            endIndex = endIndex - 1

        else:
            givenArr[endIndex] = currNum
            endIndex = endIndex - 1

    return givenArr

def findLastNum(givenArr):
    for x in range(0, len(givenArr)):
        if givenArr[x] == -1:
            return x-1
    return x


print(cloneEvenNums([1,2,3,4,-1,-1]))






