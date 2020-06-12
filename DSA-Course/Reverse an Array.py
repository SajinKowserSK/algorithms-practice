# Given an array, reverse the order of its elements
# For example, [3,5,2,5,2,3,9] → [9,3,2,5,2,5,3]
# Modify existing array, O(n) time, O(1) space

def reverseArray(givenArr):

    if len(givenArr) == 0:
        return givenArr

    start = 0
    end = len(givenArr)-1

    while start != end:
        tmp = givenArr[end]
        givenArr[end] = givenArr[start]
        givenArr[start] = tmp
        start = start + 1
        end = end - 1

    return givenArr

print(reverseArray([]))

# test cases
# normal mix
# empty array