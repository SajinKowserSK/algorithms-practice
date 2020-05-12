# Given a sorted array in non-decreasing order, return an array of squares of each number, also in non-decreasing order. For example:
# [-4,-2,-1,0,3,5] -> [0,1,4,9,16,25]
# How can you do it in O(n) time?

def squaredArr(givenArr):

    if len(givenArr) == 0:
        return givenArr

    stk = []
    start = 0
    end = len(givenArr)-1

    while(start <= end):
        currStart = givenArr[start] ** 2
        currEnd = givenArr[end] ** 2

        if currStart > currEnd:
            stk.insert(0, currStart)
            start = start + 1

        else:
            stk.insert(0, currEnd)
            end = end - 1

    return stk

# test cases
# negs and positive nums
# all positive
print(squaredArr([1,2,3]))
# all negative
print(squaredArr([-1,-2,-3]))
# one element
print(squaredArr([-1]))
# null array
print(squaredArr([]))
