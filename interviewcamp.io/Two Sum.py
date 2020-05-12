# 2 Sum Problem: Given a sorted array of integers, find two numbers in the
# array that sumto a given integer target.
# Return output as a pair of numbers
# no result = return none
# Array can have duplicates

# For example, if a = [1,2,3,5,6,7] and target = 11, the answer will be 5 and 6
# O(1) space, O(n) time

def twoSum(givenArr, target):

    if len(givenArr) == 0:
        return None

    start = 0
    end = len(givenArr)-1

    while (start != end):

        currSum = givenArr[start] + givenArr[end]

        if currSum == target:
            return str(givenArr[start]) + ", " + str(givenArr[end])

        elif currSum > target:
            end = end - 1

        elif currSum < target:
            start = start + 1

    return None


print(twoSum([10,1], 11))